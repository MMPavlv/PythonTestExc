def interval_duration(inter):
    sm = 0
    
    for i in range(0, len(inter), 2):
        sm += inter[i+1]-inter[i]
    return sm

def interval_intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    active_1 = False
    active_2 = False
    left = None
    right = None
    result = []
    while(len(arr1) > 0 and len(arr2) > 0):
        if arr1[0] < arr2[0]:
            if not active_2:
                left = None
                arr1.pop(0)
            if not active_1 and active_2:
                left = arr1.pop(0)
            if active_1 and active_2:
                right = arr1.pop(0)

            active_1 = not active_1
        else:
            if not active_1:
                left = None
                arr2.pop(0)
            if active_1 and not active_2:
                left = arr2.pop(0)
            if active_1 and active_2:
                right = arr2.pop(0)
            active_2 = not active_2

        if (left != None and right != None):
            result.append(left)
            result.append(right)
            left = None
            right = None
    return result

def appearance(intervals):
    res1 = interval_intersection(intervals['lesson'], intervals['pupil'])
    res2 = interval_intersection(res1, intervals['tutor'])

    return interval_duration(res2)

'''
Логично предположить, что значения таймстепмов в каждом списке должны только возрастать:
[начало_интервала_1, конец_интервала_1, начало_интервала_2, конец_интервала_2...]
Каждый интервал начинается только после конца предыдущего. Однако во втором примере интервалы присутствия ученика не просто
расположены непоследовательно, но и накладываются друг на друга, что логически невозможно. Для этого я в функции, находящей
пересечение интервалов, сортирую их. И тогда ответ для второго примера будет 397, а не 3577, как сказано в задании.
'''

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil':   [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor':   [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil':   [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor':   [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 397
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil':   [1594692033, 1594696347],
             'tutor':   [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       print(test_answer)
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
