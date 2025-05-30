from calculator import Calculator
def main():
    calc = Calculator()


    print('OOP Calculator')
    print('Enter operator')

    op = input('Select operator')
    if op not in ['+','-','/','*']:
        print('Invalid operation')
        return
    
    try:
        num1 = float(input('Select first number: '))
        num2 = float(input('Select second number: '))
    except ValueError:
        print("Invalid input. Please enter number")
        return

    if op == '+':
        result = calc.add(num1,num2)
    elif op == '-':
        result = calc.sub(num1,num2)
    elif op == '/':
        result = calc.divide(num1,num2)
    elif op == '*':
        result = calc.multiply(num1,num2)
    
    print(result)

if __name__ == "__main__":
    main()