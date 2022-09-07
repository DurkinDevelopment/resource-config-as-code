import string

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

def open_and_append(path_to_file, content):
   with open(path_to_file, "a") as file:
      file.write('\n%s\n' % content)
      file.close()

def write_to_file(env, resource_type, content):
   path_to_file = generate_path_of_file_to_write_to(env, resource_type)
   open_and_append(path_to_file, content)    