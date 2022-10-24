print("""""
***********************
Hesap Makinesi Programinesi Programina Hosgeldiniz

Yapilabilcek islemler:

1.Toplama Islemi

2.Cikartma Islemi

3.Carpma Islemi

4.Bolme Islemi

Yapmak istediginiz islem numarasini girip, isleminizi yapabilirsiniz.

**********************
""")

a = int(input("Birinci sayi:"))
b = int(input("Ikinci sayi:"))

islem = raw_input("yapmak istediginiz islemin numarasini giriniz:")

if islem == "1":
    print("{} ile {} in toplami {} dir\n Yine Bekleriz".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} in farki {} dir\n Yine Bekleriz".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} nin carpimi {} dir\n Yine Bekleriz".format(a,b,a*b))
elif islem == "4":
    print("{} ile {} nin birbirine bolumu {}\n Yine Bekleriz".format(a,b,a/b))
else :
    print ("Gecersiz islem, lutfen belirtilen islem numaralarindan birini giriniz!")
