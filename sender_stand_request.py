import configuration
import requests
import data


#   Создание пользователя
def post_new_user(userbody):
	#   Подставляем полный url
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     #  Тут тело
	                     json = userbody,
	                     #  А здесь заголовки
	                     headers = data.headers)


response = post_new_user(data.user_body)
#   Получение authToken из ответа и его вывод
auth_token = response.json().get("authToken")
print(f"authToken: {auth_token}")


#   Создание набора для пользователя
def post_new_client_kit(kit_body, auth_token):
	data.headers["Authorization"] += auth_token
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
	                     json = kit_body,
	                     headers = data.headers)


response = post_new_client_kit(data.kit_body, auth_token)
#   Вывод набора и его статуса создания
print(f"newClientKitStatus: {response.status_code}")
print(response.json())
