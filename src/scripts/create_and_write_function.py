import sys
from monitors.module import Monitor
from utils.helper_methods import write_to_file

def main(env, resource_type, json_input):
    Monitor().create_definition()
    write_to_file(env, resource_type, content)

if __name__ == "__main__":
    env = sys.argv[1]
    resource_type = sys.argv[2]
    json_input = sys.argv[3]
    main(env, resource_type, json_input)