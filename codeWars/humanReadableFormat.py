def format_duration(seconds):
    # If seconds is zero, return 'now'
    if seconds == 0:
        return "now"

    # Define the time units and their equivalent values in seconds
    time_units = [
        ('year', 365 * 24 * 60 * 60),  # 1 year = 365 days
        ('day', 24 * 60 * 60),  # 1 day = 24 hours
        ('hour', 60 * 60),  # 1 hour = 60 minutes
        ('minute', 60),  # 1 minute = 60 seconds
        ('second', 1)  # 1 second
    ]

    # List to store each time component in the result
    result = []

    # Loop through each time unit and calculate its value
    for unit, unit_seconds in time_units:
        if seconds >= unit_seconds:
            value = seconds // unit_seconds
            seconds %= unit_seconds
            # Append the formatted string with singular or plural form
            result.append(f"{value} {unit}" + ("s" if value > 1 else ""))

    # If there's more than one component, join them with commas and "and"
    if len(result) > 1:
        return ", ".join(result[:-1]) + " and " + result[-1]

    # If there's only one component, return it directly
    return result[0]


# Test cases
print(format_duration(62))  # "1 minute and 2 seconds"
print(format_duration(3662))  # "1 hour, 1 minute and 2 seconds"
print(format_duration(0))  # "now"

