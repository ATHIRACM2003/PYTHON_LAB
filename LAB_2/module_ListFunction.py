#1. module for list operations
import statistics as st
def maximum(listt):
    return max(listt)
def minimum(listt):
    return min(listt)
def add(listt):
    return sum(listt)
def average(listt):
    return sum(listt)/len(listt)
def median(listt):
    return st.median(listt)
def list_comprehension():
    num=[2,3,4,5]
    cube=[x*x*x for x in num]  
    print("List: ",cube)
    print("Largest: ",maximum(cube))
    print("Smallest: ",minimum(cube))
    print("Sum: ",add(cube))
    print("Average: ",average(cube))
    num2=[5*x for x in num]   #list comprehension 1
    print("\nList 2: ",num2)
    print("Largest: ",maximum(num2))
    print("Smallest: ",minimum(num2))
    print("Sum: ",add(num2))
    print("Average: ",average(num2))
    
