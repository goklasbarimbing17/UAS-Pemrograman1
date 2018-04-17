print "1. Nilai Mahasiswa"
print "2. Nilai Random"
print "3. List Append"
print "4. Tuple"
print "5. Dictionary"
print "6. Kalkulator Function"
pilih=input("Tentukan Pilihan (1/2/3/4/5/6) :")
import Goklas.a
pilih=input("Tentukan Pilihan (1/2/3/4/5/6) :")
import Goklas.b
import Goklas.c
import Goklas.d
import Goklas.e
import Goklas.f

if pilih == 1:
    print Goklas.mhs()
elif pilih ==2:
    print Goklas.b.random()
elif pilih ==3:
    print Goklas.c.lisst()
elif pilih ==4:
    print Goklas.d.tup()
elif pilih ==5:
    print Goklas.e.dic()
elif pilih ==6:
    print Goklas.f.kal()

else:
    print"Coba memilih dengan benar"
