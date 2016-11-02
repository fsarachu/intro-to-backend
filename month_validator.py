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


def main():
    for k, v in month_abbreviations.items():
        print k + ': ' + v


if __name__ == '__main__':
    main()
