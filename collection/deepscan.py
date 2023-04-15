import json
import nmap
from threat.device import Device

# Takes a list of network devices
# Performs a deep port scan and appends the findings to a new Device object
# Return list of Devices
def scan_open_ports(devices):

    # Provide the path to nmap executable and create a new scanner
    nmap_path = [r"C:\Program Files (x86)\Nmap\Nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)

    # Perform a port scan on each device, appending the data to scans list
    scans = []
    found_devices = []
    for device in devices:
        print("scanning " + device)
        scans.append(nm.scan(
            hosts=device, arguments="-T4 -A -v -p1-65535"))

    # For each scan result, create a device object using the data from the scan
    for each in scans:

        # Get the addresses
        device_name = list(each["scan"].keys())[0]
        ip_address = each["scan"][device_name]["addresses"].get(
            "ipv4", None)
        mac_address = each["scan"][device_name]["addresses"].get(
            "mac", None)

        # Create a Device object with the scan data
        device = Device(ip_address, mac=mac_address)

        # Convert any 'osmatch' found in the scan into a cpe 
        try:
            open_ports = each["scan"][ip_address]["tcp"].keys()
            for port in open_ports:
                if (each["scan"][ip_address]["tcp"][port].get("cpe") != ''):
                    device.add_cpe(convert_osmatch_to_cpe(each["scan"][ip_address].get("osmatch")))
        except KeyError:
            pass

        found_devices.append(device)

    return found_devices

def convert_osmatch_to_cpe(osmatch):
    vendor = osmatch[0]["osclass"][0].get("vendor").lower()
    osfamily = osmatch[0]["osclass"][0].get("osfamily").lower()
    osgen = osmatch[0]["osclass"][0].get("osgen")
    cpe = f"{vendor}:{osfamily}:{osgen}"
    return cpe