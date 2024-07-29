#3.
def merging_Dict(*args):
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result
dict1 = {'name': 'Anu', 'age': 20,'flower':'lily'}
dict2 = {'colour': 'red', 'flower': 'lily'}
dict3 = {'class': 10,'flower':'lily'}
print("Dict 1: ",dict1)
print("Dict 2: ",dict2)
print("Dict 3: ",dict3)
merged = merging_Dict(dict1, dict2, dict3)
print("After merge: ",merged)

def common_key(*args):
    common=set(args[0].keys())
    for dictionary in args[1:]:
        common &= dictionary.keys()
    return common
dict1 = {'name': 'Anu', 'age': 20,'flower':'lily'}
dict2 = {'colour': 'red', 'flower': 'lily'}
dict3 = {'class': 10,'flower':'lily'}
com=common_key(dict1,dict2,dict3)
print("Common keys: ",com)

def invert(dictt):
    result={}
    for key,value in dictt.items():
        if value in result:
            result[value].append(key)
        else:
            result[value]=[key]
    return result
student={'name':'Anu','age':20,'class':'Mca','roll_no':20}
print("Dictionary: ",student)
answer=invert(student)
print("Inverted Dictionary: ",answer)

def common_key_value(*dicts):
    common_pairs = dicts[0].items()
    for dictionary in dicts[1:]:
        common_pairs = common_pairs & dictionary.items()
    return dict(common_pairs)
dict1 = {'name': 'Anu', 'age': 20,'flower':'lily'}
dict2 = {'colour': 'red', 'flower': 'lily'}
dict3 = {'class': 10,'flower':'lily'}
common = common_key_value(dict1, dict2, dict3)
print("Common key value pair: ",common)



