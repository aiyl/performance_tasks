import sys
import re

dot_x = []
dot_y = []
file1 = sys.argv[1]
file2 = sys.argv[2]
f2 = open(file2)
for line in f2:
    line = re.findall('[-+]?\d+[\.]?\d*', line)
    dot_x.append(float(line[0]))
    dot_y.append(float(line[1]))
f2.close()

f1 = open(file1)
x = f1.read()
x2 = re.findall('[-+]?\d+[\.]?\d*',x)
xo = float(x2[0])
yo = float(x2[1])
r = float(x2[2])
f1.close()

for i in range(len(dot_x)):
    if (dot_x[i] - xo)**2 + (dot_y[i] - yo)**2 == r**2:
        print(0)
    elif (dot_x[i] - xo)**2 + (dot_y[i] - yo)**2 < r**2:
        print(1)
    else:
        print(2)