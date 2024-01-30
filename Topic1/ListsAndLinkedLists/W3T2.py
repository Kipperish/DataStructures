list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
mergeList = []
list1Pointer = 0
list2Pointer = 0
while list1Pointer < len(list1) and list2Pointer < len(list2) :
    if list1[list1Pointer] <= list2[list2Pointer]:
        mergeList.append(list1[list1Pointer])
        list1Pointer += 1
    elif list2[list2Pointer] <= list1[list1Pointer]:
        mergeList.append(list2[list2Pointer])
        list2Pointer += 1
while list1Pointer < len(list1):
    mergeList.append(list1[list1Pointer])
    list1Pointer += 1
while list2Pointer < len(list2):
    mergeList.append(list2[list2Pointer])
    list1Pointer += 2
print(mergeList)