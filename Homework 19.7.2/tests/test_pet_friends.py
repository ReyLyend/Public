from api import PetFriends
from settings import valid_email, valid_password
from settings import testpet_name, testpet_animal_type, testpet_age, testpet_pet_photo

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Test 1. Get api key for valid email and password"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_valid_user_incorrect_password(email=valid_email, password='incorrect_password'):
    """Test 2. Get api key for valid email, incorrect password"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_invalid_user(email='invalid_email', password='incorrect_password'):
    """Test 3. Get api key for invalid email and password"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_api_key_empty_fields(email='', password=''):
    """Test 4. Get api key. Empty fields"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result

def test_get_all_pets_with_valid_key(filter=''):
    """Test 5. Get list of pets for valid auth key."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_with_invalid_key(filter=''):
    """Test 6. Get list of pets for invalid auth key."""
    auth_key = {"key": "incorrect"}
    status, _ = pf.get_list_of_pets(auth_key, filter)
    assert status == 403

def test_post_new_pet_without_photo_with_valid_data(name=testpet_name, animal_type=testpet_animal_type, age=testpet_age):
    """Test 7. Post new pet without picture."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_without_photo(auth_key, name, animal_type, age)
    with open('pets.txt', 'w', encoding='utf8') as myFile:
        myFile.write(result['id'])
    assert status == 200
    assert len(result) > 0

def test_post_new_pet_without_photo_with_empty_data(name='', animal_type='', age=''):
    """Test 8. Post new pet without picture. Empty data."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_without_photo(auth_key, name, animal_type, age)
    with open('pets.txt', 'w', encoding='utf8') as myFile:
        myFile.write(result['id'])
    assert status == 400
    assert len(result) > 0

def test_post_new_pet_without_photo_incorrect_auth_key(name=testpet_name, animal_type=testpet_animal_type, age=testpet_age):
    """Test 9. Post new pet without picture. Incorrect Auth key"""
    auth_key = {"key": "incorrect"}
    status, _ = pf.post_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 403

def test_post_new_pet_with_valid_data_and_photo(name=testpet_name, animal_type=testpet_animal_type, age=testpet_age, pet_photo=testpet_pet_photo):
    """Test 10. Post new pet"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open('pets.txt', 'w', encoding='utf8') as myFile:
        myFile.write(result['id'])
    assert status == 200
    assert len(result) > 0

def test_post_new_pet_with_data_invalid_auth_key(name=testpet_name, animal_type=testpet_animal_type, age=testpet_age, pet_photo=testpet_pet_photo):
    """Test 11. Post new pet. Invalid auth key"""
    auth_key = {"key": "incorrect"}
    status, _ = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403

def test_post_new_pet_with_invalid_photo_format(name=testpet_name, animal_type=testpet_animal_type, age=testpet_age, pet_photo='not_a_photo.txt'):
    """Test 12. Post new pet. Invalid photo file format"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_post_new_pet_with_invalid_photo(name=testpet_name, animal_type=testpet_animal_type, age=testpet_age, pet_photo='asdf'):
    """Test 13. Post new pet. Missing photo file"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    try:
        status, _ = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    except Exception as e:
        assert type(e) == FileNotFoundError

def test_post_new_pet_with_large_number_age(name=testpet_name, animal_type=testpet_animal_type, age='9999999999999999999999999999', pet_photo=testpet_pet_photo):
    """Test 14. Post new pet. Large number age"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_post_new_pet_with_large_number_age(name=testpet_name, animal_type=testpet_animal_type, age='qwerty', pet_photo=testpet_pet_photo):
    """Test 15. Post new pet. Invalid age"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, _ = pf.post_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_post_set_photo_for_pet_id_with_valid_data(pet_photo=testpet_pet_photo):
    """Test 16. Set photo for pet id"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    with open('pets.txt') as myFile:
        pet_id = myFile.readline()
    status, result = pf.post_set_photo_for_pet_id(auth_key, pet_id, pet_photo)
    assert status == 200
    assert len(result) > 0

def test_post_set_photo_for_pet_id_invalid_auth_key(pet_photo=testpet_pet_photo):
    """Test 17. Set photo for pet id. Invalid auth key"""
    auth_key = {"key": "incorrect"}
    with open('pets.txt') as myFile:
        pet_id = myFile.readline()
    status, _ = pf.post_set_photo_for_pet_id(auth_key, pet_id, pet_photo)
    assert status == 403

def test_post_set_photo_for_invalid_pet_id(pet_photo=testpet_pet_photo):
    """Test 18. Set photo for invalid pet id"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = ''
    status, _ = pf.post_set_photo_for_pet_id(auth_key, pet_id, pet_photo)
    assert status == 404

def test_delete_pet_with_valid_id():
    """Test 19. Delete"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    with open('pets.txt') as myFile:
        pet_id = myFile.readline()
    status = pf.delete_pet(auth_key, pet_id)
    assert status == 200

def test_modify_pet_with_valid_id(name='Brady', animal_type='Cat', age='3'):
    """Test 20. Modify"""
    with open('pets.txt') as myFile:
        pet_id = myFile.readline()
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.modify_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


