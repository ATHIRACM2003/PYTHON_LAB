#6.sum of digits of 4 dig number , reverse of a 4 digit number
num=int(input("Enter a four digit number:\n "))
sum=0
rev=0
temp=num
while(num>0):
    dig=num%10
    sum+=dig
    rev=rev*10+dig
    num=num//10
print("Sum of digits: ",sum)
print("Reverse of the number: ",rev)
    
        
