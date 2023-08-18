import requests

import configuration
import data


#   Creating a user
def post_new_user(user_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     json = user_body,
	                     headers = data.headers)


response = post_new_user(data.user_body)
#   Getting an authToken from an answer and output it
auth_token = response.json().get("authToken")


#   Creating a kit
def post_new_client_kit(kit_body, auth_token):
	data.headers["Authorization"] += auth_token
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_PRODUCTS_KIT_PATH,
	                     json = kit_body,
	                     headers = data.headers)


response = post_new_client_kit(data.kit_body, auth_token)
