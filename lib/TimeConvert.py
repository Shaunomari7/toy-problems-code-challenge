#!/usr/bin/env python3


def convert_to_24_hour(hour, minute, period):
    
    # Check if the period is "pm" and the hour is not 12
    if period == "pm" and hour != 12:
        # If so, add 12 to the hour
        hour += 12
    # Check if the period is "am" and the hour is 12
    elif period == "am" and hour == 12:
        # If so, set the hour to 0 (midnight)
        hour = 0
    # Return the converted time as a string, with hour and minute zero-padded
    return f"{hour:02d}{minute:02d}"

print(convert_to_24_hour(11, 30, "am")) 
print(convert_to_24_hour(7, 30, "pm")) 