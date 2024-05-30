def userEntity(item) -> dict:
   return {
    'id': str(item['_id']),
    'name' : item['name'],
    'age' : item['age'],
    'contact' : item['contact'],
    'gender' : item['gender'],
 }

def usersEntity(entity) -> list:
   return [userEntity(_) for _ in entity ]