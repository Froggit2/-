def matem(operation_1):
    if operation_1 == "add_1":
        def suma(z, y):
            return z + y

        return "add_1"
    elif operation_1 == "-":
        def minus(z, y):
            return z - y

        return "-"


my_number = matem("add_1")
print(my_number(1, 2))



def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y

        return add  # возвращаем функцию как объект!! Тут скобки не нужны
    elif operation == "subtract":
        def subtract(x, y):
            return x - y

        return subtract


my_func_add = create_operation("add")
print(my_func_add(1, 2))
