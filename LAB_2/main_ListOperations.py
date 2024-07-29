#1.importing the list function module
import module_ListFunction as modf
age=[20,40,30,5]
modf.list_comprehension()
print("\n")
print("Age: ",age)
print("Oldest: ",modf.maximum(age))
print("Youngest: ",modf.minimum(age))
print("Sum of ages: ",modf.add(age))
print("Average of ages: ",modf.average(age))
print("Median of list [10,2,5,6,12]= ",modf.median([10,2,5,6,12]))

