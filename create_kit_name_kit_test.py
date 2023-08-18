import sender_stand_request
import data


symbol511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
n = 0

# Getting a body of product’s kit
def get_kit_body(name):
	current_kit_body = data.kit_body.copy()
	current_kit_body["name"] = name
	return current_kit_body

#   Definition of positive asserts
def positive_assert(name):
	kit_body = get_kit_body(name)
	kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)
	assert kit_response.json()["name"] == name
	print(f"\nnameNewKit: {name}")
	assert kit_response.status_code == 201
	print(f"newKitStatusCode: {kit_response.status_code}")


#   Definition of negative asserts
# def negative_assert(name):
# 	kit_body = get_kit_body(name)
# 	response = sender_stand_request.post_new_user(kit_body)


# Definitions of positive tests
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assert("a")


def test_create_kit_511_symbols_in_name_get_success_response():
	positive_assert(symbol511)


def test_create_kit_english_letters_in_name_get_success_response():
	positive_assert("QWErty")
	
	
def test_create_kit_512_symbols_in_name_get_success_response():
	positive_assert(symbol512)


def test_create_kit_russian_letters_in_name_get_success_response():
	positive_assert("Мария")
	
	
def test_create_kit_has_special_symbols_in_name_get_success_response():
	positive_assert("\"№%@\",")


def test_create_kit_has_space_in_name_get_success_response():
	positive_assert("Человек и КО")


def test_create_kit_has_number_in_name_get_success_response():
	positive_assert("123")


# Definitions of negative tests
# def test_create_kit_1_letter_in_name_get_error_response():
# 	negative_assert_symbol("A")
#
#
# def test_create_kit_16_letter_in_name_get_error_response():
# 	negative_assert_symbol("Аааааааааааааааa")
#
#
# def test_create_kit_no_name_get_error_response():
# 	kit_body = data.kit_body.copy()
# 	# Удаление параметра firstName из запроса
# 	kit_body.pop("firstName")
# 	negative_assert_no_firstname(kit_body)
#
#
# def test_create_kit_empty_name_get_error_response():
# 	kit_body = get_kit_body("")
# 	negative_assert_no_firstname(kit_body)
#
#
# def test_create_kit_number_type_name_get_error_response():
# 	kit_body = get_kit_body(12)
# 	response = sender_stand_request.post_new_user(kit_body)
# 	assert response.status_code == 400
