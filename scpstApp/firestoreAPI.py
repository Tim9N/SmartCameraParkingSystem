import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore DB
cred = credentials.Certificate('./keys/smart-camera-parking-system-61282fd7a87b.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
database = db.collection('users')

 
def addUser(email:str, license_plate:str, name:str, credit_card_number:str, last_entry:str, password:str) -> bool:
    """
    Adds a new user to the database.
    @param email:str - The email of the user
    @param license_plate:str - The license plate of the user
    @param name:str - The name of the user
    @param credit_card_number:str
    @param last_entry:str - The last entry of the user
    @param password:str - The password of the user
    @return:bool - True if the user was added successfully, False otherwise
    """
    doc_ref = database.document(email)
    doc_ref.set({
        'name': name,
        'licensePlate': license_plate,
        'creditCardNumber': credit_card_number,
        'lastEntry': last_entry,
        'password': password
    })
    if doc_ref.id == email:
        return True
    else:
        return False



def getUser(email:str) -> dict:
    """
    Gets a user from the database by email.
    @param email:str - The email of the user
    @return:dict - The user's information if found, None otherwise
    """
    doc_ref = database.document(email)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def getUserByLicensePlate(license_plate:str) -> dict:
    """
    Gets a user from the database by license plate.
    @param license_plate:str - The license plate of the user
    @return:dict - The user's information if found, None otherwise
    """
    docs = database.where('licensePlate', '==', license_plate).get()
    if docs:
        return docs[0].to_dict()
    else:
        return None
    

def getUsers() -> list:
    """
    Gets all users from the database.
    @return:list - A list of all users in the database
    """
    docs = database.stream()
    users = []
    for doc in docs:
        users.append(doc.to_dict())
    return users


def updateUser(email:str, license_plate:str, name:str, credit_card_number:str, last_entry:str, last_exit:str, password:str) -> bool:
    """
    Updates a user's information in the database.
    @param email:str - The email of the user
    @param license_plate:str - The license plate of the user
    @param name:str - The name of the user
    @param credit_card_number:str
    @param last_entry:str - The last entry of the user
    @param last_exit:str - The last exit of the user
    @param password:str - The password of the user
    @return:bool - True if the user was updated successfully, False otherwise
    """
    doc_ref = database.document(email)
    doc_ref.update({
        'licensePlate': license_plate,
        'name': name,
        'creditCardNumber': credit_card_number,
        'lastEntry': last_entry,
        'password': password,
        'lastExit': last_exit
    })  
    if doc_ref.id == license_plate:
        return True
    else:
        return False
    

def deleteUser(email:str) -> bool:
    """
    Deletes a user from the database.
    @param email:str - The email of the user
    @return:bool - True if the user was deleted successfully, False otherwise
    """
    doc_ref = database.document(email)
    doc_ref.delete()
    if doc_ref.id == email:
        return True
    else:
        return False
    
def deleteAllUsers() -> bool:
    """
    Deletes all users from the database.
    @return:bool - True if all users were deleted successfully, False otherwise
    """
    docs = database.stream()
    for doc in docs:
        doc.reference.delete()
    return True 
    
    
    
