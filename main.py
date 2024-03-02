meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit kettidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif"
            }
word = input("Ketik kata yang tidak kamu mengerti")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kata tidak teregistrasi")
