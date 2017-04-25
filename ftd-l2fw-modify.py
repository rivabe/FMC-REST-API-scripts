#!/usr/bin/env python
################################################################################
#                                                                              #
# Copyright (c) 2017 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License"); you may   #
#    not use this file except in compliance with the License. You may obtain   #
#    a copy of the License at                                                  #
#                                                                              #
#         http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################
from device_script import serviceModify


ldevid = 1234
interface1 = 'GigabitEthernet0/1'
interface2 = 'GigabitEthernet0/2'
ifname1 = 'appnic'
ifname2 = 'dbnic'
vlan1 = 1500
vlan2 = 1501
zone1 = 'web-zone'
zone2 = 'app-zone'
bvi_ip = '10.1.0.1/16'

policy_name = 'ftd-policy'
rule1_name = 'ftd-rule1'
rule1_bidir = 'true'

rule2_name = 'ftd-rule2'
rule2_bidir = 'true'

ftd_ip = "10.0.0.25"
fmc_ip = "10.0.0.30"
username = "apiuser"
password = "cisco"
virtual = False
bvi_id = 1

config_dev = {
   "dn": "uni/tn-pod54/lDevVip-ftd-5525-L2FW",
   "name": "ftd-5525-L2FW",
   "virtual": virtual,
   "devs": {
      "Device1": {
         "dn": "uni/tn-pod54/lDevVip-ftd-5525-L2FW/cDev-Device1",
         "state": 3,
         "host": ftd_ip,
         "virtual": virtual,
         "version": "6.2.0 (build 362)",
         "port": 443,
         "creds": {
            "username": username,
            "password": password
         }
      }
   },
   "host": fmc_ip,
   "contextaware": False,
   "port": 443,
   "creds": {
        "username": username,
        "password": password
   }
}

config = {
   (0, '', 4915): {
      'dn': "uni/vDev-[uni/tn-pod54/lDevVip-ftd-5525-L2FW]-tn-[uni/tn-pod54]-ctx-pod54net",
      'transaction': 0,
      'ackedstate': 0,
      'value': {
         (8, '', 'ftd-5525-L2FW_web-nic_3014658_16392'): {
            'state': 3,
            'transaction': 0,
            'vif': "ftd-5525-L2FW_web-nic",
            'ackedstate': 0,
            'encap': "3014658_16392"
         },
         (7, '', '3014658_49157'): {
            'transaction': 0,
            'ackedstate': 0,
            'state': 3,
            'tag': vlan2,
            'type': 1
         },
         (4, 'SecurityZone', zone2): {
            'state': 3,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'type', 'type'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "SWITCHED"
               }
            }
         },
         (4, 'BridgeGroupInterface', 'BVI1'): {
            'state': 3,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'bridge_group_id', 'BridgeGroupId'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': bvi_id
               },
               (4, 'Interfaces', 'Interfaces'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'Interface', 'ExternalInterface'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InterfaceHolder', 'InterfaceHolder'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "externalInterface",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'Interface', 'InternalInterface'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InterfaceHolder', 'InterfaceHolder'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "internalInterface",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               },
               (4, 'IPv4Config', 'IPv4Config'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'static', 'static'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (5, 'address', 'address'): {
                              'state': 3,
                              'transaction': 0,
                              'ackedstate': 0,
                              'value': bvi_ip
                           }
                        }
                     }
                  }
               }
            }
         },
         (10, '', 'ftd-5525-L2FW_app-nic'): {
            'state': 3,
            'transaction': 0,
            'cifs': {
               'Device1': interface2
            },
            'ackedstate': 0
         },
         (4, 'AccessPolicy', policy_name): {
            'state': 3,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (4, 'AccessRule', rule1_name): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'AccDestinationZones', 'AccDestinationZones'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'DestinationZones', 'DestinationZone'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "internalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     },
                     (5, 'bidirectional', 'Bi-Directional'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': rule1_bidir
                     },
                     (4, 'AccSourceZones', 'AccSourceZones'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'SourceZones', 'SourceZone'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "externalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               },
               (4, 'AccessRule', rule2_name): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (5, 'bidirectional', 'bidirectional'): {
                        'state': 3,
                        'transaction': 1,
                        'ackedstate': 0,
                        'value': rule2_bidir
                     },
                     (4, 'AccDestinationZones', 'AccDestinationZones'): {
                        'state': 3,
                        'transaction': 1,
                        'ackedstate': 0,
                        'value': {
                           (6, 'DestinationZones', 'DestinationZones'): {
                              'state': 3,
                              'transaction': 1,
                              'target': "externalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'AccSourceZones', 'AccSourceZones'): {
                        'state': 3,
                        'transaction': 1,
                        'ackedstate': 0,
                        'value': {
                           (6, 'SourceZones', 'SourceZones'): {
                              'state': 3,
                              'transaction': 1,
                              'target': "internalInterface/int_security_zone",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               }
            }
         },
         (10, '', 'ftd-5525-L2FW_web-nic'): {
            'state': 3,
            'transaction': 0,
            'cifs': {
               'Device1': interface1
            },
            'ackedstate': 0
         },
         (8, '', 'ftd-5525-L2FW_app-nic_3014658_49157'): {
            'state': 3,
            'transaction': 0,
            'vif': "ftd-5525-L2FW_app-nic",
            'ackedstate': 0,
            'encap': "3014658_49157"
         },
         (4, 'SecurityZone', zone1): {
            'state': 3,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'type', 'type'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "SWITCHED"
               }
            }
         },
         (1, '', 5791): {
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (3, 'FTD', 'N1'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (4, 'AccessPolicyFolder', 'AccessPolicyFolder'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InAccessPolicyRel', 'InAccessPolicyRel'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "ftd-policy",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'ExIntfConfigRelFolder', 'ExtConfig'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'ExIntfConfigRel', 'ExtConfigrel'): {
                              'connector': "consumer",
                              'state': 3,
                              'transaction': 0,
                              'target': "externalInterface",
                              'ackedstate': 0
                           }
                        }
                     },
                     (2, 'external', 'consumer'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (9, '', 'ftd-5525-L2FW_web-nic_3014658_16392'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "ftd-5525-L2FW_web-nic_3014658_16392",
                              'ackedstate': 0
                           }
                        }
                     },
                     (2, 'internal', 'provider'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (9, '', 'ftd-5525-L2FW_app-nic_3014658_49157'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "ftd-5525-L2FW_app-nic_3014658_49157",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'BridgeInterfaceFolder', 'BridgeInterfaceFolder'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InBridgeGroupInterfaceRel', 'InBridgeGroupInterfaceRel'): {
                              'state': 3,
                              'transaction': 0,
                              'target': "BVI1",
                              'ackedstate': 0
                           }
                        }
                     },
                     (4, 'InIntfConfigRelFolder', 'IntConfig'): {
                        'state': 3,
                        'transaction': 0,
                        'ackedstate': 0,
                        'value': {
                           (6, 'InIntfConfigRel', 'InConfigrel'): {
                              'connector': "provider",
                              'state': 3,
                              'transaction': 0,
                              'target': "internalInterface",
                              'ackedstate': 0
                           }
                        }
                     }
                  }
               }
            },
            'state': 3,
            'absGraph': "ftd-l2fw-graph",
            'rn': "vGrp-[uni/tn-pod54/GraphInst_C-[uni/tn-pod54/brc-web-to-app2]-G-[uni/tn-pod54/AbsGraph-ftd-l2fw-graph]-S-[uni/tn-pod54]]"
         },
         (4, 'InterfaceConfig', 'externalInterface'): {
            'state': 3,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'ifname', 'ifname'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': ifname1
               },
               (5, 'enabled', 'enabled'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "true"
               },
               (4, 'int_security_zone', 'int_security_zone'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (6, 'security_zone', 'security_zone'): {
                        'state': 3,
                        'transaction': 0,
                        'target': "web-zone",
                        'ackedstate': 0
                     }
                  }
               }
            }
         },
         (4, 'InterfaceConfig', 'internalInterface'): {
            'state': 3,
            'transaction': 0,
            'ackedstate': 0,
            'value': {
               (5, 'ifname', 'ifname'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': ifname2
               },
               (5, 'enabled', 'enabled'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': "true"
               },
               (4, 'int_security_zone', 'int_security_zone'): {
                  'state': 3,
                  'transaction': 0,
                  'ackedstate': 0,
                  'value': {
                     (6, 'security_zone', 'security_zone'): {
                        'state': 3,
                        'transaction': 0,
                        'target': "app-zone",
                        'ackedstate': 0
                     }
                  }
               }
            }
         },
         (7, '', '3014658_16392'): {
            'transaction': 0,
            'ackedstate': 0,
            'state': 2,
            'tag': vlan1,
            'type': 1
         }
      },
      'txid': 10000,
      'tagPackets': False,
      'state': 3,
      'ctxName': "pod54net",
      'tenant': "pod54"
   }
}


serviceModify (config_dev,config)
