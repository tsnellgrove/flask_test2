test_lst = []

def func_test(base):
	full_line = base + ", Burt"
	return full_line

def do_calculation(color, test_lst):
	game_over = False
	color = color.lower()
	if color == 'red':
		buffer = 'like an apple'
	elif color == 'yellow':
		buffer = 'like the sun'
	elif color == 'blue':
		buffer= 'like the ocean'
	elif color == 'blank':
		buffer = "Enter a primary color"
	elif color == 'quit':
		buffer = 'goodbye!'
		game_over = True
	else:
		buffer = 'what was that?'
	buffer = func_test(buffer)
	test_lst.append(color)
	return buffer, game_over, test_lst

#test_string = ['red', 'yellow', 'blue', 'xxyyz', 'quit']

#for value in test_string:
#	buffer, game_over, test_lst = do_calculation(value, test_lst)
#	print("The test response to " + value + " is {}".format(buffer))
#	print("The game_over value is " + str(game_over))
#	print(test_lst)

