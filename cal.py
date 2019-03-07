x, oper, y = input().split()
result = {
        'plus' : int(x)+int(y),
        'minus' :int(x)-int(y)
        }
print(result.get(oper, "Invalid Operator"))
