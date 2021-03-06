# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        res = []
        for item in items:
            if args[0] in item.keys():
                res.append(item[args[0]])
        print(res)
    else:
        for item in items:
            res = dict()
            for key in args:
                if key in item.keys():
                    res[key] = item[key]
            print(res)
       

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

if __name__ == "__main__":
    field(goods, 'title')
    field(goods, 'title', 'price')