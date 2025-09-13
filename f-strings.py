number = 42
pyvers = 3.6
array = [1, 2, 3]
print(f"{number=}")
print(f"{number:_>8}")
print(f"{number:_<8}")
floatnum = 3.14

print(f"{floatnum:0<8}")
print(f"{floatnum:.0f}")

year = 2024
month = 9
day = 2

print(f"{year=}-{month:02}-{day:02}")


p = 20.123

m = 1_000_000_000
print(f"{m:}")