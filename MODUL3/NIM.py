#program angka terakhir nim

angka = int(input ("masukkan angka :"))

for i in range(angka):
  if i == 0 or i == angka-1:
    print("O"*angka)
  else:
    print("O" + " "*(angka-2) + "O")
print()

for i in range (angka):
  for j in range (angka):
    if i == angka//2 or j == 0 and i < angka //2 or j == angka-1 and i > -1:
      print ("O", end="")
    else :
      print(" ", end="")
  print()
print ()

for i in range(angka):
  if i == 0 or i == angka-1:
    print("O"*angka)
  else:
    print("O" + " "*(angka-2) + "O")
print()

