from ncclient import manager
import xml.dom.minidom

router = {
    "host": "192.168.3.108",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}

hostname_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>Arevalo-Hernandez-Leiva-Valdebenito</hostname>
  </native>
</config>
"""

with manager.connect(**router) as m:
    netconf_reply = m.edit_config(target="running", config=hostname_config)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
