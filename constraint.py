class Constraint:

    def __init__(self, check_function):
        self.check_function = check_function

    def check(self, neighbors, value):
        return self.check_function(neighbors, value)
