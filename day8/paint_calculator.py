import math


def paint_calculator(height, width, coverage = 5):
    surface = height * width
    number_of_cans = math.ceil(surface/coverage)
    print(f"You need to buy {number_of_cans} cans of paint")


wall_height = float(input(f"Enter the height of the wall: "))
wall_width = float(input(f"Enter the width of the wall: "))
cover = int(input(f"Enter the coverage of the wall: "))
paint_calculator(wall_height, wall_width, cover)