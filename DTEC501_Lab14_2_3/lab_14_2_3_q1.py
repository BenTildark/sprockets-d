"""
Given the change in CBD driving speeds, you need to find the closest recorded speed when compared to the speed limit.

Write a function called find_nearest_speed.

find_nearest_speed has two parameters

recorded_speeds
speed_limit
recorded_speeds is a list of integers containing the recorded speeds.

speed_limit is an integer which is the maximum speed on that stretch of road.

The function find_nearest_speed returns an integer which is the speed that is closest to the speed limit.

Hints.

Iterate through the list of speeds looking at the difference each time.
The difference can be found using slide 23 of presentation 2-2.
To make the scenario easier, if two values have equal difference, return the last most value.
The solution is 8 lines of code including the def and return lines.

Example test code
max_speed = 30
speed_data = [24, 25, 27, 28, 31, 35]
closest_speed = find_nearest_speed(speed_data, max_speed)
print("The closest recorded speed was {} Km/h.".format(closest_speed))

The closest recorded speed was 31 Km/h.

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Lab: 14 2 3 Q1


def find_nearest_speed(recorded_speeds, speed_limit):

    """Find the closed speed to the speed limit"""
    # Use the built-in min() function, to find the element which has the minimum distance from the speed limit.
    return min(recorded_speeds, key=lambda x: abs(x-speed_limit))


max_speed = 30
speed_data = [24, 25, 27, 28, 31, 35]
closest_speed = find_nearest_speed(speed_data, max_speed)
print("The closest recorded speed was {} Km/h.".format(closest_speed))
