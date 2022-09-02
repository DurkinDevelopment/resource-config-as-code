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