#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 3, 2022
# This program calculates the volume
# and surface area of a torus


# import torus_constants
import math


def main():
    # input
    print("This program calculates the volume")
    print("and surface area of a torus.")
    print("")
    print("Note: the tube radius cannot be bigger than")
    print("the radius of revolution, as that would result")
    print("in an impossible shape :)")
    print("")
    tube_rad = int(input("Enter the torus's tube radius in inches: "))
    rad_of_rev = int(input("Enter the torus's radius of revolution in inches: "))

    # process
    # calculating volume
    volume = math.pi * math.pi * 2 * (tube_rad * tube_rad) * rad_of_rev

    # calculating surface area
    surface_area = math.pi * math.pi * 4 * tube_rad * rad_of_rev

    # output
    # to round to two decimals: :,.2f
    print("")
    print("Your volume is {:,.2f} inches^3.".format(volume))
    print("Your surface area is {:,.2f} inches^2.".format(surface_area))
    # print("Also PI * PI = {}".format(math.pi * math.pi))


if __name__ == "__main__":
    main()
