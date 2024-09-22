# Calculator Functions 
def add (x, y):
    return x + y

def subtract(x, y):
    return x - y

def division (x,y):
    return x / y

def multiplication (x,y):
    if y == 0:
        return "Error! Division by zero."
    return x * y

# we take the input from the user 
def get_numbers():
    num1 =  float(input ("Enter your first number : ") )
    num2 =  float(input("Enter your second number : "))
    return num1, num2

# operations 
def select_operation():
    print ("select an operation : ")
    print ("1. + Addition")
    print ("2. - Subtraction")
    print ("3. / Division")
    print ("4. * Multiplication")
    choice = input ("Enter choice (+ ,- ,* ,/ )")
    return choice 


def Calculator ():
    while True :
        operation = select_operation()
        if operation in ['+', '-' ,'/' ,'*'  ]:
           
            num1 ,num2 = get_numbers()
            if operation == '+':
                print (f"{num1} + {num2} = {add(num1,num2)}")
            elif operation == '-':
                print (f"{num1} - {num2} = {subtract(num1,num2)}")
            elif operation == '*':
                print (f"{num1} * {num2} = {multiplication(num1,num2)}")
            elif operation == '/':
                print (f"{num1} / {num2} = {division(num1,num2)}")
        else:
            print ("invalid operation! please try again .")

        again = input("Do you wan tto perform another calculation? (yes/no) : ").lower
        if again != 'yes':
            print ('Good bye ')
            break
Calculator()