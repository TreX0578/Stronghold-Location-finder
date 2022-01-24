import sys
p=float(input("Enter the pixel change: "))
d=(3000/p)
print()
print("Rough distance: ",int(d),"blocks \n",round(d/8)," blocks in the nether")
x1=float(input("Enter your X of your initial standing block: "))
z1=float(input("Enter your Z of your initial standing block: "))
x2=float(input("Enter your X of your final standing block: "))
z2=float(input("Enter your Z of your final standing block: "))
print()
if x1==x2 and z1==z2:
  sys.exit("Both of your cordinates are same, check for signs and re-enter your data for X and Z, in both initial and final standing block")
if x1==x2:
  x1+=0.00000000001
if z1==z2:
  z1+=0.00000000001
m=(z2-z1)/(x2-x1)
r=(1+m*m)**(1/2)
pos_x3=(d/r)+x1
pos_z3=((d*m)/r)+z1
neg_x3=-1*(d/r)+x1
neg_z3=-1*((d*m)/r)+z1
if (x2>x1 and z2<z1) or (x2>x1 and z2>z1):
  print("Rough stronghold position(X,Z): (",int(pos_x3),",",int(pos_z3),")\n Nether position of stronghold: (",round(pos_x3/8),",",round(pos_z3/8),")")
if (x2<x1 and z2>z1) or (x2<x1 and z2<z1):
  print("Rough stronghold position(X,Z): (",int(neg_x3),",",int(neg_z3),")\n Nether position of stronghold: (",round(neg_x3/8),",",round(neg_z3/8),")")
