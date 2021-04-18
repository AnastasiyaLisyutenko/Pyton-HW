print("Введите целое число")
value = int(input())
max_value = 0
cach_value = 0;
while value != 0:
    cach_value = value % 10
    value = value // 10
    if (max_value < cach_value):
        max_value = cach_value
print(max_value)
