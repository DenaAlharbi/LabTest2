# Dena Alharbi 202250560 F78

def isValid(PIN):
    if len(PIN) != 4:
        return False
    if not PIN.isdigit():
        return False
    for i in range(len(PIN)):
        if PIN[i] in PIN[0:i]:
            # print(f"{PIN[i]} is repeated") --Just to check if it works
            return False
        if PIN[i] in PIN[i + 1:]:
            # print(f"{PIN[i]} is repeated") --Just to check if it works
            return False

    return True


def main():
    PIN = input("Enter PIN (4 different digits): ")
    while not isValid(PIN):
        PIN = input("Invalid, re-enter PIN (4 different digits): ")
    print("PIN is valid")


main()
