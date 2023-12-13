#Array Outlet1Sales[4]
#Array Outlet2Sales[4]
#Array Outlet3Sales[4]
Outlet1Sales = [10,12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]
sales = [Outlet1Sales,Outlet2Sales,Outlet3Sales]
def totalSale(array, quarter):
    total = 0
    for i in range(len(array)):
        total += array[i][quarter-1]
    return total
print(f"Total for quarter 1: {totalSale(sales, 1)}")
print(f"Total for quarter 2: {totalSale(sales, 2)}")
print(f"Total for quarter 3: {totalSale(sales, 3)}")
print(f"Total for quarter 4: {totalSale(sales, 4)}")