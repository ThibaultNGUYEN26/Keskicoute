CHAR_LIMIT = 10
USERNAME_CHAR_LIMIT = 15

def validate_length(new_value):
	return len(new_value) <= USERNAME_CHAR_LIMIT

def validate_float(new_value):
	if len(new_value) > CHAR_LIMIT:
		return False
	if new_value == "" or new_value == ".":
		return True
	try:
		float(new_value)
		if '.' in new_value:
			decimal_part = new_value.split('.')[1]
			if len(decimal_part) > 2:
				return False
		return True
	except ValueError:
		return False
