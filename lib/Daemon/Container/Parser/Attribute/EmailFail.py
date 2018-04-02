from lib.Daemon.Container.Parser.Attribute import Attribute

class EmailFail(Attribute):
    def validate(self):
        if super(self).enabled() and str(super(self).value()).strip() == "":
            raise Exception("email_fail attribute error")

