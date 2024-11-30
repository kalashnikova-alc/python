import math


def circle_length(radius):
    return 2 * math.pi * radius


def circle_area(radius):
    return math.pi * radius ** 2


def main():
    r1 = float(input("Введіть радіус першого кола: "))
    r2 = float(input("Введіть радіус другого кола: "))
    r3 = float(input("Введіть радіус третього кола: "))

    c1 = circle_length(r1)
    c2 = circle_length(r2)
    c3 = circle_length(r3)
    total_length = c1 + c2 + c3

    s1 = circle_area(r1)
    s2 = circle_area(r2)
    s3 = circle_area(r3)
    total_area = s1 + s2 + s3

    print("Сума довжин кіл:", total_length)
    print("Сума площ кругів:", total_area)


main()


def circle_properties(radius):
    length = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return length, area


def main():
    r1 = float(input("Введіть радіус першого кола: "))
    r2 = float(input("Введіть радіус другого кола: "))
    r3 = float(input("Введіть радіус третього кола: "))

    c1, s1 = circle_properties(r1)
    c2, s2 = circle_properties(r2)
    c3, s3 = circle_properties(r3)

    total_length = c1 + c2 + c3
    total_area = s1 + s2 + s3

    print("Сума довжин кіл:", total_length)
    print("Сума площ кругів:", total_area)


main()
