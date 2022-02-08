def Precedence_Order(opd):
	if opd == '+' or opd == '-':
		return 1
	if opd == '*' or opd == '/':
		return 2
	return 0

def Operation(num1, num2, opd):
	if opd == '+': return num1 + num2
	if opd == '-': return num1 - num2
	if opd == '*': return num1 * num2
	if opd == '/': return num1 // num2

def Evaluate(expression):
	values = []
	ops = []
	i = 0

	while i < len(expression):
		if expression[i] == ' ':
			i += 1
			continue
		
		elif expression[i] == '(':
			ops.append(expression[i])

		elif expression[i].isdigit():
			val = 0

			while (i < len(expression) and expression[i].isdigit()):
				val = (val * 10) + int(expression[i])
				i += 1

			values.append(val)
			i -= 1
		
		elif expression[i] == ')':
			while len(ops) != 0 and ops[-1] != '(':
				val2 = values.pop()
				val1 = values.pop()
				opd = ops.pop()

				values.append(Operation(val1, val2, opd))
			ops.pop()

		else:
			while (len(ops) != 0 and Precedence_Order(ops[-1]) >= Precedence_Order(expression[i])):
				val2 = values.pop()
				val1 = values.pop()
				opd = ops.pop()

				values.append(Operation(val1, val2, opd))
			
			ops.append(expression[i])
		i += 1
	
	while len(ops) != 0:
		val2 = values.pop()
		val1 = values.pop()
		opd = ops.pop()

		values.append(Operation(val1, val2, opd))

	return values[-1]
	
if __name__ == "__main__":
	# Your code goes here
	pass
	print(Evaluate('121*(5-1)/11'))
	print(Evaluate('100 * (2+12)'))
	print(Evaluate('85/23-16'))
