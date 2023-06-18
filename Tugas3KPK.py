
print("=== PROGRAM SEDERHANA MENCARI KPK ===")
a = int(input('Masukkan bilangan pertama = '))
b = int(input('Masukkan bilangan kedua   = '))

def fpb(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            fpb=i
        # else:
        #     continue
    return fpb

def kpk(a,b):
    kpk=int(a*b/fpb(a,b))
    return kpk

print('KPK = ',kpk(a,b))
