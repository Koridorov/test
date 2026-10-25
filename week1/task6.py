#Да се напише програма, която при подадени цели числа a,b,c да изчислява и принтира дискриминанта на квадратното уравнение ах2+bx+c=0.
#(Подсказка: D = b^2 - 4ac)
a,b,c=(input("Input the value of a, in the following uravnenie: ax2+bx+c=0: ")), (input("Input the value of b, in the following uravnenie: ax2+bx+c=0: ")), (input("Input the value of c, in the following uravnenie: ax2+bx+c=0: "))
D=(int(b)**2)-(4*int(a)*int(c))
print(f"Diskriminantata e {D}")

