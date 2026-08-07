import math

station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]


def get_average(temps):
    return sum(temps) / len(temps)


def get_deviation(temps):
    mean = get_average(temps)

    total = 0

    for temperature in temps:
        total += (temperature - mean) ** 2

    variance = total / len(temps)
    deviation = math.sqrt(variance)

    return deviation


# by Rahul Rimal

def get_summary(temps):
    average = get_average(temps)
    deviation = get_deviation(temps)

    print("Weather Station:", station_name)
    print("Minimum Temperature:", min(temps), "°C")
    print("Maximum Temperature:", max(temps), "°C")
    print("Average Temperature:", round(average, 2), "°C")
    print("Standard Deviation:", round(deviation, 2), "°C")


get_summary(temperatures)

try:
    print(mean)
except NameError:
    print("NameError: 'mean' is a local variable inside get_deviation().")

    