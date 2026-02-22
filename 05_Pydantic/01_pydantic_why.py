def insert_patient_data(name: str,age: int):
    print(name,age)

    # if age < 0:
    #     raise ValueError('age cannot be negative')
    # else:
    #     if type(name)== str and type(age) == int:
    #         print(name)
    #         print(age)
    #         print('inserted into database')
    #     else:
    #         raise TypeError('name and age must be string and int respectively')

data = insert_patient_data('hasnain', 'g')
print(data)