import sys
import random
import string
from monitors.module import Monitor

def generate_monitor_json():
    return Monitor().create_definition()

def main(json_input):
    return generate_monitor_json()
    
  
# Using the special variable 
# __name__
if __name__=="__main__":
    generated_monitor_json = main(sys.argv[1])
    print(generated_monitor_json)