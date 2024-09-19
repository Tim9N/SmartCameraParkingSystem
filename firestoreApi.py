import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore DB
cred = credentials.Certificate('./keys/smart-camera-parking-system-61282fd7a87b.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
database = db.collection('users')

 
# This function adds a new user to the database.
# @param license_plate:str - The license plate of the user
# @param first_name:str - The first name of the user
# @param last_name:str - The last name of the user
# @param credit_card_number:str
# @return:bool - True if the user was added successfully, False otherwise
def addUser(license_plate:str, first_name:str, last_name:str, credit_card_number:str) -> bool:
    doc_ref = database.document(license_plate)
    doc_ref.set({
        'firstName': first_name,
        'lastName': last_name,
        'creditCardNumber': credit_card_number,
        'lastEntry': firestore.SERVER_TIMESTAMP
    })
    if doc_ref.id == license_plate:
        return True
    else:
        return False


# This function gets a user from the database.
# @param license_plate:str - The license plate of the user
# @return:dict - The user's information if found, None otherwise
def getUser(license_plate:str) -> dict:
    doc_ref = database.document(license_plate)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    

# This function gets all users from the database.
# @return:list - A list of all users in the database
def getUsers() -> list:
    docs = database.stream()
    users = []
    for doc in docs:
        users.append(doc.to_dict())
    return users


# This function updates a user's information in the database.
# @param license_plate:str - The license plate of the user
# @param first_name:str - The first name of the user
# @param last_name:str - The last name of the user
# @param credit_card_number:str
# @return:bool - True if the user was updated successfully, False otherwise
def updateUser(license_plate:str, first_name:str, last_name:str, credit_card_number:str) -> bool:
    doc_ref = database.document(license_plate)
    doc_ref.update({
        'firstName': first_name,
        'lastName': last_name,
        'creditCardNumber': credit_card_number,
        'lastEntry': firestore.SERVER_TIMESTAMP
    })  
    if doc_ref.id == license_plate:
        return True
    else:
        return False
    

# This function deletes a user from the database.
# @param license_plate:str - The license plate of the user
# @return:bool - True if the user was deleted successfully, False otherwise
def deleteUser(license_plate:str) -> bool:
    doc_ref = database.document(license_plate)
    doc_ref.delete()
    if doc_ref.id == license_plate:
        return True
    else:
        return False
    
# This function deletes all users from the database.
# @return:bool - True if all users were deleted successfully, False otherwise
def deleteAllUsers() -> bool:
    docs = database.stream()
    for doc in docs:
        doc.reference.delete()
    return True 
    
    
    
