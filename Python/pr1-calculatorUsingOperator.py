# calculator using operators:

print("""calculator using operators\nfor addition : +\nfor subtraction : - \nfor multiplication : * \nfor division : / \nfor modulo : % \nfor flor division : // \nfor exponent : **\n\n""");

print("Enter first number:")
firstNum = int(input());
print("Enter second nummber:");
secNum = int(input());
print("Enter operator: ");
operator = input();

if(operator == '+'):
    print("sum of a and b :", firstNum + secNum);
elif operator == '-':
    print("difference of a and b :", firstNum - secNum);
elif operator == '*':
    print("product of a and b :", firstNum * secNum);
elif operator == '/':
    print("division of a and b :", firstNum / secNum);
elif operator == '%':
    print("modulo of a and b :", firstNum % secNum);
elif operator == '//':
    print("flor division of a and b :", firstNum // secNum);

print("Run the program again to perform another operation");


