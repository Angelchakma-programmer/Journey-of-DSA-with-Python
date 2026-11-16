
#Reverse number..
number = 123456
a = []
while number > 0:
    last_number = number%10
    print(last_number)

    number = number//10
    num = a.append(last_number)
print(a)

n = 6789

res = int(str(n)[::-1])
print(res)