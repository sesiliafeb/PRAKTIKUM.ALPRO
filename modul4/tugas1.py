def luas_kerucut():
    r =int(input("jari jari kerucut :"))
    s =int(input("selimut :"))
    rumus1 = 22/7 * r * s 
    rumus2 = r + s
    rumus3 = rumus1 * rumus2
    print ("luas permukaan kerucut :", rumus3)

def luas_limas():
    s =int(input("sisi limas :"))
    a =int(input("alas limas :"))
    t =int(input("tinggi limas :"))
    rumus1 = 1.72 * s * s
    rumus2 = 5 * 1/2 * a * t
    rumus3 = rumus1 + rumus2 
    print ("luas permukaan limas segilima:", rumus3)


def luas_prisma():
    luas_alas      =int(input("luas alas :"))
    keliling_alas  =int(input("keliling alas :"))
    t              =int(input("tinggi prisma :"))
    rumus = 2 * luas_alas + keliling_alas * t
    print ("luas permukaan prisma segilima :", rumus)

print("mengitung LUAS PERMUKAAN bangun ruang : kerucut, limas segilima, prisma segilima")
print("pilihan 1 untuk rumus luas permukaan kerucut")
print("pilihan 2 untuk rumus luas permukaan limas segilima") 
print("pilihan 3 untuk rumus luas permukaan prisma segilima")

pilihan_rumus = int(input("masukan pilihan yang mau anda hitung: "))
    
if pilihan_rumus == 1 :
        luas_kerucut()
         
elif pilihan_rumus == 2 :
        luas_limas()
        
elif pilihan_rumus == 3 :
        luas_prisma()
        
else :
        print("pilihan tidak valid. silahkan masukkan angka 1, 2, & 3")

