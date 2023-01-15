def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start(s):
        i = index(s)
        if s[i] == '0':
            return False
        if s.isalpha() or s[i:len(s)].isdigit():
            return True
    return False


def start(s):
    if s.isalnum():
        if 2 <= len(s) <= 6 and s[0:2].isalpha():
            return True
    return False


def index(s):
    i = 0
    for char in s:
        if char.isalpha() and i < len(s) - 1:
            i += 1
        else:
            break
    return i

if __name__ == "__main__":
    main()