#girilen sayıyı ters çeviren program.

sayi = int(input("sayı girin:"))
ters = 0
while sayi > 0:
    tersSayi = sayi % 10
    ters = ters * 10 + tersSayi
    sayi = sayi // 10

print(ters)