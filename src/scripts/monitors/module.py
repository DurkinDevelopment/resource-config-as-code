from utils import helper_methods
from monitors import template

class Monitor:
    def create_definition(self):
        name = self.create_name(5)
        template = self.create_template(name)
        definition = "%s = %s" % (name, template)
        return definition
    def create_template(self, name = "Example monitor - service check"):
        return template.MONITOR % name
    def create_name(self, length):
        prefix = helper_methods.randomword(length)
        return "monitor_json_%s" % prefix

