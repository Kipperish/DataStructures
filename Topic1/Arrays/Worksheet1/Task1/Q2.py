#Array names[max]
names = ["Johnathon", "Clarence", "Arnold", "Alfredo", "Reginald", "William James Octavius VII"]
def findNum(array, name):
    found = False 
    count = 0
    num = 0
    while found == False:
        if count == (len(array)-1) and array[len(array)-1] != name: #Checks if it has iterated through full array and not found the name
            found == True #sets found to true to break out of the loop so it is not infinite
            print("Name not found")
        elif  array[count] == name: #Checks if the current position in the array holds name
            num = count+1
            found = True #sets found to true to break out of the loop
            print(f"Record Number for {name}: {num}")
        count += 1

findNum(names ,"Arnold")
findNum(names ,"Demetrius")
