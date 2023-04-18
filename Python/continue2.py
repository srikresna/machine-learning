total_line = 10
_line = 0
star = 0
while _line < total_line:
    if (star) >= (_line+1):
        print()
        _line = _line+1
        star = 0
        continue      # Saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*", end="")
    star = star+1