import json
import allure
from utils.checking import Checking
from utils.API import GoogleMapsAPI


"""Создание, изменение, удаление локации"""


@allure.epic("Создание новой локации")
class TestCreatePlace():

    @allure.description("Создание, изменение и удаление новой локации")
    def test_create_new_place(self):

        print('Метод POST')
        result_post = GoogleMapsAPI.create_new_place()  # Создание новой локации
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)    # Проверка статус кода
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])    # Проверка наличия полей
        Checking.check_json_value(result_post, 'status', 'OK')    # Проверка значения обязательного поля

        print('Метод ГЕТ')
        result_get = GoogleMapsAPI.get_new_place(place_id)    # Проверка созданной локации
        Checking.check_status_code(result_get, 200)    # Проверка статус кода
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])    # Проверка наличия полей
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')    # Проверка значения обязательного поля

        print('Метод ПУТ')
        result_put = GoogleMapsAPI.put_new_place(place_id)  # Изменение адреса локации
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод ГЕТ')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')  # Проверка смены адреса

        print('Метод DELETE')
        result_delete = GoogleMapsAPI.delete_new_place(place_id)  # Удаление локации
        Checking.check_status_code(result_delete, 200)
        print(list(json.loads(result_delete.text)))
        Checking.check_json_token(result_delete, ['status'])

        print('Метод ГЕТ')
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Проверка существования локации
        Checking.check_status_code(result_get, 404)


