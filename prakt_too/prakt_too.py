from math import *
from random import *
print("puu l�bim��du arvutamine")
#kirjuta programm, mis k�sib kasutaja k�est puu �mberm��du ning teatav selle peale puu l�bim��t
c=float(input("anna �mberm��t: "))
d=round(c/pi,2)
print(f"puu l�bim��t= {d}")



#2.Arvutage Pythoni k�sureal, kui pikk on ristk�likukujulise maat�ki diagonaal, mille m��tmed on Nm x Mm. N ja M k�si kasutajalt.

print("v�ljenda diagonaali pikkus")
N=float(input("Sisesta N:"))
M=float(input("Sisesta M:"))
d=round(sqrt(N**2+M**2),2)
print(f"Ristk�likukujulise maat�ki diagonaal on {d}")

#3Leidke j�rgnevast n�iteprogrammist semantiline viga:

aeg = float(input("Mitu tundi kulus s�iduks? "))
teepikkus = float(input("Mitu kilomeetrit s�itsid? "))
kiirus = teepikkus/aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")
#4Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 t�is arvust.

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
#6 Arvutame kolmnurga �mberm��du. Loo kolm t�isarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga �mberm��du (P=a+b+c)
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c
print(F"�mberm��t on {P}")
#7 Pitsa
P=randint(1.6)
print("Iga�ks maksab {summa}")
#8 K�tusekulu arvutamineKasutaja sisestab tangitud k�tuse liitrid Kasutaja sisestab l�bitud kilomeetrid Programm leiab k�tusekulu 100km kohta keskmiselt
print("k�tusekaalu arvutamine")
l=float(input("K�tuse liitride kogus:"))
km=float(input("Labitud kilomeetrid: "))
kulu=(l/km)*100
print(f"k�tusekulu {kulu}")
#9 Rulluisutajad Rulluisutaja keskmine kiirus on 29,9km/h Kui kaugele j�uab M minutiga
print("Rulluisutajad")
M=int(input("Minutid:"))
M=M/60
tee=M*29.9
print(f"j�uab {tee} km")
#10 Ajateisendus
print("Sisenda aja minutis:")
M=int(input("Sisenda aja minutis:")) #1h=60min
H=M//60 #h
M=M%60 #min
print(f"{H}:{M}")


