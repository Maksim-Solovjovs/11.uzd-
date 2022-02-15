sk = int(input("Ievadi skolnieku skaitu: "))
a = 1
b = 0
c = 0
d = 0
while a<=sk:
  sk1 = int(input("Ievadi atzimi: "))
  if sk1>7:
    b=b+1
  elif sk1>=5 and sk1<=7:
    d=d+1
  else:
    c=c+1
  a=a+1
print("Teicamnieki:",b)
print("Viduveji:",d)
print("Nesekmigi:",c)