#!usr/bin/env python
import subprocess
import re
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result :
        print("New MAC Address : " + mac_address_search_result.group(0))
    else :
        print("[-] Sorry Could not Find the MAC Address")

interface = raw_input("Interface >")
new_mac = raw_input ("New MAC >")

change_mac(interface, new_mac)
get_current_mac(interface)

print ("Made By S.M Proud to be a Muslim")