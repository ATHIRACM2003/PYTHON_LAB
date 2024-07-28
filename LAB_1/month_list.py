#10. month days
months=['January','February','March','April','May','June','July','August','September','October','November','December']
mon=input("Enter the month name ")
if mon in ('January','March','May','July','August','October','December'):
    print(f"The number of days in {mon} is 31")
elif mon in ('February','April','June','September','November'):
    if mon=='February':
        year=int(input("Enter year"))
        if year%4==0:
            print(f"The number of days in {mon} is 29")
        else:
            print(f"The number of days in {mon} is 28")
    else:
        print(f"The number of days in {mon} is 30")
else:
    print("Invalid input")
