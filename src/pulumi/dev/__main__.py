"""A Python Pulumi program"""

import json
import pulumi
import pulumi_datadog as datadog


foo = datadog.Monitor("foo",
    escalation_message="Escalation message @pagerduty",
    include_tags=True,
    message="Monitor triggered. Notify: @hipchat-channel",
    monitor_thresholds=datadog.MonitorMonitorThresholdsArgs(
        critical="4",
        warning="2",
    ),
    name="Name for monitor foo",
    query="avg(last_1h):avg:aws.ec2.cpu{environment:foo,host:foo} by {host} > 4",
    tags=[
        "foo:bar",
        "team:fooBar",
    ],
    type="metric alert")
    

monitor_json_kzssp = datadog.MonitorJson("monitorJson", monitor="""{
        "name": "monitor_json_kzssp",
        "type": "service check",
        "query": "\"ntp.in_sync\".by(\"*\").last(2).count_by_status()",
        "message": "Change the message triggers if any host's clock goes out of sync with the time given by NTP. The offset threshold is configured in the Agent's 'ntp.yaml' file.

See [Troubleshooting NTP Offset issues](https://docs.datadoghq.com/agent/troubleshooting/ntp for more details on cause and resolution.",
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
    }""")
