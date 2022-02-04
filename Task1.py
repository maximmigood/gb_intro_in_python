lst = [7,
       12,
       4.3,
       'Батарейка',
       7,
       .0,
       ['33', 33, .7],
       (12, 1, '77'),
       {3: 12, 4: 13, 5: 14},
       False,
       None,
       False,
       b'Hello, ',
       [1, 2, 3, 4],
       complex(1, 2),
       bytearray(b'Python'),
       {3, 2, 3, 2, 4}]
for e in lst:
    # print(type(e))
    if type(e) == type(None):
        print(e)
