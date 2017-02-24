def fizzBuzz(n):
	if n % 15 == 0:
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Fizz'
	elif n % 5 == 0:
		return 'Buzz'
	else:
		return str(n)

def get_chatbot_response(message):
    if message[:2] == '!!':
        return 'Woosh'
    else:
        return 'Not a command'