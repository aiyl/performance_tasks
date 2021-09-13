import sys

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        arr = []
        for i in range(n):
            arr.append(i + 1)

        class CustomList(list):
            def __getitem__(self, index):
                return super(CustomList, self).__getitem__(index % len(self))

        a = CustomList(arr)

        k = 0
        str1 = str(a[0])
        while a[0] != a[k + m - 1]:
            k += m - 1
            str1 += str(a[k])
        print(str1)
    except Exception as e:
        print("need another argument" + str(e))