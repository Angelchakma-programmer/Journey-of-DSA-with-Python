

#Linear time complexity O(n):
#It's A lineaer time Complexity.

name = ["Angel Chakma","Lolin Chakma","Noppo Chakma","Biggan Chakma","Junan Chakma"]
a = 0
for i in name:
    a += 1
    print(a,":",i)

#problem 1
number = [10, 20, 30, 40, 50]

addition = sum(number)
print("Total sum is :",addition)

#problem two
#find even number on list
no = [12, 7, 4, 9, 16, 3, 8]
count_even = 0
for num in no:
    if num %2   == 0:
        count_even +=1

#This is O(n)

print("Total even number is :",count_even)

#problem 3:
#Find learg numbers

arrry = [14, 7, 29, 3, 21, 11]

learg_no = arrry[0]
for angel in arrry:
    if angel > learg_no:
        learg_no = angel

print("The learge number is :",learg_no)


#problem 4 :
#Count a target numbers

numbers = [5, 2, 5, 8, 5, 3, 2, 5]
count_target = 0
for s in numbers:
    if s == 5:
        count_target += 1
print(count_target, "time has 5 in list")

#problem 5:
#Reverse list

lists = [10, 20, 30, 40, 50]
num_items = len(lists)
new_list = []
for x in lists:
    num_items -= 1
    new_list.append(lists[num_items])

print("The new list is :",new_list)

#prolem 6:
#find numbers have or not

nums = [4, 9, 2, 1, 7, 11]
found = False
for nub in nums:
    if nub == 15:
        found = True
if found == True:

            print("yes found")


else:
            print("Not found")




