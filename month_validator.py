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


def valid_month(month):
    month = month.capitalize()
    if month in months:
        return month
    else:
        return None


def main():
    print valid_month('january')
    print valid_month('some junk')
    print valid_month('AUGUST')


if __name__ == '__main__':
    main()
