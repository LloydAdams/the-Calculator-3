while True:
    #Girilen Sayıların Listeye Eklenmesi ve İşlemin Yapılıp Yapılmadığına Dair Değerlerin Döndürülmesi
    def SayıKontrol():
        if islem=="toplama": 
            for i in range(adet):
                sayi=input(f"{i+1}. Sayıyı Giriniz: ")
                liste.append(sayi)
            Toplama(liste,adet)
            İşlemDoğruMu=True
            
        elif islem=="çıkarma":
            for i in range(adet):
                sayi=input(f"{i+1}. Sayıyı Giriniz: ")
                liste.append(sayi)
            Çıkarma(liste,adet)
            İşlemDoğruMu=True
            
        elif islem=="çarpma":
            for i in range(adet):
                sayi=input(f"{i+1}. Sayıyı Giriniz: ")
                liste.append(sayi)
            Çarpma(liste,adet)
            İşlemDoğruMu=True
            
        elif islem=="bölme":
            for i in range(adet):
                sayi=input(f"{i+1}. Sayıyı Giriniz: ")
                liste.append(sayi)
            Bölme(liste,adet)
            İşlemDoğruMu=True
            
        else:
            print("Yanlış Değer Girdiniz. Lütfen Tekrar Deneyiniz.\n")
            İşlemDoğruMu=False

        return İşlemDoğruMu
            

    #4 İşlemlerin Yapıldığı ve Doğru Sayı Değerlerinin Girildiğini Kontrol Eden Fonksiyonlar
    def Toplama(liste,adet):
        global toplam
        for a in range(adet):

            try:
                toplam+=float(liste[a])
            except ValueError:
                print("Lütfen Geçerli Sayı Değerleri Giriniz\n")
                SayıKontrol()
        print("İşlemin Sonucu: ",toplam)

    def Çıkarma(liste,adet):
        global fark
        fark=float(liste[0])
        for a in range(1,adet):           
            try:
                fark-=float(liste[a])
            except ValueError:
                print("Lütfen Geçerli Bir Sayı Giriniz\n")
                SayıKontrol() 
        print("İşlemin Sonucu: ",fark)

    def Çarpma(liste,adet):
        global çarpım
        for a in range(adet):
            try:
                çarpım*=float(liste[a])
            except ValueError:
                print("Lütfen Geçerli Bir Sayı Giriniz\n")
                SayıKontrol()
        print("İşlemin Sonucu: ",çarpım)

    def Bölme(liste,adet):
        global bölüm
        bölüm=float(liste[0])
        for a in range(1,adet):
            try:
                bölüm/=float(liste[a])
            except ValueError:
                print("Lütfen Geçerli Bir Sayı Giriniz\n")
                SayıKontrol()
            except ZeroDivisionError:
                print("İşlemin Sonucu: Reel Sayılar Kümesinde Tanımsız")
                return
        print("İşlemin Sonucu: ",bölüm)
    
    
    toplam=0
    çarpım=1
    #Kullanıcıdan Değer Alma
    try:
        global adet
        adet=int(input("İşlem Yapılacak Sayı Adedini Giriniz: "))
        if adet<=0:
            raise ValueError
    except ValueError:
        print("Yanlış Değer Girdiniz. Lütfen Tekrar Deneyiniz.\n")
        continue
    global liste
    liste=[]
    global islem
    islem=input("Yapılacak İşlemi Giriniz [toplama/çıkarma/çarpma/bölme]: ").lower()

    islemkontrol=SayıKontrol()
    if islemkontrol:
        break
    else:
        continue

    
    







