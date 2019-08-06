sums=0
sql=20
def north_west(tsil,row,col):
   # print(row,col,row-1*col-1)
    if (row-1)*(col-1)>2:
        global sums
        print(sql)
        if tsil[row-1][0]>tsil[0][col-1]:
            print(tsil[row-1][0],tsil[0][col-1])
            sums+=tsil[0][0]*tsil[0][col-1]
            print("partial sum: ",sums)
            tsil[row-1][0]-=tsil[0][col-1]
            list2=[[0 for i in range(col)]for j in range(row-1)]
            for i in range(row-1):
                for j in range(col):
                    list2[i][j]=tsil[i+1][j]
#removed row where supply is smaller
            north_west(list2,row-1,col)
        elif tsil[row-1][0]<tsil[0][col-1]:
            print(tsil[row-1][0],tsil[0][col-1])
            sums+=tsil[0][0]*tsil[row-1][0]
            print("partial sum: ",sums)
            tsil[0][col-1]-=tsil[row-1][0]
            list2=[[0 for i in range(col-1)]for j in range(row)]
            for i in range(row):
                for j in range(col-1):
                    list2[i][j]=tsil[i][j+1]
#removed coloumn where demand is smaller
            north_west(list2,row,col-1)
    if (col-1)==2:
        sums+=tsil[0][0]*tsil[1][0]+tsil[0][1]*tsil[1][1]
    elif (row-1)==2:
        sums+=tsil[0][0]*tsil[0][1]+tsil[1][0]*tsil[1][1]
    print(sums)
rows=int(input("enter number of rows: "))
columns=int(input("enter number of columns: "))
list1=[[0 for i in range(columns)]for j in range(rows)]
for i in range(rows):
    for j in range(columns):
        list1[i][j]=int(input("enter value: "))
      
north_west(list1,rows,columns)
