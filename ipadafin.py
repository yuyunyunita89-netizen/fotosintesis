def teka_teki_alam():
    print("Selamat datang di Teka-Teki Alam!")
    score = 0
    
    # Daftar pertanyaan dan jawaban
    pertanyaan = [
        {
            "tanya": "Apa nama proses di mana tumbuhan membuat makanan menggunakan sinar matahari?",
            "jawab": "fotosintesis"
        },
        {
            "tanya": "Binatang apa yang dikenal sebagai raja hutan?",
            "jawab": "singa"
        },
        {
            "tanya": "Apa nama sungai terpanjang di dunia?",
            "jawab": "nil"
        },
        {
            "tanya": "Apa nama gas yang kita hirup untuk bernapas?",
            "jawab": "oksigen"
        },
        {
            "tanya": "Apa nama lapisan bumi tempat kita tinggal?",
            "jawab": "kerak bumi"
        }
    ]
    
    for i, item in enumerate(pertanyaan, 1):
        jawaban_user = input(f"{i}. {item['tanya']} ").strip().lower()
        if jawaban_user == item['jawab']:
            print("Benar!\n")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah '{item['jawab']}'.\n")
    
    print(f"Skor kamu: {score} dari {len(pertanyaan)}")
    if score == len(pertanyaan):
        print("Hebat! Kamu jago banget tentang alam!")
    elif score >= len(pertanyaan) // 2:
        print("Bagus! Kamu tahu cukup banyak tentang alam.")
    else:
        print("Jangan menyerah, coba lagi ya!")

if __name__ == "__main__":
    teka_teki_alam()