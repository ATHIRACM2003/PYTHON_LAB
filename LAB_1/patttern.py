#3.print patterns
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
    
let = ['A', 'B', 'C', 'D', 'E']
n = len(let)  
for i in range(n):
    for j in range(n - i - 1):    # Print spaces
        print(" ", end=" ")
    for j in range(i + 1):      # Print letters
        print(let[j], end=" ")
    print("\n")

