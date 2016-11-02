from datetime import datetime


class YearValidator:
    min_year = 1900
    max_year = datetime.now().year


def main():
    print 'min_year: {}'.format(YearValidator.min_year)
    print 'max_year: {}'.format(YearValidator.max_year)


if __name__ == '__main__':
    main()
