import random
import os

tekateki = ["Semakin kita berpaling, semakin dia menjauh… Apakah itu?", "Hewan apa yang namanya hanya ada 2 huruf?", "Apa yang berada di antara langit dan bumi?", "Bila diikat, dia akan berjalan. Bila ikatannya dibuka, maka dia akan berhenti. Siapakah itu?", "Apa yang memiliki gigi tetapi tidak bisa menggigit?", "Apa yang tidak punya jari tapi bisa menunjuk?", "Apa yang bergerak tanpa berhenti tetapi tidak pernah pergi ke mana-mana?", "Ditutup jadi tongkat, dibuka jadi tenda, apakah itu?", "Kalau sedang sendiri, kakinya ada empat, kalau berdua kakinya jadi ada delapan, siapakah aku?", "Apa yang selalu bergerak, tapi tidak pernah lelah?"]
jawaban = ["telinga", "u dan g", "dan", "sepatu", "sisir", "kompas", "jam dinding", "payung", "kursi", "waktu"]
acak_angka = random.randint(0, 3)

dead = 0
tebakan_limit = 5

while tebakan_limit >= dead:  
    print('\n"' + tekateki[acak_angka] + '"\n')
    jawab = input("Kesempatan menebak sisa: " + str(tebakan_limit) + "\nJawabanmu: ")
    jawab = jawab.lower()
    if tebakan_limit == 0:
        os.system("clear")
        print("Yahhh kesempatanmu habis, lain kali mikir lebih keras ya bego! (｡•̀ ⤙ •́ ｡ꐦ) !!!")  
        break 
    elif jawab != jawaban[acak_angka]:
        os.system("clear")
        tebakan_limit -= 1  
        print("\nSalah! ayo mikir lebih keras! (ᵕ—ᴗ—)\n" )
    elif jawab == jawaban[acak_angka]:
        os.system("clear")
        print("Selamat! kamu benar! jawabannya: " + jawaban[acak_angka] + " ૮ ˶ᵔ ᵕ ᵔ˶ ა")
        break