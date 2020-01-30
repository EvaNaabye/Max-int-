north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

total_cars = north_int + west_int + south_int + east_int

while total_cars > 0:
    if (north_int + south_int) >= (east_int + west_int):
        print("Green lights on N/S")
        north_int -= 5
        south_int -= 5
    total_cars -= (north_int - south_int)

    if (east_int + west_int) > (north_int + south_int):
        print("Green lights on E/W")
        east_int -= 5
        west_int -= 5
    total_cars -= (west_int - east_int)

    if total_cars <= 0:
        print("No cars waiting, the traffic jam has been solved!")
        break