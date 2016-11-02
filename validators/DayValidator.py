class DayValidator:
    def __init__(self):
        pass

    min_day = 1
    max_day = 31

    @staticmethod
    def validate(day):
        """Validates if its a number between 1 and 31. Returns the day as an int if valid, else None"""
        if day and day.isdigit():
            num_day = int(day)
            if 1 <= num_day <= 31:
                return num_day
            else:
                return None
        else:
            return None


def main():
    print '\n--- Days ---'
    print 'min_day: {}'.format(DayValidator.min_day)
    print 'max_day: {}'.format(DayValidator.max_day)

    print '\n--- Test Validations ---'
    print 'validate(\'23\'): {}'.format(DayValidator.validate('23'))
    print 'validate(\'34\'): {}'.format(DayValidator.validate('34'))
    print 'validate(\'0\'): {}'.format(DayValidator.validate('0'))


if __name__ == '__main__':
    main()
