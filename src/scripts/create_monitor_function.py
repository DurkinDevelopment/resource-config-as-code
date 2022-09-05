import sys
import random
import string


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

monitor_json_template = """datadog.MonitorJson(\"monitorJson\", monitor=\"\"\"{
    "name": "%s",
    "type": "service check",
    "query": "\"ntp.in_sync\".by(\"*\").last(2).count_by_status()",
    "message": "Change the message triggers if any host's clock goes out of sync with the time given by NTP. The offset threshold is configured in the Agent's 'ntp.yaml' file.\n\nSee [Troubleshooting NTP Offset issues](https://docs.datadoghq.com/agent/troubleshooting/ntp for more details on cause and resolution.",
    "tags": [],
    "multi": true,
	"restricted_roles": null,
    "options": {
        "include_tags": true,
        "locked": false,
        "new_host_delay": 150,
        "notify_audit": false,
        "notify_no_data": false,
        "thresholds": {
            "warning": 1,
            "ok": 1,
            "critical": 1
        }
    },
    "priority": null,
    "classification": "custom"
}
\"\"\")"""

def generate_monitor_json():
    prefix = randomword(5)
    monitor_name = "monitor_json_%s" % prefix
    updated_monitor_json = monitor_json_template % monitor_name
    generated_monitor_json = "%s = %s" % (monitor_name, updated_monitor_json)
    return generated_monitor_json

def main(json_input):
    return generate_monitor_json()
    
  
# Using the special variable 
# __name__
if __name__=="__main__":
    generated_monitor_json = main(sys.argv[1])
    print(generated_monitor_json)