def levels_from_string(string):
    ''' Converts strings into a list of Levels. Can handle strings like:
            -- 'K.AA,1.BB,2.BB,3.CC'
            -- '[K.AA, 1.BB, 2.BB, 3.CC]'

    Convenient function for testing
    '''
    string = string.translate(None, '[]')
    return [Level(x.split('.')[0].strip(), x.split('.')[1].strip()) for
            x in string.split(',')]


class Level(object):
    '''
    A grade and domain combination.

    For example, 1.RL -- 1st grade Reading Literature -- can be represented
    as a single object.

    Grade can be any number, 'K', or None. Internally they are represented as
    integers.
    '''
    def __init__(self, grade, domain):
        if grade == 'K' or grade == 'k':
            grade = 0
        if grade is None or grade == "None" or grade == "":
            grade = -1
        self.grade = int(grade)
        self.domain = domain

    def __str__(self):
        grade = self.grade
        if grade == 0:
            grade = 'K'
        if grade == -1:
            grade = None
        return "{}.{}".format(grade, self.domain)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.grade == other.grade and self.domain == other.domain
