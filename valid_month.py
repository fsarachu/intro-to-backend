months = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
)

month_abbreviations = {m[:3].lower(): m for m in months}

for k, v in month_abbreviations.items():
    print k + ': ' + v
