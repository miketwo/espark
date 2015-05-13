class Student(object):
    def __init__(self, name, levels_list):
        '''
        ARGS
            name - the kid's name
            levels_list -- a list of Level objects representing the current
                           knowledge of the student. For example, a list of
                           [2.RF, 2.RL, K.RI] means the student tested at the
                           2nd grade level in Reading Foundations and Reading
                           Literature, but she's struggling at the Kindergarten
                           level in Reading Informational Text.
        '''
        self.name = name
        self.levels = levels_list

    def __str__(self):
        return "{} ==> {}".format(self.name, str(self.levels))

    def __repr__(self):
        return str(self.__dict__)

    def path(self, domain_order, number=5):
        ''' Calculates the path forward for this student

        ARGS
            student -- Student Object
            domain_order -- a list of Level objects, the order of which
                            specifies the complete education path from start
                            to finish
            number -- maximum number of  steps in the calculated path to return
        '''
        # Make a copy of domains so we don't mess with the original
        a = domain_order[:]
        # For each level of the student, remove all lower levels.
        # What remains will be the path forward for the student.
        for lvl in self.levels:
            a = filter(lambda x: not (lvl.domain == x.domain and
                                      x.grade < lvl.grade), a)
        return a[:number]
