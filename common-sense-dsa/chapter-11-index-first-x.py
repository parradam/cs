def index_first_x(str, index=0):
    if str[0] == "x":
        return 0
    return 1 + index_first_x(str[1:])


str = "abcdefghijklmnopqrstuvwxyz"

print(index_first_x(str))

# This assumes that there is always at least one "x" in the string
