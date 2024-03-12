from turtle import Screen
from spaceship import SpaceShip
from bullets import Bullet
from score import Score
from invaders import Invader
import time
import random

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Space Invaders!")
# below method hide the tracer
my_screen.tracer(0)
my_screen.register_shape('gifs\spaceship.gif')
my_screen.register_shape('gifs\invader.gif')

# Make invaders
all_invaders = []
y = 150

for i in range(3):
    x = 120
    for j in range(6):
        x -= 50
        invader = Invader(x, y)
        all_invaders.append(invader)
    y -= 25

# Make random invader's bullet
all_bullets = []


def random_bullet():
    random_chance = random.randint(1, 150)
    if random_chance == 1:
        random_invader = random.choice(all_invaders)
        invader_bullet = Bullet(x=random_invader.xcor(), y=random_invader.ycor(), head=270)
        all_bullets.append(invader_bullet)


spaceship = SpaceShip()
# invader = Invaders(-240, 160)
scoreboard = Score()


# Initialise game
my_screen.update()
my_screen.listen()
my_screen.onkey(spaceship.move_left, "Left")
my_screen.onkey(spaceship.move_right, "Right")
my_screen.onkey(spaceship.fire(), "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.0001)
    my_screen.update()
    if len(all_invaders) <= 0:
        scoreboard.result(message="Win")
        game_is_on = False
    if scoreboard.lives <= 0:
        scoreboard.result(message="Lives")
        game_is_on = False

    # Invaders move
    for invader in all_invaders:
        invader.move_invader()

    # Invader's bullet
    random_bullet()
    for bullet in all_bullets:
        bullet.bullet_move()
        bullet.detect_lower_limit()

        # detect collision of invader's bullet with spaceship
        if spaceship.distance(bullet) < 20:
            scoreboard.remove_life()
            bullet.disappear()
            spaceship.reposition()
            continue

    # player bullet actions
    spaceship.player_bullet.bullet_move()

    # detect collision of invaders with player's bullet
    for invader in all_invaders:
        if spaceship.player_bullet.distance(invader) < 10:
            invader.delete_invader()
            spaceship.player_bullet.disappear()
            scoreboard.score += 20
            scoreboard.update_score()
            break

    # detect collision of player's bullet with invader's bullet
    for bullet in all_bullets:
        if spaceship.player_bullet.distance(bullet) < 5:
            bullet.disappear()
            spaceship.player_bullet.disappear()
            scoreboard.score += 5
            scoreboard.update_score()
            break

my_screen.mainloop()
my_screen.exitonclick()
