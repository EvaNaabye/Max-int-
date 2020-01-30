north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

total_cars = north_int + west_int + south_int + east_int

while total_cars > 0:
    if (north_int + south_int) >= (east_int + west_int):
        print("Green lights on N/S")
        if north_int >= 0 and north_int < 5:
            total_cars -= north_int
            north_int = 0
        else:
            total_cars -= 5
            north_int -= 5

        if south_int >= 0 and south_int < 5:
            total_cars -= south_int
            south_int = 0
        else:
            total_cars -= 5
            south_int -= 5

    if (east_int + west_int) > (north_int + south_int):
        print("Green lights on E/W")
        if east_int >= 0 and east_int < 5:
            total_cars -= east_int
            east_int = 0
        else:
            total_cars -= 5
            east_int -= 5

        if west_int >= 0 and west_int < 5:
            total_cars -= west_int
            west_int = 0
        else:
            total_cars -= 5
            west_int -= 5

    if total_cars <= 0:
        print("No cars waiting, the traffic jam has been solved!")
        break