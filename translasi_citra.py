import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shifty):
  """
  Fungsi untuk melakukan translasi citra.

  Args:
    image: Citra yang akan ditranslasi.
    shiftX: Jumlah pergeseran horizontal.
    shifty: Jumlah pergeseran vertikal.

  Returns:
    Citra yang telah ditranslasi.
  """
  imgTranslasi = np.roll(image, shift=shifty, axis=0)  # Geser vertikal
  imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)  # Geser horizontal
  # Mengisi bagian yang kosong dengan warna hitam (0)
  if shifty > 0:
    imgTranslasi[:shifty, :] = 200 # Bagian atas jika geser ke bawah
  elif shifty < 0:
    imgTranslasi[shifty:, :] = 100  # Bagian bawah jika geser ke atas
  if shiftX > 0:
    imgTranslasi[:, :shiftX] = 300  # Bagian kiri jika geser ke kanan
  elif shiftX < 0:
    imgTranslasi[:, shiftX:] = 400 # Bagian kanan jika geser ke kiri
  return imgTranslasi

# Memuat citra
image = img.imread("C:\\Users\\user\\\Downloads\\tiger.jpg.jpg")

# Melakukan translasi citra
shiftX = 50
shifty = -300
imgResult = Translasi(image, shiftX=shiftX, shifty=shifty)

# Menampilkan citra asli dan hasil translasi
plt.figure(figsize=(10, 10))
plt.subplot(2, 1, 1)
plt.imshow(image)
plt.title("Citra Asli")

plt.subplot(2, 1, 2)
plt.imshow(imgResult)
plt.title("Citra Translasi")

plt.tight_layout()
plt.show()