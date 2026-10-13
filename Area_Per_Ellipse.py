#!/usr/bin/envpython3
# Created By:Deepak
# Date: 09/26/2026
# This program asks the user for the area and perimeter of a Ellipse


def main():
    # get the semi-major axis from the user
    a = float(input("Enter the semi-major axis of the ellipse (cm): "))

    # get the semi-minor axis from the user
    b = float(input("Enter the semi-minor axis of the ellipse (cm): "))

    # calculate the area and perimeter of an ellipse
    area = math.pi * a * b
    perimeter = math.pi * (3 * (a + b) - ((3 * a + b) * (a + 3 * b)) ** 0.5)

    # display the area and perimeter to the user with proper units
    print("The area is: {:.2f}cm²".format(area))
    print("The perimeter is: {:.2f}cm".format(perimeter))


if __name__ == "__main__":
    main()
