def times(str):
    for c in str:
        alien[c] = alien.get(c, 0) + 1
    for key, value in alien.items():
        print(key, value)
alien = {}
times("asdfgasd")