# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def create_argument_dictionary(**kwargs):
    argument_dictionary = {}

    for arg_name, arg_value in kwargs.items():
        if not isinstance(arg_value, (str, int, float, bool)):
            arg_value = str(arg_value)

        argument_dictionary[arg_value] = arg_name

    return argument_dictionary

# Вызов функции с ключевыми аргументами
result = create_argument_dictionary(name="Alice", age=25, country="USA", married=True, favorite_color="blue")

# Вывод результата
for key, value in result.items():
    print(f"{key}: {value}")
