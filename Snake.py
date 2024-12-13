import os
import random
import time

# Konfigurasi awal
width, height = 20, 10  # Ukuran area permainan (kolom x baris)
snake = [(5, 5)]  # Posisi awal ular
direction = (0, 1)  # Arah awal (bergerak ke kanan)
food = (random.randint(0, height - 1), random.randint(0, width - 1))  # Posisi makanan
score = 0  # Skor awal
game_over = False

# Fungsi untuk menggambar arena permainan
def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(height):
        for x in range(width):
            if (y, x) == snake[0]:  # Kepala ular
                print("S", end="")
            elif (y, x) in snake[1:]:  # Tubuh ular
                print("s", end="")
            elif (y, x) == food:  # Posisi makanan
                print("F", end="")
            else:
                print(".", end="")  # Area kosong
        print()
    print(f"Score: {score}")

# Fungsi untuk mengubah arah
def get_new_direction():
    global direction
    key = input("Move (W/A/S/D): ").lower()
    if key == 'w' and direction != (1, 0):  # Ke atas
        direction = (-1, 0)
    elif key == 'a' and direction != (0, 1):  # Ke kiri
        direction = (0, -1)
    elif key == 's' and direction != (-1, 0):  # Ke bawah
        direction = (1, 0)
    elif key == 'd' and direction != (0, -1):  # Ke kanan
        direction = (0, 1)

# Game loop utama
while not game_over:
    draw_board()
    get_new_direction()

    # Hitung posisi kepala baru
    head_y, head_x = snake[0]
    delta_y, delta_x = direction
    new_head = (head_y + delta_y, head_x + delta_x)

    # Periksa kondisi permainan
    if (new_head in snake) or (new_head[0] < 0 or new_head[0] >= height) or (new_head[1] < 0 or new_head[1] >= width):
        game_over = True
        print("Game Over!")
        break

    # Periksa apakah makanan dimakan
    if new_head == food:
        score += 1
        food = (random.randint(0, height - 1), random.randint(0, width - 1))  # Tempatkan makanan baru
    else:
        snake.pop()  # Hapus ekor ular

    # Tambahkan kepala baru ke ular
    snake.insert(0, new_head)

    time.sleep(0.2)  # Delay untuk mengontrol kecepatan permainan

if game_over:
    print(f"Your final score: {score}")
