def find_value(values, match):
    if len(values) == 0:
        print(f"Значение {match} не найдено!")
    else:
        if values[0] == match:
            print(f"Значение {match} найдено!")
        else:
            values.pop(0)
            print(values)
            find_value(values, match)

find_value(['pink', 'green'], 'yellow')