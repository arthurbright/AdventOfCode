pairs = [
    (7, 4),
    (7, 6),
    (7, 5),
    (5, 3),
    (6, 1),
    (7, 5),
    (0, 4),
    (4, 3),
    (4, 7),
    (6, 1),
    (7, 4),
    (6, 5),
    (4, 7),
    (3, 2),
    (6, 1)
]

offset = 7
for a, b in pairs:
    a = (a + offset) % 8
    b = (b + offset) % 8
    a, b = b, a

    code = 8 * a + b
    print(chr(code + ord('A')))