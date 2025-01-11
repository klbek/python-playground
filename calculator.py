def calculate(operator, number1, number2):
    match operator:
        case 1: 
            return number1 + number2 
        case 2:
            return number1 - number2 
        case 3:
            return number1 / number2 
        case 4:
            return number1 * number2 
        case _:
            return "invalid input"


user_response = input("Choose an operator and enter two numbers, separate by a space:\n1 -> +\n2 -> -\n3 -> :\n4 -> *\n").split(" ")
user_response = [int(i) for i in user_response]
operator, number1, number2 = user_response
print(calculate(operator, number1, number2))
