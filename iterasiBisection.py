a=0
b=10
i=0

while (b-a) > 0.1:
        i=i+1
        x=(a+b)/2
        if 5*x**3+3 <0:
            a=x
        elif 5*x**3+3 >0:
            b=x
        else:
            print('Nilai x ', x)
            break
        
        print('Iterasi ke-%d Nilai x terdekat ' %i, x)
