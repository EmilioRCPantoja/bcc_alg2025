a = int(input('digite um número: '))
b = int(input('digite mais um número: '))
n = int(input('digite quantos números a mais você deseja colocar: '))
x1 = a+b
x = [x1]
i=1
for i in range(n):
 if i%2 != 0:
   xn = int(input('digite outro número: '))
   xn = xn + x[i]
   x.append(xn)
   
 else:
   xn = int(input("digite outro número: "))
   xn = xn * x[i]
   x.append(xn)
   
xs = sum(x)
print(xs)
