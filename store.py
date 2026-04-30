# program to calculate the total revenue of store.

orders = [
    [100,200,150], #coustmer1  expences
    [300,250],     #coustmer2  expences
    [400,100,50],  #coustmer3  expences
    ]

total_revenue =0

for i in range(len(orders)):
    ct = 0
    for j in range(len(orders[i])):
       ct += orders[i][j]
       
    print("coustmer",i+1,"expense=",ct)  
    total_revenue += ct                  # calcutating total revenue of store
print()    
    
    
print("total revenue = ",total_revenue)    
    
