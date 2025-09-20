from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import Basic, PowerConfiguration, Identify
from zigpy.zcl.clusters.security import IasZone
from zhaquirks import Bus
from zhaquirks.tuya import TuyaManufCluster

class TuyaZG102Z(CustomDevice):
    signature = {
        'models_info': [('HOBEIAN', 'ZG-102Z')],
        'endpoints': {
            1: {
                'profile_id': 0x0104,
                'device_type': 0x0402,
                'input_clusters': [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    IasZone.cluster_id,
                    0xEF00,  # Tuya manufacturer specific
                ],
                'output_clusters': [],
            },
        },
    }
    replacement = {
        'endpoints': {
            1: {
                'profile_id': 0x0104,
                'device_type': 0x0402,
                'input_clusters': [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    IasZone.cluster_id,
                    TuyaManufCluster.cluster_id,  # Hersteller-spezifischer Cluster mit Tuya-Quirk
                ],
                'output_clusters': [],
            },
        },
    }
