p=float(input("Enter the pixel change: "))
d=(2250/p)
print("Rough distance= ",int(d),"blocks \n",int(d/8)," blocks in the nether")
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
diff_x=x1-x2
diff_z=z1-z2
if diff_x>diff_z:
  if x1>x2:
    print("Rough stronghold position(X,Z) = (",int(neg_x3),",",int(neg_z3),")\n Nether position of stronghold = (",int(neg_x3/8),",",int(neg_z3/8),")")
  if x2>x1:
    print("Rough stronghold position(X,Z) = (",int(pos_x3),",",int(pos_z3),")\n Nether position of stronghold = (",int(pos_x3/8),",",int(pos_z3/8),")")
  if x1==x2:
    print("ERROR! CORDINATES SEEMS TO BE SAME, RUN THE CODE AGAIN WITH CORRECT VALUES")
if diff_z>diff_x:
  if z1>z2:
    print("Rough stronghold position(X,Z) = (",int(neg_x3),",",int(neg_z3),")\n Nether position of stronghold = (",int(neg_x3/8),",",int(neg_z3/8),")")
  if z2>z1:
    print("Rough stronghold position(X,Z) = (",int(pos_x3),",",int(pos_z3),")\n Nether position of stronghold = (",int(pos_x3/8),",",int(pos_z3/8),")")
  if z1==z2:
    print("ERROR! CORDINATES SEEMS TO BE SAME, RUN THE CODE AGAIN WITH CORRECT VALUES")
if diff_x==diff_z:
  if z1>z2:
    print("Rough stronghold position(X,Z) = (",int(neg_x3),",",int(neg_z3),")\n Nether position of stronghold = (",int(neg_x3/8),",",int(neg_z3/8),")")
  if z2>z1:
    print("Rough stronghold position(X,Z) = (",int(pos_x3),",",int(pos_z3),")\n Nether position of stronghold = (",int(pos_x3/8),",",int(pos_z3/8),")")
