x0 = float(2)
y0 = float(3)
x1 = float(4)
y1 = float(5)
x2 = float(6)
y2 = float(7)

b0 = y0

b1 = (y1-y0)/(x1-x0)
c1 = (y2-y1)/(x2-x1)
b2 = (c1-b1)/(x2-x0)

x = float(3.5)
y = b0+b1 * (x-x0)+ b2*(x-x0)*(x-x1)
print(f"Hasil nilai x %1.4f memiliki nilai y %1.4f" %(x,y))
