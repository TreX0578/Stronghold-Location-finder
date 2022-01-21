p=float(input("Enter the pixel change: "))
d=(2250/p)
print("Rough distance: ",int(d),"blocks \n",round(d/8)," blocks in the nether")
x1=float(input("Enter your X of first standing point: "))
z1=float(input("Enter your Z of first standing point: "))
x2=float(input("Enter your X of second standing point: "))
z2=float(input("Enter your Z of second standing point: "))
m=(z2-z1)/(x2-x1)
r=(1+m*m)**(1/2)
pos_x3=(d/r)+x1
pos_z3=((d*m)/r)+z1
neg_x3=-1*(d/r)+x1
neg_z3=-1*((d*m)/r)+z1
if (x2>x1 and z2<z1) or (x2<x1 and z2<z1):
  print("Rough stronghold position(X,Z): (",int(pos_x3),",",int(pos_z3),")\n Nether position of stronghold: (",round(pos_x3/8),",",round(pos_z3/8),")")
if (x2<x1 and z2>z1) or (x2>x1 and z2>z1):
  print("Rough stronghold position(X,Z): (",int(neg_x3),",",int(neg_z3),")\n Nether position of stronghold: (",round(neg_x3/8),",",round(neg_z3/8),")")
