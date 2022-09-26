def same_by(characteristic, objects):
    result, result1 = [], []
    for i in objects:
        if characteristic(i) == 0:
            result.append(i)
        else:
            result1.append(i)            
    if result == objects or result1 == objects:
        return True
    return False

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

same_by(lambda x: x % 2, values)
