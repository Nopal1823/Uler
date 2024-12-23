import os
import random
import time

width, height = 20, 10
snake = [(5, 5)]
direction = (0, 1)
food = (random.randint(0, height - 1), random.randint(0, width - 1))
score = 0
game_over = False

def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(height):
        for x in range(width):
            if (y, x) == snake[0]:
                print("S", end="")
            elif (y, x) in snake[1:]:
                print("s", end="")
            elif (y, x) == food:
                print("F", end="")
            else:
                print(".", end="")
        print()
    print(f"Score: {score}")

def get_new_direction():
    global direction
    key = input("Move (W/A/S/D): ").lower()
    if key == 'w' and direction != (1, 0):
        direction = (-1, 0)
    elif key == 'a' and direction != (0, 1):
        direction = (0, -1)
    elif key == 's' and direction != (-1, 0):
        direction = (1, 0)
    elif key == 'd' and direction != (0, -1):
        direction = (0, 1)

while not game_over:
    draw_board()
    get_new_direction()

    head_y, head_x = snake[0]
    delta_y, delta_x = direction
    new_head = (head_y + delta_y, head_x + delta_x)

    if (new_head in snake) or (new_head[0] < 0 or new_head[0] >= height) or (new_head[1] < 0 or new_head[1] >= width):
        game_over = True
        print("Game Over!")
        break

    if new_head == food:
        score += 1
        food = (random.randint(0, height - 1), random.randint(0, width - 1))
    else:
        snake.pop()

    snake.insert(0, new_head)
    time.sleep(0.2)

if game_over:
    print(f"Your final score: {score}")
