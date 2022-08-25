import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email: str, password: str) -> json:
        """Method does API request to server and returns status code and result
        in JSON format with unique user key, found with requested email and password"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:
        """Method does API request to server and returns status code and result with
        the list of all found pets, based on the used filter. Empty filter will give all pets.
        'my_pets' filter will return user's pets"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            }
        )
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/create_pet_simple', data=data, headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open('images/' + pet_photo, 'rb'), 'image/jpg')
            }
        )
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', data=data, headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_set_photo_for_pet_id(self, auth_key: json, pet_id: str, pet_photo: str):
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open('images/' + pet_photo, 'rb'), 'image/jpg')
            }
        )
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, data=data, headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> str:
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        return status

    def modify_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            }
        )
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.put(self.base_url + 'api/pets/' + pet_id, data=data, headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


