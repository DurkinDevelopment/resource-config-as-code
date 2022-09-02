"""A monitor resource for using pulumi's datadog integration"""

import pulumi
import pulumi_datadog as datadog

# How to create an array of input properties to pass into args?
@overload
def Monitor(resource_name: str,
            args: MonitorArgs,
            opts: Optional[ResourceOptions] = None)


def MonitorArgs()
    return {
        escalation_message: Optional[str] = None,
        include_tags: Optional[bool] = None,
        locked: Optional[bool] = None,
        message: Optional[str] = None,
        monitor_thresholds: Optional[MonitorMonitorThresholdsArgs] = None,
        name: Optional[str] = None,
        query: Optional[str] = None,
        tags: Optional[Sequence[str]] = None,
        type: Optional[str] = None
    }

    monitor = datadog.Monitor("my-monitor")

pulumi.export("monitor", monitor.name)

# Can I use this file for all pulumi functions?
# Can I read from dev / prod based on pulumi up command and read all files and their functions?
# Remove any args that aren't necessary / required

class MonitorClass(self):
    def __init__(self):
        enable_logs_sample: Optional[bool] = None,
        escalation_message: Optional[str] = None,
        evaluation_delay: Optional[int] = None,
        force_delete: Optional[bool] = None,
        groupby_simple_monitor: Optional[bool] = None,
        include_tags: Optional[bool] = None,
        locked: Optional[bool] = None,
        message: Optional[str] = None,
        monitor_threshold_windows: Optional[MonitorMonitorThresholdWindowsArgs] = None,
        monitor_thresholds: Optional[MonitorMonitorThresholdsArgs] = None,
        name: Optional[str] = None,
        new_group_delay: Optional[int] = None,
        new_host_delay: Optional[int] = None,
        no_data_timeframe: Optional[int] = None,
        notify_audit: Optional[bool] = None,
        notify_no_data: Optional[bool] = None,
        priority: Optional[int] = None,
        query: Optional[str] = None,
        renotify_interval: Optional[int] = None,
        renotify_occurrences: Optional[int] = None,
        renotify_statuses: Optional[Sequence[str]] = None,
        require_full_window: Optional[bool] = None,
        restricted_roles: Optional[Sequence[str]] = None,
        tags: Optional[Sequence[str]] = None,
        timeout_h: Optional[int] = None,
        type: Optional[str] = None,
        validate: Optional[bool] = None)


@overload
def Monitor(resource_name: str,
            opts: Optional[ResourceOptions] = None,
            enable_logs_sample: Optional[bool] = None,
            escalation_message: Optional[str] = None,
            evaluation_delay: Optional[int] = None,
            force_delete: Optional[bool] = None,
            groupby_simple_monitor: Optional[bool] = None,
            include_tags: Optional[bool] = None,
            locked: Optional[bool] = None,
            message: Optional[str] = None,
            monitor_threshold_windows: Optional[MonitorMonitorThresholdWindowsArgs] = None,
            monitor_thresholds: Optional[MonitorMonitorThresholdsArgs] = None,
            name: Optional[str] = None,
            new_group_delay: Optional[int] = None,
            new_host_delay: Optional[int] = None,
            no_data_timeframe: Optional[int] = None,
            notify_audit: Optional[bool] = None,
            notify_no_data: Optional[bool] = None,
            priority: Optional[int] = None,
            query: Optional[str] = None,
            renotify_interval: Optional[int] = None,
            renotify_occurrences: Optional[int] = None,
            renotify_statuses: Optional[Sequence[str]] = None,
            require_full_window: Optional[bool] = None,
            restricted_roles: Optional[Sequence[str]] = None,
            tags: Optional[Sequence[str]] = None,
            timeout_h: Optional[int] = None,
            type: Optional[str] = None,
            validate: Optional[bool] = None)
@overload
def Monitor(resource_name: str,
            args: MonitorArgs,
            opts: Optional[ResourceOptions] = None)