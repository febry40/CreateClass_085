class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"PersegiPanjang, panjang{self.panjang} cm, dan lebar {self.lebar} cm "


def main():
    print("===Program Persegi Panjang===")

    try:
        panjang = float(input("Masukkan panjang"))
        lebar = float(input("Masukkan lebar"))
        if panjang <= 0 or lebar <= 0:
            print ("nilai panjang dan lebar harus positif")
            return
    
        persegi_panjang = PersegiPanjang(panjang, lebar)
   
        print (PersegiPanjang)
        print ("Keliling:", persegi_panjang.keliling())
        print ("Luas:", persegi_panjang.luas())

    except ValueError:
        print("nilai harus sesuai")

main()