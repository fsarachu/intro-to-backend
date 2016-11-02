class DayValidator:
    def __init__(self):
        pass

    days = (
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thurdsday',
        'Friday',
        'Saturday',
        'Sunday'
    )

    day_abbvs = [day[:3].lower() for day in days]
