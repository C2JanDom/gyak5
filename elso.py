print ("Adja meg a háromszög oldalának első hosszát!")
a = float(input())


print ("Adja meg a háromszög oldalának második hosszát!")
b = float(input())

print ("Adja meg a háromszög oldalának harmadik hosszát!")
c = float(input())


if a + b > c:
    print("A megadott szakaszok alkothatnak háromszöget.")

else:
    print("A megadott szakaszok nem alkothatnak háromszöget.")
