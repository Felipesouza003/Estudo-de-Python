import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

d = float(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

if(d >= 10):
    print("longe")
else:
    print("perto")