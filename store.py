orders = [
    [100,200,150],
    [300,250],
    [400,100,50],
    ]

total_revenue =0

for i in range(len(orders)):
    ct = 0
    for j in range(len(orders[i])):
       ct += orders[i][j]
       
    print("coustmer",i+1,"expense=",ct)  
    total_revenue += ct
print()    
    
    
print("total revenue = ",total_revenue)    
    