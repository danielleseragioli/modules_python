def ft_water_reminder():
    lastWatering = int(input("Days since last watering: "))
    if lastWatering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
