import data
import sender_stand_request

#   Long variables for tests
symbol511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


#   Getting a product’s body kit
def get_kit_body(name):
	current_kit_body = data.kit_body.copy()
	current_kit_body["name"] = name
	return current_kit_body


#   Positive assertion
def positive_assertion(name):
	kit_body_positive = get_kit_body(name)
	kit_response = sender_stand_request.post_new_client_kit(kit_body_positive, sender_stand_request.auth_token)
	assert kit_response.json()["name"] == name
	assert kit_response.status_code == 201


#   Negative assertion
def negative_assertion(name):
	kit_body_negative = get_kit_body(name)
	kit_response = sender_stand_request.post_new_client_kit(kit_body_negative, sender_stand_request.auth_token)
	assert kit_response.status_code == 400


#   Positive tests
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assertion("a")


def test_create_kit_511_symbols_in_name_get_success_response():
	positive_assertion(symbol511)


def test_create_kit_english_letters_in_name_get_success_response():
	positive_assertion("QWErty")


def test_create_kit_russian_letters_in_name_get_success_response():
	positive_assertion("Мария")


def test_create_kit_has_special_symbols_in_name_get_success_response():
	positive_assertion("\"№%@\",")


def test_create_kit_has_space_in_name_get_success_response():
	positive_assertion("Человек и КО")


def test_create_kit_has_number_in_name_get_success_response():
	positive_assertion("123")


#   Negative tests
def test_create_kit_empty_name_get_error_response():
	negative_assertion("")


def test_create_kit_512_symbols_in_name_get_error_response():
	negative_assertion(symbol512)


def test_create_kit_no_name_get_error_response():
	current_kit_body_negative = data.kit_body.copy()
	#   Deleting “name” from a query
	current_kit_body_negative.pop("name")
	negative_assertion(current_kit_body_negative)


def test_create_kit_numeric_type_name_get_error_response():
	negative_assertion(123)
