from flask import Flask, render_template, request, redirect, url_for, session
from game_v1 import StonePaperScissors

app = Flask(__name__)
app.secret_key = "stone-paper-scissors-secret"  # Needed for session
game = None  # Will be initialized per session


# Start page: choose mode
@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        mode = request.form.get("mode")
        session["mode"] = mode
        if mode == "computer":
            return redirect(url_for("choose_difficulty"))
        else:
            return redirect(url_for("play_human"))
    return render_template("start.html")


# Two-player (human vs human) mode
@app.route("/play_human", methods=["GET", "POST"])
def play_human():
    global game
    if not game or game.mode != "human":
        game = StonePaperScissors(mode="human")
    user1_choice = session.get("user1_choice")
    user2_choice = session.get("user2_choice")
    result = None
    winner_popup = None

    if request.method == "POST":
        if not user1_choice and "user1_choice" in request.form:
            user1_choice = request.form["user1_choice"]
            session["user1_choice"] = user1_choice
        elif user1_choice and not user2_choice and "user2_choice" in request.form:
            user2_choice = request.form["user2_choice"]
            session["user2_choice"] = user2_choice

    # If both choices are made, determine winner
    if user1_choice and user2_choice:
        winner = game.determine_winner(user1_choice, user2_choice)
        if winner == "draw":
            result = "It's a draw!"
        elif winner == "user1":
            result = "Player 1 wins the round! 🎉"
        else:
            result = "Player 2 wins the round! 🎉"

        # Apply scoring for non-draw rounds
        if winner in ("user1", "user2"):
            match_winner = game.apply_round_winner(winner)
            if match_winner:
                winner_popup = "Player 1" if match_winner == "user1" else "Player 2"
                # Reset scores for next match automatically after popup
                game.reset_scores()

        # Reset round choices for next round
        session.pop("user1_choice")
        session.pop("user2_choice")
        user1_choice = None
        user2_choice = None

    return render_template(
        "human.html",
        choices=game.CHOICES,
        user1_choice=user1_choice,
        user2_choice=user2_choice,
        result=result,
        user1_score=game.user1_score,
        user2_score=game.user2_score,
        winner_popup=winner_popup
    )

@app.route("/choose_difficulty", methods=["GET", "POST"])
def choose_difficulty():
    if request.method == "POST":
        difficulty = request.form.get("difficulty")
        session["difficulty"] = difficulty
        return redirect(url_for("play_computer"))
    return render_template("difficulty.html")

# Play vs Computer route
@app.route("/play_computer", methods=["GET", "POST"])
def play_computer():
    global game
    result = None
    user_choice = None
    computer_choice = None
    winner_popup = None
    # Get difficulty from session
    difficulty = session.get("difficulty", "easy")
    if not game or game.difficulty != difficulty:
        game = StonePaperScissors(mode="computer", difficulty=difficulty)

    if request.method == "POST":
        user_choice = request.form["choice"]
        # For hard mode, computer picks after user
        if difficulty == "hard":
            computer_choice = game.get_computer_choice(user_choice)
        else:
            computer_choice = game.get_computer_choice()
        winner = game.determine_winner(user_choice, computer_choice)
        game.update_last(user_choice, winner)

        if winner == "draw":
            result = "It's a draw!"
        elif winner == "user1":
            result = "You win the round! 🎉"
        else:
            result = "Computer wins the round! 💻"

        if winner in ("user1", "user2"):
            match_winner = game.apply_round_winner(winner)
            if match_winner:
                winner_popup = "You" if match_winner == "user1" else "Computer"
                game.reset_scores()

    return render_template(
        "index.html",
        choices=game.CHOICES,
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        user_score=game.user1_score,
        computer_score=game.user2_score,
        winner_popup=winner_popup
    )

if __name__ == "__main__":
    app.run(debug=True)
