import turtle

# Set up the screen
screen = turtle.Screen()

# Path gambar harus dalam format .gif
gambar = "Provinsi_indonesia_img.jpg"

# Tambahkan gambar sebagai bentuk turtle
screen.addshape(gambar)
turtle.shape(gambar)

# Fungsi untuk mendapatkan koordinat lokasi klik
def lokasi(x, y):
    print(x, y)

# Event listener untuk mendeteksi klik pada layar
turtle.onscreenclick(lokasi)

# Menutup layar saat diklik
screen.exitonclick()
