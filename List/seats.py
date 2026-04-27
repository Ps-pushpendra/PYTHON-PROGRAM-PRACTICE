# python program to check the availability of seats as the seats given in the from of list.

# 1 = booked , 0 = empty seat

# seat arrangement

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
        print(seats[i][j],end=" ") # here end is for apace between the seats 
    
        if (seats[i][j]==1):
           booked +=1
        if (seats[i][j]==0):
           empty +=1    
    print()
print()    
        
print("total booked seats: ",booked)
print("total empty seats: ",empty)
        
