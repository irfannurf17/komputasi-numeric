
#persiapan fungsi
f1=lambda x,y,z:(27-y+2*z)/10
f2=lambda x,y,z:(-15-3*x+z)/10
f3=lambda x,y,z:(25-2*x+3*y)/10
#inisialisasi
x0=0
y0=0
z0=0
iterasi = 1

e=float(input("Masukkan galat yang diinginkan : "))
print('\niterasi\tx\ty\tz\n')
kondisi=True
while kondisi :
	x1=f1(x0,y0,z0)
	y1=f2(x1,y0,z0)
	z1=f3(x1,y1,z0)
	print('%d\t %0.4f\t %0.4f\t %0.4f\n' %(iterasi,x1,y1,z1))
	e1=abs(x0-x1);
	e2=abs(y0-y1);
	e3=abs(z0-z1);
	
	iterasi+=1
	x0=x1
	y0=y1
	z0=z1

	kondisi = e1>e and e2>e and e3>e
print('\nHasil: x=%0.3f, y=%0.3f and z = %0.3f\n' %(x1,y1,z1))
