# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegistryStatistics(Model):
    """RegistryStatistics.

    :param total_device_count:
    :type total_device_count: long
    :param enabled_device_count:
    :type enabled_device_count: long
    :param disabled_device_count:
    :type disabled_device_count: long
    """

    _attribute_map = {
        "total_device_count": {"key": "totalDeviceCount", "type": "long"},
        "enabled_device_count": {"key": "enabledDeviceCount", "type": "long"},
        "disabled_device_count": {"key": "disabledDeviceCount", "type": "long"},
    }

    def __init__(
        self, total_device_count=None, enabled_device_count=None, disabled_device_count=None
    ):
        super(RegistryStatistics, self).__init__()
        self.total_device_count = total_device_count
        self.enabled_device_count = enabled_device_count
        self.disabled_device_count = disabled_device_count
