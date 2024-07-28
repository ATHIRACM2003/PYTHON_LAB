#8. print from dictionary
people =[
    {"name":"John Doe","age": 30,"blood_group":'A+'} , 
    {'name' :'Jane Smith ' ,'age' : 25 , 'blood_group' : ' B-' },
    {'name':'Emily Davis ' , 'age' : 40 , 'blood_group' : 'O+'},
    {'name':'William Johnson','age':35,'blood_group':'AB-'} ,
    {'name':'Michael Brown','age':28,'blood_group':'A-'} ,
    {'name':'Emma Wilson','age':22,'blood_group':'B+'} ,
    {'name':'Oliver Martinez','age':33,'blood_group':'O-'},
    {'name':'Sophie Anderson','age':37,'blood_group':'AB+'} ,
    {'name':'James Thomas','age':45,'blood_group':'A+'} ,
    {'name':'Isabelle Lee','age':38,'blood_group':'B-'} 
    ]

def people_info(people):
    for person in people:
        print(f"Name: {person['name']}")
        print(f"Age: {person['age']}")
        print(f"Blood Group: {person['blood_group']}")
        print("-" * 20)

people_info(people)
