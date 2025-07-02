'''
def hash_operation(value:str)->int:
    hash_code:int = 0
    for letter in value:
        hash_code += ord(letter)
    
    hash_code= hash_code % 10
    return hash_code

#print(hash_operation("lulu")) return 0

def add_to_list(value:str,my_list:list[str])->None:
    get_index = hash_operation(value)
    my_list[get_index] = value
    return None

def search_for(value:str,my_list:list[str])->bool:
    index:int = hash_operation(value)
    if my_list[index] == value:
        return True
    else:
        return False

hash_list : list[str] = ["" for _ in range(10)]

add_to_list('lulu',hash_list)
print(hash_list)
print(search_for('lulu',hash_list))
'''

def hash_operation(value:str)->int:
    hash_code:int = 0
    for letter in value:
        hash_code += ord(letter)
    
    hash_code= hash_code % 10
    return hash_code

def add_to_list(value:str,my_list:list[list[str]])->None:
    get_index = hash_operation(value)
    my_list[get_index].append(value)
    return None

def search_for(value:str,my_list:list[list[str]])->bool:
    index:int = hash_operation(value)
    for data in my_list[index]:
        if data==value:
            return True
    return False

hash_list : list[list[str]] =[[] for _ in range(10)]