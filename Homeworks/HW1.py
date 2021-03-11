#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
#Merge two lists. Multiply all values in the newlist by 2.
#Use the loop to print the data type of the all values in the new list.

#Question 1

mylist1 = [3,5,7,9]
mylist2 = [10,12,14,16]

mylist1.extend(mylist2)

mylist3 =[x*2 for x in mylist1]

for i in mylist3: #mylist3 elemanlarını yazdırır.
    print(i, end=" ")
print("\n")    
for i in mylist3: #mylist3 elemanlarının type'ını yazdırır.
    print(type(i), end=" ") 
