from math import *
from random import *
print("puu läbimõõdu arvutamine")
#kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatav selle peale puu läbimõõt
c=float(input("anna ümbermõõt: "))
d=round(c/pi,2)
print(f"puu läbimõõt= {d}")



#2.Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

print("väljenda diagonaali pikkus")
N=float(input("Sisesta N:"))
M=float(input("Sisesta M:"))
d=round(sqrt(N**2+M**2),2)
print(f"Ristkülikukujulise maatüki diagonaal on {d}")

#3Leidke järgnevast näiteprogrammist semantiline viga:

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")
#4Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.

print("Aritmeetiline keskmine")
A1=int(input("Esimene arv:"))
A2=int(input("Teine arv"))
A3=int(input("Kolmas arv"))
A4=int(input("Neljas arv"))
A5=int(input("Viies arv"))
K=(A1+A2+A3+A4+A5)/5
print(f"kesknime on {K}")
#5
print("   @..@   ")
print("  (----)  ")
print(" ( \__/ ) ")
print(" ^^ "" ^^ ")
#6 Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c
print(F"Ümbermõõt on {P}")
#7 Pitsa
P=randint(1.6)
print("Igaüks maksab {summa}")
#8 Kütusekulu arvutamineKasutaja sisestab tangitud kütuse liitrid Kasutaja sisestab läbitud kilomeetrid Programm leiab kütusekulu 100km kohta keskmiselt
print("kütusekaalu arvutamine")
l=float(input("Kütuse liitride kogus:"))
km=float(input("Labitud kilomeetrid: "))
kulu=(l/km)*100
print(f"kütusekulu {kulu}")
#9 Rulluisutajad Rulluisutaja keskmine kiirus on 29,9km/h Kui kaugele jõuab M minutiga
print("Rulluisutajad")
M=int(input("Minutid:"))
M=M/60
tee=M*29.9
print(f"jõuab {tee} km")
#10 Ajateisendus
print("Sisenda aja minutis:")
M=int(input("Sisenda aja minutis:")) #1h=60min
H=M//60 #h
M=M%60 #min
print(f"{H}:{M}")


