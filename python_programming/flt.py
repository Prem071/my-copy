








numbers_ = [[10,20,30],
            50, [20,10], "Tokyo",[20]
            ]
for i in numbers_:

    if type(i) == int:
        print(i)

    else:
        for j in i:
            print(j)

