#4.list to dictionary
listColour=["Black","Red","Maroon","Yellow"],["000000","FF0000","800000","FFFF00"]
print(listColour)
list_Color=[]
for i in listColour:
    list_Color.append({listColour[0][0]:listColour[1][0],listColour[0][1]:listColour[1][1],listColour[0][2]:listColour[1][2],listColour[0][3]:listColour[1][3]})
print(list_Color)
    
