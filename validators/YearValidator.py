from datetime import datetime


class YearValidator:
    def __init__(self):
        pass

    min_year = 1900
    max_year = datetime.now().year

    @staticmethod
    def validate(year):
        try:
            num_year = int(year)
        except ValueError as e:
            return None
        else:
            if YearValidator.min_year <= num_year <= YearValidator.max_year:
                return num_year
            else:
                return None


def main():
    print 'min_year: {}'.format(YearValidator.min_year)
    print 'max_year: {}'.format(YearValidator.max_year)

    print "\n--- Test Validations ---"
    print 'validate(\'2016\'): {}'.format(YearValidator.validate('2016'))
    print 'validate(\'  2016   \'): {}'.format(YearValidator.validate('  2016   '))
    print 'validate(2016): {}'.format(YearValidator.validate(2016))
    print 'validate(\'asdklas\'): {}'.format(YearValidator.validate('asdklas'))
    print 'validate(\'1900\'): {}'.format(YearValidator.validate('1900'))
    print 'validate(\'1996\'): {}'.format(YearValidator.validate('1996'))
    print 'validate(\'1820\'): {}'.format(YearValidator.validate('1820'))
    print 'validate(\'2017\'): {}'.format(YearValidator.validate('2017'))


if __name__ == '__main__':
    main()
