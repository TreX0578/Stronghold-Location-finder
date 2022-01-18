p=float(input("Enter the pixel change: "))

d=int(2250/p)

print("Rough distance= ",d,"blocks")

x1=int(input("Enter your X of first standing point: "))

z1=int(input("Enter your Z of first standing point: "))

x2=int(input("Enter your X of second standing point: "))

z2=int(input("Enter your Z of second standing point: "))

m=(z2-z1)/(x2-x1)

x3=int(d/((1+m*m)**(1/2))+x1)

z3=int((d*m)/((1+m*m)**(1/2))+z1)

print("Rough stronghold position(X,Z) = (",x3,",",z3,")\n Nether position of stronghold = (",int(x3/8),",",int(z3/8),")")
