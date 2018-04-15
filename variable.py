class Variable:

    def __init__(self):
        self.value = None
        self.domain = None

    def set_variable_domain(self, domain):
        self.domain = domain

    def set_variable_value(self, value):
        self.value = value
