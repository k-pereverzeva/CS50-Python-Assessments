def main():
    fraction = input("Fraction: ")
    procent = gauge(convert(fraction))
    print(procent)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            procent = round(x/y * 100)
            if x > y:
                raise ValueError()
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return procent


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
