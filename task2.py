def task(x1,y1,x2,y2,x3,y3,x4,y4):
    _x1 = None
    _x2 = None
    _y1 = None
    _y2 = None

    #normalization
    rec1x1 = min(x1, x2)
    rec1x2 = max(x1, x2)
    rec1y1 = min(y1, y2)
    rec1y2 = max(y1, y2)

    rec2x1 = min(x3, x4)
    rec2x2 = max(x3, x4)
    rec2y1 = min(y3, y4)
    rec2y2 = max(y3, y4)

    if (rec1x1 <= rec2x1 <= rec1x2):
        _x1 = rec2x1

    if (rec1x1 <= rec2x2 <= rec1x2):
        _x2 = rec2x2

    if (rec2x1 <= rec1x1 <= rec2x2):
        _x1 = rec1x1

    if (rec2x1 <= rec1x2 <= rec2x2):
        _x2 = rec1x2

    if (rec1y1 <= rec2y1 <= rec1y2):
        _y1 = rec2y1

    if (rec1y1 <= rec2y2 <= rec1y2):
        _y2 = rec2y2

    if (rec2y1 <= rec1y1 <= rec2y2):
        _y1 = rec1y1

    if (rec2y1 <= rec1y2 <= rec2y2):
        _y2 = rec1y2

    res = (_x1 != None and _x2 != None and _y1 != None and _y2 != None)
    if not res:
        return res
    else:
        return [res, abs(_x2-_x1)*abs(_y2-_y1)]

'''
Функция возвращает False, если прямоугольники не пересекаются.
Если же пересекаются, то возвращается список, где первый элемент это True, а второй площадь пересечения.
'''

print(task(0,0,10,10,1,1,4,4))
print(task(1,1,2,2,3,3,4,4))
