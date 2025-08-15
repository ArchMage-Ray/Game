import random
import os

# Games: Teka-teki. Ini adalah game dimana anda harus menebak jawaban dari sebuah teka-teki yang sudah disediakan, 
# disini anda punya 5 kali kesempatan menebak.
# Jika anda gagal menebak jawabannya, maka anda akan kalah.

# Total: 10
tekateki = [
    "Semakin kita berpaling, semakin dia menjauh… Apakah itu?", 
    "Hewan apa yang namanya hanya ada 2 huruf?",
    "Apa yang berada di antara langit dan bumi?",
    "Bila diikat, dia akan berjalan. Bila ikatannya dibuka, maka dia akan berhenti. Siapakah itu?",
    "Apa yang memiliki gigi tetapi tidak bisa menggigit?", 
    "Apa yang tidak punya jari tapi bisa menunjuk?", 
    "Apa yang bergerak tanpa berhenti tetapi tidak pernah pergi ke mana-mana?", 
    "Ditutup jadi tongkat, dibuka jadi tenda, apakah itu?", 
    "Kalau sedang sendiri, kakinya ada empat, kalau berdua kakinya jadi ada delapan, siapakah aku?", 
    "Apa yang selalu bergerak, tapi tidak pernah lelah?"
    ]

# Total: 10
jawaban = [
    "telinga", 
    "u dan g", 
    "dan", 
    "sepatu", 
    "sisir", 
    "kompas", 
    "jam dinding", 
    "payung", 
    "kursi", 
    "waktu"
    ]

# Fungsi mengacak angka random 0-9 untuk array teka-teki.
acak_angka = random.randint(0, 9)

end = 0
tebakan_limit = 5

# Fungsi loop permainan #
# Ketika tebakan_limit(5) lebih dari sama dengan end(0) maka program akan
# mencetak hasil dari acak_angka dan disesuaikan dengan kolom pada array teka-teki.
while tebakan_limit >= end:  
    print('\n"' + tekateki[acak_angka] + '"\n')
    jawab = input("Kesempatan menebak sisa: " 
                  + str(tebakan_limit) 
                  + "\nJawabanmu: ")
    jawab = jawab.lower()
    # Ketika tebakan_limit mencapai angka 0, maka kesempatan telah habis,
    # layar CLI akan dibersihkan dan permainan berakhir.
    if tebakan_limit == 0:
        os.system("clear")
        print("Yahhh kesempatanmu habis, lain kali mikir"
              "lebih keras ya bego! (｡•̀ ⤙ •́ ｡ꐦ) !!!")  
        break 
    # Ketika user memberi input yang tidak sesuai dengan jawaban maka
    # layar CLI akan dibersihkan dan fungsi loop akan aktif dan  
    # mengurangi jumlah value tebakan_limit.
    elif jawab != jawaban[acak_angka]:
        os.system("clear")
        tebakan_limit -= 1  
        print("\nSalah! ayo mikir lebih keras! (ᵕ—ᴗ—)\n" )
    # Jika user memberi input yang identik dengan array jawaban yang sesuai maka,
    # permainan berakhir dengan kemenangan user.
    elif jawab == jawaban[acak_angka]:
        os.system("clear")
        print("Selamat! kamu benar! jawabannya: " 
              + jawaban[acak_angka]  
              + " ૮ ˶ᵔ ᵕ ᵔ˶ ა")
        break

# by @ArchMage-Ray
