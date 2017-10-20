import ui
import math

def factorial(sender):
	user_input = int(view['number_input'].text)
	num = 1
	for i in range(1, user_input + 1):
		num = num * i
		view['factorial_label'].text = str(num)
		
view = ui.load_view()
view.present('sheet')
