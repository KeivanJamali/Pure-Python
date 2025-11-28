import math
import turtle
import os
import subprocess
import threading
import atexit
import random
import time
from pathlib import Path

# Global variable to store music process
music_process = None

def heart_a(k):
    return 15 * math.sin(k) ** 3

def heart_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

def draw_mini_heart(t, x, y, size, color="pink"):
    """Draw a small heart at position (x, y)"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(size * 2.2)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.02)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.02)
    t.forward(size * 2.2)
    t.end_fill()
    t.setheading(0)

def write_romantic_message(message, x, y, font_size=30):
    """Write a message letter by letter with animation"""
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.color("white")
    
    displayed = ""
    for char in message:
        displayed += char
        writer.clear()
        writer.write(displayed, align="center", font=("Georgia", font_size, "italic"))
        time.sleep(0.08)
    
    return writer

def draw_heart_shape(t, size):
    """Draw a heart shape using turtle at current position"""
    t.begin_fill()
    t.left(140)
    t.forward(size * 1.5)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.013)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.013)
    t.forward(size * 1.5)
    t.end_fill()
    t.setheading(0)

def create_floating_hearts(num_hearts=12):
    """Create floating hearts around the screen"""
    hearts = []
    colors = ["pink", "hotpink", "lightpink", "deeppink", "crimson", "salmon", "red"]
    
    for _ in range(num_hearts):
        h = turtle.Turtle()
        h.hideturtle()
        h.speed(0)
        h.penup()
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(180, 320)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        h.goto(x, y)
        color = random.choice(colors)
        h.color(color, color)  # Set both pen and fill color
        size = random.uniform(8, 18)
        # Store velocity and size for animation
        h.dx = random.uniform(-3, 3)
        h.dy = random.uniform(1, 4)  # Float upward
        h.heart_size = size
        hearts.append(h)
    
    return hearts

def animate_floating_hearts(hearts, duration=20):
    """Animate hearts floating upward"""
    screen = turtle.Screen()
    screen.tracer(0)  # Turn off auto-update for smooth animation
    
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for h in hearts:
            h.clear()
            
            # Draw the heart at current position
            h.pendown()
            draw_heart_shape(h, h.heart_size)
            h.penup()
            
            # Update position - float upward with gentle sway
            new_x = h.xcor() + h.dx + random.uniform(-1, 1)
            new_y = h.ycor() + h.dy
            
            # Reset to bottom if goes too high
            if new_y > 350:
                new_y = -350
                new_x = random.uniform(-350, 350)
            
            # Keep within horizontal bounds with bounce
            if new_x > 380 or new_x < -380:
                h.dx = -h.dx
                new_x = max(-380, min(380, new_x))
            
            h.goto(new_x, new_y)
        
        screen.update()
        time.sleep(0.05)
    
    screen.tracer(1)  # Turn auto-update back on

def draw_small_heart(t, x, y, size, color="red"):
    """Draw a small decorative heart at position (x, y)"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)
    t.forward(size)
    t.end_fill()
    t.setheading(0)
    t.penup()

def draw_star(t, x, y, size, color="gold"):
    """Draw a small star at position (x, y)"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(color, color)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()

def draw_rose(t, x, y, size=1):
    """Draw a beautiful rose"""
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    
    # Draw stem
    t.color("darkgreen")
    t.pensize(3 * size)
    t.pendown()
    t.forward(80 * size)
    t.penup()
    
    # Draw leaves
    t.goto(x, y + 30 * size)
    t.setheading(45)
    t.color("green", "green")
    t.pendown()
    t.begin_fill()
    t.circle(15 * size, 150)
    t.left(120)
    t.circle(15 * size, 150)
    t.end_fill()
    t.penup()
    
    t.goto(x, y + 50 * size)
    t.setheading(135)
    t.pendown()
    t.begin_fill()
    t.circle(-15 * size, 150)
    t.right(120)
    t.circle(-15 * size, 150)
    t.end_fill()
    t.penup()
    
    # Draw rose petals (spiral of circles)
    t.goto(x, y + 85 * size)
    colors = ["#8B0000", "#B22222", "#DC143C", "#FF0000", "#FF6B6B"]
    
    for i, color in enumerate(colors):
        t.color(color, color)
        petal_size = (20 - i * 3) * size
        for angle in range(0, 360, 45):
            t.penup()
            t.goto(x + (10 - i * 2) * size * math.cos(math.radians(angle)), 
                   y + 85 * size + (10 - i * 2) * size * math.sin(math.radians(angle)))
            t.setheading(angle)
            t.pendown()
            t.begin_fill()
            t.circle(petal_size, 180)
            t.end_fill()
    
    t.penup()
    t.pensize(1)

def draw_intertwined_hearts(t, x, y, size=1):
    """Draw two hearts intertwined - symbolizing two becoming one"""
    # First heart (left, pink)
    t.penup()
    t.goto(x - 30 * size, y)
    t.setheading(0)
    t.color("hotpink", "hotpink")
    t.pensize(3)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(50 * size)
    for _ in range(200):
        t.right(1)
        t.forward(0.4 * size)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(0.4 * size)
    for _ in range(100):
        t.forward(0.5 * size)
    t.end_fill()
    t.penup()
    t.setheading(0)
    
    # Second heart (right, red) - slightly overlapping
    t.goto(x + 30 * size, y)
    t.color("red", "red")
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(50 * size)
    for _ in range(200):
        t.right(1)
        t.forward(0.4 * size)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(0.4 * size)
    for _ in range(100):
        t.forward(0.5 * size)
    t.end_fill()
    t.penup()
    t.setheading(0)
    t.pensize(1)

def draw_shooting_star(t, start_x, start_y, length, angle):
    """Draw a shooting star with trail"""
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(angle)
    
    # Draw trail (fading line)
    colors = ["white", "#FFFACD", "#FFE4B5", "#FFDAB9", "#FFE4E1"]
    for i, color in enumerate(colors):
        t.color(color)
        t.pensize(5 - i)
        t.pendown()
        t.forward(length / 5)
    
    # Draw star at the end
    t.color("white", "white")
    t.begin_fill()
    for _ in range(5):
        t.forward(8)
        t.right(144)
    t.end_fill()
    t.penup()
    t.pensize(1)

def draw_couple_silhouette(t, x, y, size=1):
    """Draw a simple romantic couple silhouette"""
    t.penup()
    t.color("#4A0000", "#4A0000")
    
    # Person 1 (left) - head
    t.goto(x - 25 * size, y + 40 * size)
    t.pendown()
    t.begin_fill()
    t.circle(12 * size)
    t.end_fill()
    
    # Person 1 - body
    t.penup()
    t.goto(x - 25 * size, y + 28 * size)
    t.setheading(-90)
    t.pensize(8 * size)
    t.pendown()
    t.forward(45 * size)
    
    # Person 2 (right) - head
    t.penup()
    t.goto(x + 25 * size, y + 35 * size)
    t.pendown()
    t.begin_fill()
    t.circle(11 * size)
    t.end_fill()
    
    # Person 2 - body
    t.penup()
    t.goto(x + 25 * size, y + 24 * size)
    t.setheading(-90)
    t.pensize(7 * size)
    t.pendown()
    t.forward(40 * size)
    
    # Arms reaching toward each other (holding hands)
    t.penup()
    t.goto(x - 25 * size, y + 10 * size)
    t.setheading(30)
    t.pensize(4 * size)
    t.pendown()
    t.forward(30 * size)
    
    t.penup()
    t.goto(x + 25 * size, y + 8 * size)
    t.setheading(150)
    t.pendown()
    t.forward(30 * size)
    
    t.penup()
    t.pensize(1)
    t.setheading(0)

def draw_infinity_heart(t, x, y, size=1):
    """Draw an infinity symbol made with a heart feel - eternal love"""
    t.penup()
    t.goto(x, y)
    t.color("deeppink")
    t.pensize(4)
    t.pendown()
    
    # Draw infinity symbol with curves
    for _ in range(2):
        t.circle(30 * size, 180)
        t.circle(-30 * size, 180)
    
    t.penup()
    t.pensize(1)

def animate_sparkles(duration=5):
    """Create sparkle animation across the screen"""
    screen = turtle.Screen()
    screen.tracer(0)
    sparkles = []
    
    for _ in range(20):
        s = turtle.Turtle()
        s.hideturtle()
        s.speed(0)
        s.penup()
        sparkles.append(s)
    
    start_time = time.time()
    while time.time() - start_time < duration:
        for s in sparkles:
            s.clear()
            x = random.randint(-350, 350)
            y = random.randint(-250, 250)
            s.goto(x, y)
            s.color(random.choice(["white", "gold", "lightyellow", "pink"]))
            size = random.randint(3, 8)
            s.pendown()
            s.begin_fill()
            for _ in range(5):
                s.forward(size)
                s.right(144)
            s.end_fill()
            s.penup()
        screen.update()
        time.sleep(0.1)
    
    for s in sparkles:
        s.clear()
    screen.tracer(1)

def draw_holding_hands(t, x, y, size=1):
    """Draw two hands holding each other in a lovely way - outline only"""
    t.speed(2)  # Slow down for dramatic effect
    t.pensize(3)
    
    # === LEFT HAND (reaching from left) ===
    t.color("white")
    
    # Left arm/wrist
    t.penup()
    t.goto(x - 250 * size, y - 30 * size)
    t.setheading(0)
    t.pendown()
    t.goto(x - 150 * size, y - 20 * size)
    
    # Left palm bottom
    t.goto(x - 100 * size, y - 25 * size)
    t.goto(x - 50 * size, y - 30 * size)
    
    # Left pinky
    t.goto(x - 40 * size, y - 20 * size)
    t.goto(x - 30 * size, y + 20 * size)
    t.goto(x - 20 * size, y + 35 * size)  # Pinky tip
    t.goto(x - 25 * size, y + 20 * size)
    
    # Left ring finger
    t.goto(x - 15 * size, y + 25 * size)
    t.goto(x - 5 * size, y + 55 * size)  # Ring tip
    t.goto(x + 5 * size, y + 25 * size)
    
    # Left middle finger
    t.goto(x + 10 * size, y + 30 * size)
    t.goto(x + 15 * size, y + 70 * size)  # Middle tip
    t.goto(x + 25 * size, y + 30 * size)
    
    # Left index finger
    t.goto(x + 30 * size, y + 25 * size)
    t.goto(x + 35 * size, y + 60 * size)  # Index tip
    t.goto(x + 45 * size, y + 20 * size)
    
    # Left thumb (going over the right hand)
    t.goto(x + 55 * size, y + 15 * size)
    t.goto(x + 80 * size, y + 40 * size)  # Thumb tip
    t.goto(x + 90 * size, y + 25 * size)
    t.goto(x + 85 * size, y + 5 * size)
    
    # Connect back along top of left palm
    t.goto(x + 50 * size, y + 5 * size)
    t.goto(x - 50 * size, y + 15 * size)
    t.goto(x - 150 * size, y + 20 * size)
    t.goto(x - 250 * size, y + 30 * size)
    
    t.penup()
    
    # === RIGHT HAND (reaching from right, fingers interlocking) ===
    t.color("pink")
    
    # Right arm/wrist
    t.goto(x + 250 * size, y + 30 * size)
    t.setheading(180)
    t.pendown()
    t.goto(x + 150 * size, y + 20 * size)
    
    # Right palm top
    t.goto(x + 100 * size, y + 25 * size)
    t.goto(x + 60 * size, y + 20 * size)
    
    # Right thumb (wrapping under)
    t.goto(x + 50 * size, y + 10 * size)
    t.goto(x + 30 * size, y - 20 * size)
    t.goto(x + 15 * size, y - 45 * size)  # Thumb tip
    t.goto(x + 25 * size, y - 25 * size)
    t.goto(x + 35 * size, y - 10 * size)
    
    # Right index (between left middle and ring)
    t.goto(x + 20 * size, y - 5 * size)
    t.goto(x + 5 * size, y - 40 * size)  # Index tip
    t.goto(x - 10 * size, y - 5 * size)
    
    # Right middle finger
    t.goto(x - 15 * size, y - 10 * size)
    t.goto(x - 25 * size, y - 50 * size)  # Middle tip
    t.goto(x - 40 * size, y - 10 * size)
    
    # Right ring finger
    t.goto(x - 45 * size, y - 15 * size)
    t.goto(x - 55 * size, y - 45 * size)  # Ring tip
    t.goto(x - 65 * size, y - 20 * size)
    
    # Right pinky
    t.goto(x - 70 * size, y - 25 * size)
    t.goto(x - 80 * size, y - 50 * size)  # Pinky tip
    t.goto(x - 90 * size, y - 30 * size)
    
    # Right palm bottom
    t.goto(x - 70 * size, y - 35 * size)
    t.goto(x + 50 * size, y - 35 * size)
    t.goto(x + 150 * size, y - 20 * size)
    t.goto(x + 250 * size, y - 30 * size)
    
    t.penup()
    t.pensize(1)

def heartbeat_animation(times=5):
    """Make the screen pulse like a heartbeat"""
    screen = turtle.Screen()
    colors = ["black", "#1a0000", "#2a0000", "#1a0000", "black"]
    
    for _ in range(times):
        for color in colors:
            screen.bgcolor(color)
            time.sleep(0.1)
        time.sleep(0.3)

def surprise_animation():
    """The surprise that happens after the heart is drawn!"""
    screen = turtle.Screen()
    
    # Clear the screen with a fade effect
    turtle.clear()
    time.sleep(0.5)
    
    # Heartbeat effect
    heartbeat_animation(3)
    
    # === SCENE 1: Romantic message with sparkles ===
    animate_sparkles(2)
    
    message = "I Love You Forever!"
    writer = write_romantic_message(message, 0, 50, 40)
    
    # Draw one decorative heart below the message
    decorator = turtle.Turtle()
    decorator.hideturtle()
    decorator.speed(0)
    draw_small_heart(decorator, 0, -30, 20, "hotpink")
    time.sleep(2)
    
    # Transition heartbeat
    writer.clear()
    decorator.clear()
    heartbeat_animation(2)
    
    # === SCENE 2: Intertwined hearts - two becoming one ===
    screen.bgcolor("black")
    
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    
    # Draw shooting stars first
    draw_shooting_star(drawer, -300, 200, 80, -30)
    draw_shooting_star(drawer, 200, 250, 100, -150)
    draw_shooting_star(drawer, -100, 280, 60, -45)
    
    time.sleep(0.5)
    draw_intertwined_hearts(drawer, 0, 50, 1.5)
    
    msg_turtle = turtle.Turtle()
    msg_turtle.hideturtle()
    msg_turtle.penup()
    msg_turtle.goto(0, -80)
    msg_turtle.color("white")
    msg_turtle.write("Two Hearts, One Love", align="center", font=("Georgia", 25, "italic"))
    
    time.sleep(3)
    
    # Transition heartbeat
    drawer.clear()
    msg_turtle.clear()
    heartbeat_animation(2)
    
    # === SCENE 3: Beautiful Rose ===
    draw_rose(drawer, 0, -100, 1.5)
    
    msg_turtle.goto(0, -200)
    msg_turtle.color("pink")
    msg_turtle.write("A Rose For My Love", align="center", font=("Georgia", 25, "italic"))
    
    time.sleep(3)
    
    # Transition heartbeat
    drawer.clear()
    msg_turtle.clear()
    heartbeat_animation(2)
    
    # === SCENE 4: Couple silhouette with infinity ===
    # Draw a big heart outline in background
    drawer.penup()
    drawer.color("#2a0000")
    drawer.pensize(3)
    for i in range(628):
        k = i / 100
        x = heart_a(k) * 15
        y = heart_b(k) * 15 - 20
        if i == 0:
            drawer.goto(x, y)
            drawer.pendown()
        else:
            drawer.goto(x, y)
    drawer.penup()
    drawer.pensize(1)
    
    msg_turtle.goto(0, -180)
    msg_turtle.color("hotpink")
    msg_turtle.write("Together Forever", align="center", font=("Georgia", 25, "italic"))
    
    time.sleep(3)
    
    # Transition heartbeat
    drawer.clear()
    msg_turtle.clear()
    heartbeat_animation(2)
    
    # === SCENE 5: Grand finale with floating hearts ===
    # Final messages
    msg_turtle.goto(0, 80)
    msg_turtle.color("white")
    msg_turtle.write("You are my everything", align="center", font=("Georgia", 30, "italic"))
    
    msg_turtle.goto(0, 20)
    msg_turtle.color("pink")
    msg_turtle.write("My heart beats for you", align="center", font=("Georgia", 25, "italic"))
    
    # Draw stars around
    star_drawer = turtle.Turtle()
    star_drawer.hideturtle()
    star_drawer.speed(0)
    for _ in range(15):
        x = random.randint(-350, 350)
        y = random.randint(120, 280)
        draw_star(star_drawer, x, y, random.randint(5, 12), random.choice(["gold", "white", "lightyellow"]))
    
    # Create and animate floating hearts
    hearts = create_floating_hearts(15)
    animate_floating_hearts(hearts, duration=16)
    
    # Clean up floating hearts
    for h in hearts:
        h.clear()
    
    # === FINAL: Just a gentle heartbeat and peaceful ending ===
    msg_turtle.clear()
    star_drawer.clear()
    
    heartbeat_animation(2)
    
    # Final romantic message
    final_msg = turtle.Turtle()
    final_msg.hideturtle()
    final_msg.penup()
    final_msg.goto(0, 0)
    final_msg.color("white")
    final_msg.write("Forever Yours", align="center", font=("Georgia", 35, "italic"))

def stop_music():
    """Stop the music process when program exits"""
    global music_process
    if music_process:
        try:
            music_process.terminate()
            music_process.wait(timeout=2)
        except:
            music_process.kill()

def play_music(music_file, start_time=0):
    """Play music in background using system audio players starting at specified time"""
    global music_process
    
    if not os.path.exists(music_file):
        print(f"Music file '{music_file}' not found. Drawing heart without music.")
        return
    
    try:
        # For Linux - with start time support
        if os.system('which mpg123 > /dev/null 2>&1') == 0:
            music_process = subprocess.Popen(['mpg123', '-q', '--loop', '-1', '-k', str(start_time), music_file])
        elif os.system('which ffplay > /dev/null 2>&1') == 0:
            music_process = subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-loop', '0', '-ss', str(start_time), music_file], 
                           stderr=subprocess.DEVNULL)
        elif os.system('which cvlc > /dev/null 2>&1') == 0:
            music_process = subprocess.Popen(['cvlc', '--loop', '--quiet', '--start-time', str(start_time), music_file])
        else:
            print("No audio player found. Please install mpg123, ffplay, or vlc.")
    except Exception as e:
        print(f"Could not play music: {e}")

atexit.register(stop_music)

music_file = Path(r"/mnt/Data1/Python_Projects/Pure-Python/P5/10-Romantic/song.mp3")
start_at_seconds = 115  # Start at 1:55 (1 minute 55 seconds)
music_thread = threading.Thread(target=play_music, args=(music_file, start_at_seconds), daemon=True)
music_thread.start()

turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

###############################################################################
for i in range(800):
    turtle.goto(heart_a(i)*20, heart_b(i)*20)
    turtle.color("red")
    turtle.goto(0, 0)

###############################################################################
time.sleep(1)
surprise_animation()
    
try:
    turtle.done()
finally:
    stop_music()