import math
import tabulate

BatasBawah, BatasAtas, banyakKelas, Fi = -1,-1, 0, []
while BatasBawah < 0 :
    BatasBawah = int(input("Batas Bawah Pertama : "))
while BatasAtas <= BatasBawah or BatasAtas < 0 :
    BatasAtas = int(input("Batas Atas Pertama : "))
while banyakKelas < 1 :
    banyakKelas = int(input("Masukkan berapakali banyaknya Kelas (>1) : "))
while len(Fi) != banyakKelas :
    Fi = list(map(int, input("Frekuensi : ").strip().split()))

#Menghitung panjang kelas
panjangKelas = BatasAtas - BatasBawah + 1
nilaiTengah = (BatasAtas + BatasBawah) / 2 #Float
sumFi = sum(Fi)

#BB, BA
dataKelompok = [[BatasBawah + (panjangKelas*(x)) for x in range (banyakKelas)],[BatasAtas + (panjangKelas*(x)) for x in range (banyakKelas)], [nilaiTengah + (panjangKelas*(x)) for x in range (banyakKelas)]] #BA BB NTengah
XiFi = [dataKelompok[2][i]*Fi[i] for i in range (banyakKelas)]
Mean = sum(XiFi)/sum(Fi) #Mean
#Mengolah Data
Xi_X_abs = [abs(dataKelompok[2][i]-Mean) for i in range (banyakKelas)]
Xi_X = [(dataKelompok[2][i]-Mean) for i in range (banyakKelas)]
Xi_X_sqr = [((dataKelompok[2][i]-Mean)**2) for i in range (banyakKelas)]
jmlXi_X_abs = sum(Xi_X_abs)
Data = []
for i in range (banyakKelas):
    pending = []
    pending.append(dataKelompok[0][i])
    pending.append(dataKelompok[1][i])
    pending.append(Fi[i])
    pending.append(dataKelompok[2][i])
    pending.append(XiFi[i])
    pending.append(Xi_X[i])
    pending.append(Xi_X_abs[i])
    pending.append(Xi_X_sqr[i])
    Data.append(pending)

print(tabulate.tabulate(Data, headers=["Batas Bawah", "Batas Atas", "Frekuensi", "Xi", "XiFi", "Xi-X(bar)", "|Xi-X(bar)|", "(Xi-X(bar))^2"]))
#Jangkauan
R = (max(dataKelompok[1])-min(dataKelompok[0]))
#Mean
#Simpangan Rata Rata
Sr = (jmlXi_X_abs/sum(Fi))
#Simpangan Baku
jmlXi_X_sqr = sum(Xi_X_sqr)
y =(jmlXi_X_sqr/sum(Fi))
Sd = math.sqrt(y)
#Varians
v = (Sd)**2

Data_Bawah = [[Mean, R, Sr, Sd, v]]
print()
print(tabulate.tabulate(Data_Bawah, headers=["Mean", "Jangkauan", "Simpangan Rata-rata", "Simpangan Baku", "Varians"]))