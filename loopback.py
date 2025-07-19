from ncclient import manager
import xml.dom.minidom

router = {
    "host": "192.168.3.108",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}

netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>11</name>
    <description>loopback creada con NETCONF</description>
    <ip>
     <address>
      <primary>
       <address>11.11.11.11</address>
       <mask>255.255.255.255</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

with manager.connect(**router) as m:
    netconf_reply = m.edit_config(target="running", config=netconf_loopback)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
