Pokemon.py Discord Botu

Bu proje Python ile geliştirilmiş bir Discord botudur. Bot, kullanıcıların Pokémon benzeri karakterler seçerek savaşmalarına olanak tanır. Projenin amacı, nesne tabanlı programlama ve Discord bot yapımını uygulamalı olarak öğrenmek ve eğlenceli bir komut sistemi oluşturmaktır.

Botun Özellikleri

- Kullanıcılar karakter seçebilir (örnek: Pikachu, Charmander)
- Seçilen karakterle savaş başlatılabilir
- Kazanan karakter güce göre belirlenir
- Karakter sınıfı ve savaş mekanizması logic.py dosyasında tanımlanmıştır
- Bot, Discord sunucusunda mesajlara tepki verir

Dosya Yapısı

Main.py : Botun başlatıldığı ana dosya  
logic.py : Karakter sınıfı ve savaş sistemi  
.env : Gizli token bilgileri  
requirements.txt : Gerekli Python kütüphaneleri  
README.md : Proje açıklaması

Kurulum

1. Projeyi GitHub üzerinden klonlayın:  
   git clone https://github.com/ZaferDem/pokemon.py.git

2. Gerekli kütüphaneleri yükleyin:  
   pip install -r requirements.txt

3. .env adında bir dosya oluşturun ve içine kendi Discord bot tokenınızı yazın:  
   DISCORD_BOT=tokeniniz

4. Botu başlatmak için:  
   python Main.py

Komutlar

!choose [karakter_adı] : Bir karakter seçmenizi sağlar  
!battle : Seçilen karakterle savaş başlatır  

Proje Hakkında

Bu proje, sınıf yapısı, fonksiyonlar, Discord API ve komut sistemini kullanarak bir oyun mantığı kurmayı hedeflemiştir. Geliştirilmeye açıktır ve yeni özellikler kolayca eklenebilir.
