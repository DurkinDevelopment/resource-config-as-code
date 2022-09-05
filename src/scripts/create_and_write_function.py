import sys
import create_monitor_function
import write_to_file

def main(env, resource_type, json_input):
    content = create_monitor_function.main(json_input)
    write_to_file.main(env, resource_type, content)

if __name__ == "__main__":
    env = sys.argv[1]
    resource_type = sys.argv[2]
    json_input = sys.argv[3]
    main(env, resource_type, json_input)