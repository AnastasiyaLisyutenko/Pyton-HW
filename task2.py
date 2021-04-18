print("Введите время в секундах")
time = int(input())
h = time // 3600
m = (time % 3600) // 60
s = time % 60
print("{0}:{1}:{2}".format(h, m, s))
