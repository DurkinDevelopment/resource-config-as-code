from ...utils.helper_methods import randomword
import template

class Monitor:
    def create_definition(self):
        name = create_name(5)
        template = create_template(name)
        definition = "%s = %s" % (name, template)
        return definition
    def create_template(self, name = "Example monitor - service check"):
        return template.MONITOR % name
    def create_name(self, length):
        prefix = randomword(length)
        return "monitor_json_%s" % prefix

