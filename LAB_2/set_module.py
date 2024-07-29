#2.set modules
def add(sett,value):
    new=sett.add(value)
    return new
def rem(sett,value):
    new=sett.discard(value)
    return new
def un_in(s1,s2):
    uni=s1.union(s2)
    print("Union: ",uni)
    inter=s1.intersection(s2)
    print("Intersection: ",inter)
def diff(s1,s2):
    return s1-s2
def sub(s1,s2):
    return s1.issubset(s2)
def length(s):
    j=0
    for i in s:
        j+=1
    return j
def sym_diff(s1,s2):
    return s1.symmetric_difference(s2)
def power_set(s):
    s = list(s)
    power_set = [[]]
    for elem in s:
        new_subsets = [subset + [elem] for subset in power_set]
        power_set.extend(new_subsets)
    return power_set

def unique_subsets(input_set):
    input_list = list(input_set)
    result = []
    def find_sub(current, index):
        result.append(current.copy())
        for i in range(index, len(input_list)):
            current.append(input_list[i])
            find_sub(current, i + 1)
            current.pop() 
    find_sub([], 0)
    return result





    

    
