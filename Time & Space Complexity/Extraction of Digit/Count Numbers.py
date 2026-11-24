
import math
#Count digit in numbers variable...
#just using logic..
numbers = 12345675757575757

num = numbers
count = 0

while num > 0 :
    count += 1
    num = num // 10

print("The numbers len is :",count)
#here is time complexity O(log10 (N)) and space complexity O(1)
#using math module

def Count_numbers(num):
    a = int(math.log10(num)) + 1
    
    print("The numbers len isss : ",a)

Count_numbers(numbers)
#here is time complexity O(log10(N)) and space complexity is O(1)
