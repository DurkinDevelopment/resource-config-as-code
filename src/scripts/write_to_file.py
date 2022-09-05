import sys

# Take in the input from the create_monitor_function script to write to the file
# Take in the input for the dev or prod directory
# Take in the input for the resource type directory

# Add in dynamic file name (standardized naming convention)

# This assumes that the file directory will be accessed from the scripts directory

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def generate_file_name(env, resource_type):
    random_prefix = randomword(5)
    file_name = "%s_%s_%s.py" % (env, resource_type, random_prefix)

def generate_path_of_file_to_write_to(env, resource_type):
    ## code for writing to a new file
    # path_to_file = "../pulumi/%s/resources/custom/%s/%s" % (env, resource_type)
    ## code for writing to the main file
    path_to_file = "/home/runner/work/resource-config-as-code/resource-config-as-code/src/pulumi/%s/__main__.py" % env
    return path_to_file

def write_to_file(path_to_file, content):
    with open(path_to_file, "a") as file:
        file.write('\n%s\n' % content)
        file.close()

def main(env, resource_type, content):
    path_to_file = generate_path_of_file_to_write_to(env, resource_type)
    write_to_file(path_to_file, content)    

if __name__ == "__main__":
    env = sys.argv[1]
    resource_type = sys.argv[2]
    content = sys.argv[3]
    main(env, resource_type, content)