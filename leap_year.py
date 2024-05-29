def leap(nbre):
    year=int(nbre)
    if (year%400 == 0):
        return "LEAP"
    elif (year%4==0 and year%100!=0):
        return "LEAP"
    else:
        return "NOPE"

if __name__ == '__main__':
    year=int(input("Enter a year: "))
    print(leap(year))
