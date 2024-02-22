print("<"*3, "\t  Latihan\t", ">"*3)
print("Berikut akan tampil list dengan kondisi : " )
print("1. range(1,100)" )
print("2. value/item : genap ( i >= 10 dan i <= 20 )" )
print("3. value/item : ganjil ( i >= 90 dan i <= 100 )" )

data1 = [ i for i in range( 1, 100 ) if i % 2 == 0 and i >= 10 and i <= 20]
data2 = [ i for i in range( 1, 100 ) if i % 2 == 1 and i >= 90 and i <= 100]
print( f"data : { data1 + data2 }" )

print("<"*3, "\t  Latihan 2\t", ">"*3)
data = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
print( f"data : { data[2], data[0], data[3], data[4], data[5], data[6], data[1] }" )

print("<"*3, "\t  Latihan 3\t", ">"*3)
data = "IgNatIus"
hasil = []
for b in data:
    if b.isupper():
        hasil.append(b)
print( f" data : { hasil }")