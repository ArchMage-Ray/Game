# Halo! selamat datang di Game versi bahasa Indonesia🎮️
Disini saya mendokumentasikan setiap game yang saya buat sendiri, dan kalian bisa mencobanya sendiri lho!

## Berikut game-game yang saya buat:
- ***Teka-Teki*** | `teka-teki.py`

---

## 🐱Tentang Game Teka-Teki🐱
`teka-teki.py` adalah program kuis teka-teki interaktif berbasis terminal yang menantang pemain untuk menebak jawaban dari kumpulan teka-teki lucu dan menarik. Pemain memiliki batas kesempatan menebak yang terbatas untuk setiap teka-teki. <br><br>
*Informasi Tambahan*:
- Program ini dibuat dengan bahasa pemograman *Python*.
- Masalah saat proses produksi: *"Bagaimana caranya untuk mengacak array A, tapi array A harus tetap bisa terhubung dengan array B dan harus sesuai dengan value yang saya inginkan"*. 

### Fitur Utama🧋
- Menyajikan teka-teki secara acak dari daftar pertanyaan.
- Membatasi jumlah tebakan agar permainan tetap menantang (default 5 kali).
- Memberikan feedback berupa pesan lucu dan memotivasi saat jawaban salah.
- Menggunakan sistem huruf kecil (lowercase) untuk memastikan jawaban tidak case-sensitive.
- Bersih dan minimalis, menggunakan `os.system("clear")` untuk membersihkan layar agar tampilan lebih rapi.

### Cara Kerja Program⚙️
**1.)** Program memilih angka acak sebagai indeks untuk teka-teki dari list tekateki. <br>
**2.)** Pemain diberi kesempatan 5 kali untuk menebak jawaban yang benar. <br>
**3.)** Setelah setiap tebakan, jika jawaban salah, kesempatan menurun dan layar dibersihkan. <br>
**4.)** Jika jawaban benar, program mengucapkan selamat dan keluar. <br>
**5.)** Jika kesempatan habis, program memberitahu pemain bahwa kesempatan telah berakhir dan keluar. 

### Struktur kode📜
**1.) List tekateki**: Menyimpan pertanyaan teka-teki. <br>
```
tekateki = ["Semakin kita berpaling, semakin dia menjauh… Apakah itu?", "Hewan apa yang namanya hanya ada 2 huruf?", "Apa yang berada di antara langit dan bumi?", "Bila diikat, dia akan berjalan. Bila ikatannya dibuka, maka dia akan berhenti. Siapakah itu?", "Apa yang memiliki gigi tetapi tidak bisa menggigit?", "Apa yang tidak punya jari tapi bisa menunjuk?", "Apa yang bergerak tanpa berhenti tetapi tidak pernah pergi ke mana-mana?", "Ditutup jadi tongkat, dibuka jadi tenda, apakah itu?", "Kalau sedang sendiri, kakinya ada empat, kalau berdua kakinya jadi ada delapan, siapakah aku?", "Apa yang selalu bergerak, tapi tidak pernah lelah?"]
```

<br>

**2.) List jawaban**: Menyimpan jawaban dan urutan yang sesuai dengan pertanyaan di tekateki (index matching). <br>
```
jawaban = ["telinga", "u dan g", "dan", "sepatu", "sisir", "kompas", "jam dinding", "payung", "kursi", "waktu"]
```

<br>

**3.) Variabel** `acak_angka`: Menentukan urutan teka-teki yang dipilih secara acak(0–9) dalam list teka-teki.
```
acak_angka = random.randint(0, 9)
```
> Beginilah cara saya mengatasi masalah "Bagaimana caranya untuk mengacak array A, tapi array A harus tetap bisa terhubung dengan array B dan harus sesuai dengan value yang saya inginkan" adalah **Dengan membuat 2 array tersebut memiliki urutan yang sama.**  <br>
> Sebagai contoh:
```
array_A = ["neko", "usagi", "sakana"]
              0       1         2
array_B = ["kucing', "kelinci", "ikan"]
              0         1          2

## Semisal hasil dari `acak_angka` adalah array_A[2] maka jika urutannya sama dengan array_B, tak peduli mau array_A diacak bagaimanapun juga hasilnya akan tetap terhubung dengan array_B karena yang diacak hanya array_A. ##
array_B[2] = array_B[2] 

```

<br>

**4.) Loop while**: Mengatur proses menebak dengan batas kesempatan. <br>
```
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
```

<br>

**5.) Fungsi** `os.system("clear")`: Membersihkan layar terminal agar user experience tetap nyaman.

## Catatan Tambahan
- Saat ini pemilihan teka-teki hanya antara indeks 0 sampai 9 (karena `random.randint(0,9)`), jadi hanya 10 teka-teki yang akan muncul. Tapi kamu bisa menambahkannya sendiri untuk `tekateki` dan `jawaban`.
- Kamu bisa memperluas program dengan menyesuaikan nilai `random.randint` agar mencakup seluruh daftar teka-teki.
- Penanganan input belum memeriksa typo atau sinonim, jadi jawaban harus tepat sesuai string di list jawaban.

**Contoh Tampilan**
```
"Semakin kita berpaling, semakin dia menjauh… Apakah itu?"

Kesempatan menebak sisa: 5  
Jawabanmu: 
```
