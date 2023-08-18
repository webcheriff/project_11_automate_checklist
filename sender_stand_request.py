import configuration
import requests
import data


def post_new_user(body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # Подставляем полный url
	                     json = body,  # Тут тело
	                     headers = data.headers)  # А здесь заголовки


response = post_new_user(data.user_body)
auth_token = response.json().get('authToken')  # Получение authToken из ответа
print(f"authToken: {auth_token}")


def post_new_client_kit(kitbody, authtoken):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
	                     json = kitbody,
	                     headers = data.headers)


response = post_new_client_kit(data.kit_body, auth_token)
print(f"newClientKitStatus: {response.status_code}")
