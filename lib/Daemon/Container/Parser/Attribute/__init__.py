

class Attribute():

    attr_enabled = False
    attr_value = None
    attr_descr = None

    def __init__(self, name):
        pass

    def enabled(self, value = None):
        if value is not None:
            self.attr_enabled = value if value is True else False
        return self.attr_enabled

    def value(self, value = None):
        if value is not None:
            self.attr_value = value if value is not None else None
        return self.attr_value

    def description(self, value = None):
        if value is not None:
            self.attr_descr = value if value is not None else None
        return self.attr_descr

    def validate(self):
        pass
