#2.importing set module
import set_module as sm
numbers={12,14,25,24,30}
print("Set 1= ",numbers)
sm.add(numbers,24)
print("After adding, set= ",numbers)
print("The element removed: ",sm.rem(numbers,20))
print("After removing, set= ",numbers)
sm.rem(numbers,12)
print("After removing, set= ",numbers)
age={20,10,50,60}
print("Set 2= ",age)
sm.un_in(numbers,age)
count={10,20,30,40}
print("Set 3= ",count)
print("Difference of set2 and set3: ",sm.diff(age,count))
s1={1,3,5,7,9}
s2={2,3,4,5,6}
print("Set 4= ",s1)
print("Set 5= ",s2)
print("Is set 5 subset of set 4? ",sm.sub(s2,s1))
print("The length of set 5 is: ",sm.length(s2))
print("Symmetric difference of set 4 and set 5= ",sm.sym_diff(s1,s2))
s3 = {1, 2, 3}
print("Set 6= ",s3)
print(sm.power_set(s3))
sett = {1, 2, 3}
subsets = sm.unique_subsets(sett)
print("Unique Subsets: ")
for subset in subsets:
    print(subset)
