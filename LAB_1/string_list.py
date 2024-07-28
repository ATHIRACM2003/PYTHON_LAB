#2.return strings with first and last character identical from the list
A=['abc','xyz','aba','1221']
print("A= ",A)
#print(A.index('aba'))
for i in A:
    if i[0]==i[-1]:
        print(i," at index",A.index(i))

    
