# Array Numbers [6]
numbers = [1,2,3,4,5,6]
total = 0
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i]) #Prints the value at the index pointed to in the array
    total += numbers[i] #increases total by the value found in the array
print(f"Total is {total}") 
print(f"Average is {total/6}")