import json
from django.http import JsonResponse
from .models import Player
from .validators import *
from django.shortcuts import get_object_or_404


def authenticate(request):
    if request.method != "POST":
        return JsonResponse({}, status=405)  # Method Not Allowed

    try:
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        if not username or not password:
            return JsonResponse({}, status=400)  # Bad Request

        player = get_object_or_404(Player, username=username)

        if player.password == password:
            return JsonResponse({}, status=200)  # OK
        else:
            return JsonResponse({}, status=401)  # Unauthorized

    except json.JSONDecodeError:
        return JsonResponse({}, status=400)  # Bad Request


def signup(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)  # Method Not Allowed

    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        age = data.get('age')
        email = data.get('email')

        if username is None or password is None or age is None:
            return JsonResponse({}, status=400)  # Bad Request

        # Validate username, password, and age using the model's validators
        if not validate_username(username) or not validate_password(password) or not validate_age(age):
            return JsonResponse({}, status=400)  # Bad Request

        # Create the Player object
        player = Player(username=username, password=password, age=age)

        if email:
            player.email = email

        player.save()

        return JsonResponse({}, status=201)  # Created

    except json.JSONDecodeError:
        return JsonResponse({}, status=400)  # Bad Request


def profile(request, username):
    if request.method == "GET":
        try:
            player = Player.objects.get(username=username)
        except Player.DoesNotExist:
            return JsonResponse({}, status=404)
        response_body = {
            "username": player.username,
            "rank": player.get_rank_display(),
            "score": float(player.score)
        }
        return JsonResponse(response_body, status=200)

    elif request.method == "PUT":
        if "auth-token" not in request.headers:
            return JsonResponse({}, status=401)  # Unauthorized

        auth_token = request.headers["auth-token"]
        if auth_token[::-1] != auth_token:
            return JsonResponse({}, status=401)  # Unauthorized

        try:
            player = Player.objects.get(username=username)
        except Player.DoesNotExist:
            return JsonResponse({}, status=404)

        try:
            request_data = json.loads(request.body)
            password = request_data.get("password")
            age = request_data.get("age")
            email = request_data.get("email")

            if not password or not age or not email:
                return JsonResponse({}, status=400)  # Bad Request

            validate_password(password)
            validate_age(age)

            player.password = password
            player.age = age
            if email != "null":
                player.email = email
            player.save()

            return JsonResponse({}, status=200)  # OK

        except json.JSONDecodeError:
            return JsonResponse({}, status=400)  # Bad Request

    else:
        return JsonResponse({}, status=405)  # Method Not Allowed


def scoreboard(request):
    if request.method == "GET":
        return handle_get_request(request)
    elif request.method == "PUT":
        return handle_put_request(request)
    else:
        return JsonResponse({}, status=405)


def handle_get_request(request):
    start = request.GET.get("start")
    end = request.GET.get("end")
    if not start or not end:
        return JsonResponse({}, status=400)  # Bad Request
    try:
        start = int(start)
        end = int(end)

        if end - start > 10:
            return JsonResponse({}, status=400)  # Bad Request

        players = Player.objects.order_by("-score", "username")[start:end]

        players_data = []
        for player in players:
            player_data = {
                "username": player.username,
                "rank": player.get_rank_display(),
                "score": str(player.score)
            }
            players_data.append(player_data)

        return JsonResponse({"players": players_data}, status=200)  # Success
    except ValueError:
        return JsonResponse({}, status=400)  # Bad Request
    except Exception:
        return JsonResponse({}, status=500)  # Internal Server Error


def handle_put_request(request):
    try:
        if "auth-token" not in request.headers:
            return JsonResponse({}, status=401)  # Unauthorized

        auth_token = request.headers["auth-token"]
        if auth_token[::-1] != auth_token:
            return JsonResponse({}, status=401)  # Unauthorized

        data = json.loads(request.body)
        player_id = data.get("player_id")
        username = data.get("username")
        score = float(data.get("score"))

        if not (username or player_id):
            return JsonResponse({}, status=400)
        if username:
            player = Player.objects.get(username=username)
        elif player_id:
            player = Player.objects.get(id=player_id)

        data = json.loads(request.body)
        player_id = data["player_id"]
        username = data.get("username")
        score = float(data.get("score"))

        if not (username or player_id):
            return JsonResponse({}, status=400)
        if username:
            player = Player.objects.get(username=username)
        elif player_id:
            player = Player.objects.get(id=player_id)

        validate_score(score)
        player.score = score
        player.save()
        update_ranks()

        return JsonResponse({}, status=200)  # OK

    except (KeyError, json.JSONDecodeError):
        return JsonResponse({}, status=400)  # Bad Request
    except Player.DoesNotExist:
        return JsonResponse({}, status=404)  # Not Found
    except Exception:
        return JsonResponse({}, status=500)  # Internal Server Error


def update_ranks():
    players = Player.objects.order_by('-score')

    if players:
        king_score = players[0].score
        tenth_of_king_score = king_score / 10

        for player in players:
            if player.score == king_score:
                player.rank = 'K'
            elif player.score < tenth_of_king_score:
                player.rank = 'N'
            elif player.score < king_score / 2:
                player.rank = 'I'
            else:
                player.rank = 'P'

        Player.objects.bulk_update(players, ['rank'])
