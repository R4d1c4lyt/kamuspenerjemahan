import time
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "BRB": "Memberitahu bahwa anda akan pergi sebentar",
            "XD": "Suatu teks yang menunjukkan emoji ketawa",
            "WHAT": "Bisa sebagai pemberi tahu bahwa anda terkejut atau bingung",
            "EWW": "Merasa jijik / tidak nyaman"
            }

print("Halo! Selamat datang ke dalam dictionary tentang kata - kata meme!")
time.sleep(1)
print("Anda dapat mencari 5 kata meme dari dictionary ini.")
time.sleep(1)
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word in meme_dict.keys():
        print("Makna kata",word,"adalah",meme_dict[word])
        print(" ")
    else:
        print('kata tidak ditemukan...')
        print(" ")
  
print("Terima kasih sudah menggunakan dictionary ini tentang kata - kata meme!")
