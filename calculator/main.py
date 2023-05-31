def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Here the add for example is calling the function add
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("First Number : "))
num2 = int(input("Second Number : "))
# print on screen all items on operations dictionary
for i in operations:
    print(i)
operation_symbol = input("Type the operator : ")

# With the operation_symbol variable, we are telling that the calculation_function is like for example , operations[
# +], and if it's +, it will call the function add.
calculation_function = operations[operation_symbol]

# calculation_function here called the add function and it will sum the 2 numbers.
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Type another operator : ")
num3 = int(input("Third Number : "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(answer, num3)

print(f"{answer} {operation_symbol} {num3} = {second_answer}")
