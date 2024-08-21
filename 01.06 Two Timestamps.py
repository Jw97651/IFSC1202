def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

hours1 = int(input("Enter the number of hours for the first timestamp: "))
minutes1 = int(input("Enter the number of minutes for the first timestamp: "))
seconds1 = int(input("Enter the number of seconds for the first timestamp: "))
hours2 = int(input("Enter the number of hours for the second timestamp: "))
minutes2 = int(input("Enter the number of minutes for the second timestamp: "))
seconds2 = int(input("Enter the number of seconds for the second timestamp: "))
seconds1_total = time_to_seconds(hours1, minutes1, seconds1)
seconds2_total = time_to_seconds(hours2, minutes2, seconds2)
difference = seconds2_total - seconds1_total
print("The number of seconds between the two timestamps is " + str(difference) + ".")