seats = [
    [1,0,0,1,0],
    [0,1,1,0,0],
    [0,0,0,1,1],
    [1,0,1,0,0],
    [1,1,0,0,1]
    ]
    
booked = empty = 0
    
for i in range(len(seats)):
    for j in range(len(seats[i])):
        print(seats[i][j],end=" ")
    
        if (seats[i][j]==1):
           booked +=1
        if (seats[i][j]==0):
           empty +=1    
    print()
print()    
        
print("total booked seats: ",booked)
print("total empty seats: ",empty)
        
