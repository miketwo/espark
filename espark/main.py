'''
Library for espark functions
'''
from itertools import chain


def creates_paths(student_file, domain_order):
    students = create_students_from_csv(student_file)
    levels = create_ordering_from_csv(domain_order)
    result = []
    for student in students:
        path = calculate_path(student, levels)
        pathstr = ",".join(str(p) for p in path)
        result.append("{},{}".format(student.name, pathstr))
    return result


def make_levels(string):
    ''' Converts a string like 'K.AA,1.BB,2.BB,3.CC' into a list of Levels '''
    return [Level(x.split('.')[0], x.split('.')[1]) for x in string.split(',')]


def create_students_from_csv(csv_file):
    ''' Convert a csv file into a list of Student objects '''
    students = []
    with open(csv_file, 'r') as f:
        firstline = f.readline().strip()
        domains = firstline.split(',')[1:]
        for line in f:
            linelist = line.strip().split(',')
            name = linelist[0]
            grades = linelist[1:]
            levels = [Level(*t) for t in zip(grades, domains)]
            students.append(Student(name, levels))
    return students

def create_ordering_from_csv(csv_file):
    ''' Convert a csv file into a list of Levels '''
    levels = []
    with open(csv_file, 'r') as f:
        for line in f:
            linelist = line.strip().split(',')
            grade = linelist[0]
            for domain in linelist[1:]:
                levels.append(Level(grade, domain))
    return levels


def calculate_path(student, levels, number=5):
    ''' Calculates the path forward for a student

    ARGS
        student -- Student Object
        levels -- a list of Level objects, the order of which specifies
                  the complete path from new student to graduate
        number -- how many steps in the calculated path to return
    '''
    a = levels[:]  # make a copy so we don't mess with the original
    # For each level of the student, remove all levels underneath
    # Todo: make more efficient
    for lvl in student.levels:
        a = filter(lambda x: not (lvl.domain == x.domain and x.grade < lvl.grade), a)
    return a[:number]


class Student(object):
    def __init__(self, name, levels_list):
        # levels_list -- a list of Level objects
        self.name = name
        self.levels = levels_list

    def __str__(self):
        return "{} ==> {}".format(self.name, str(self.levels))

    def __repr__(self):
        return str(self.__dict__)


class Level(object):
    def __init__(self, grade, domain):
        if grade == 'K' or grade == 'k':
            grade = 0
        self.grade = int(grade)
        self.domain = domain

    def __str__(self):
        grade = self.grade
        if grade == 0:
            grade = 'K'
        return "{}.{}".format(grade, self.domain)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.domain == other.domain:
            return self.grade == other.grade
        else:
            return False

    def __hash__(self):
        return hash((self.grade, self.domain))

    def lower_levels(self):
        ''' Creates a list of all levels lower than the self object '''
        return [Level(i, self.domain) for i in range(self.grade)]


# Deprecated below ---------------------

def fast_filter(student_levels, levels):
    stuff = chain.from_iterable([lvl.lower_levels() for lvl in student_levels])
    s = set(stuff)
    return [x for x in levels if x not in s]
