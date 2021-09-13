import sys
import re

if __name__ == "__main__":
    file = sys.argv[1]
    f2 = open(file)
    arr = []
    for line in f2:
        line = re.findall('\d*', line)[0]
        arr.append(int(line))
    K = round(sum(arr)/len(arr))
    summ = 0
    for i in range(len(arr)):
        summ += abs(K - arr[i])
    print(summ)
