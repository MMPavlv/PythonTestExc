'''
В задании приведен пример, что при входных данных '111111111110000000000000000' ответ будет 10,
что не соответствует самой формулировке задачи. Всего единиц 11, то есть, индекс первого нуля будет тоже 11, так как индексация
начинается с нуля. Не понятно, как мог взяться ответ 10. Решение использует встроенный метод find(), который возвращает
первую позицию вхождения подстроки в строку.
'''


def task(array):
    return array.find('0')

print(task("111111111110000000000000000"))
