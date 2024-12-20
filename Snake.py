import os  #Import library os untuk membersihkan layar terminal.
import random  #Import library random untuk menghasilkan posisi makanan secara acak.

#Konfigurasi awal
width, height = 20, 10  #Ukuran area permainan (Kolom x Baris).
snake = [(5, 5)]  #Posisi awal ular (kepala ular).
direction = (0, 1)  #Arah awal ular bergerak ke kanan.
food = (random.randint(0, height - 1), random.randint(0, width - 1))  #Posisi awal makanan secara acak.
score = 0  #Skor awal permainan.
game_over = False  #Status permainan (False berarti permainan belum berakhir).

#Fungsi untuk menggambar arena permainan
def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')  #Membersihkan layar terminal agar tampilan diperbarui.
    for y in range(height):  #Looping baris dalam area permainan.
        for x in range(width):  #Looping kolom dalam area permainan.
            if (y, x) == snake[0]:  #Jika koordinat adalah kepala ular.
                print("S", end="")  #Cetak huruf 'S' untuk kepala ular.
            elif (y, x) in snake[1:]:  #Jika koordinat adalah tubuh ular.
                print("s", end="")  #Cetak huruf 's' untuk tubuh ular.
            elif (y, x) == food:  #Jika koordinat adalah posisi makanan.
                print("F", end="")  #Cetak huruf 'F' untuk makanan.
            else:  #Jika koordinat kosong.
                print(".", end="")  #Cetak titik '.' untuk area kosong.
        print()  #Ganti baris setelah mencetak satu baris penuh.
    print(f"Score: {score}")  #Cetak skor pemain saat ini.

#Fungsi untuk mengubah arah ular
def get_new_direction():
    global direction  #Gunakan variabel global untuk mengubah arah.
    key = input("Move (W/A/S/D): ").lower()  #Ambil input pemain (W/A/S/D) untuk arah pergerakan.
    if key == 'w' and direction != (1, 0):  #Jika tombol 'W' ditekan dan ular tidak bergerak ke bawah.
        direction = (-1, 0)  #Ubah arah ke atas.
    elif key == 'a' and direction != (0, 1):  #Jika tombol 'A' ditekan dan ular tidak bergerak ke kanan.
        direction = (0, -1)  #Ubah arah ke kiri.
    elif key == 's' and direction != (-1, 0):  #Jika tombol 'S' ditekan dan ular tidak bergerak ke atas.
        direction = (1, 0)  #Ubah arah ke bawah.
    elif key == 'd' and direction != (0, -1):  #Jika tombol 'D' ditekan dan ular tidak bergerak ke kiri.
        direction = (0, 1)  #Ubah arah ke kanan.

#Game loop utama
while not game_over:  #Loop utama berjalan selama permainan belum berakhir.
    draw_board()  #Panggil fungsi untuk menggambar arena permainan.
    get_new_direction()  #Panggil fungsi untuk mengambil input arah dari pemain.

    #Hitung posisi kepala baru
    head_y, head_x = snake[0]  #Ambil posisi kepala ular saat ini.
    delta_y, delta_x = direction  #Ambil arah pergerakan ular.
    new_head = (head_y + delta_y, head_x + delta_x)  #Hitung posisi kepala baru berdasarkan arah.

    #Periksa kondisi permainan
    if (new_head in snake) or (new_head[0] < 0 or new_head[0] >= height) or (new_head[1] < 0 or new_head[1] >= width):
        game_over = True  #Set status permainan menjadi berakhir.
        print("Game Over!")  #Cetak pesan game over.
        break  #Keluar dari loop utama.

    #Periksa apakah makanan dimakan
    if new_head == food:  #Jika posisi kepala baru sama dengan posisi makanan.
        score += 1  #Tambahkan skor pemain.
        food = (random.randint(0, height - 1), random.randint(0, width - 1))  #Tempatkan makanan baru secara acak.
    else:
        snake.pop()  #Hapus ekor ular jika makanan tidak dimakan.

    #Tambahkan kepala baru ke ular
    snake.insert(0, new_head)  #Tambahkan posisi kepala baru ke daftar ular.

if game_over:  #Jika permainan berakhir.
    print(f"Your final score: {score}")  #Cetak skor akhir pemain.
