# FLOWCHARTS
import sys

msg_= {0: "Enter an equation",
        1: "Do you even know what numbers are? Stay focused!",
        2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        3: "Yeah... division by zero. Smart move...",
        4: "Do you want to store the result? (y / n):",
        5: "Do you want to continue calculations? (y / n):",
        6: " ... lazy",
        7: " ... very lazy",
        8: " ... very, very lazy",
        9: "You are",
        10: "Are you sure? It is only one digit! (y / n)",
        11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
        12: "Last chance! Do you really want to embarrass yourself? (y / n)"}

memory = 0.0

def askq():
    global calc, x, y, oper
    calc = input(f"{msg_[0]} \n")
    x, oper, y = calc.split(" ")
    return

def checknum():
    global x, y, oper
    if x == "M":
        x = memory
    elif x.isalpha():
        print(msg_[1])
        input_checks()

    if y == "M":
        y = memory
    elif y.isalpha():
        print(msg_[1])
        input_checks()
    return

def operation_check():
    global x, y, oper
    if oper not in ['+', '-', '*', '/']:
        print(msg_[2])
        input_checks()
    else:
        x = float(x)
        y = float(y)
        return

def is_one_digit(v):
    global x, y, oper
    if -10 < v < 10 and v % 1 == 0:
        return True
    else:
        return False


def lazy_calc_check():
    global x, y, oper
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg_[6]
    if x == 1 or y == 1 and oper == "*":
        msg = msg + msg_[7]
    if x == 0 or y == 0 and oper != "/":
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)
    return

# result is calculated
def calc_result():  
    global x, y, oper, result
    result = 0.0
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    elif oper == "/" and y == 0:
        print(msg_[3])
        calculator()
    return

def input_checks():
    askq()
    checknum()
    operation_check()
    lazy_calc_check()
    

def calculator():
    global memory
    input_checks()
    calc_result()
    
    print(result)

    print(msg_[4])
    store_it  = input()
    if store_it == "n":
        pass
    elif store_it == 'y' and is_one_digit(result) is False:
        memory = result
    elif store_it == 'y' and is_one_digit(result):
        counter = 0
        response = 'y'
        #  asks if user really wants to store such a small number
        while True:
            print(msg_[10 + counter])
            response = input()
            if response == "n":
                break
            elif response == "y" and counter < 2:
                counter += 1
            else:
                memory = result
                break
        

    print(msg_[5])
    more_calcs  = input()
    if more_calcs == 'y':
        calculator()
    else:
        sys.exit()

calculator()