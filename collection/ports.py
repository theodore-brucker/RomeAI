import nmap
import json

from threat.device import Device

def scan_open_ports(devices):

    #Provide the path to nmap executable and create a new scanner
    nmap_path = [r"C:\Program Files (x86)\Nmap\Nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)

    #Perform a port scan on each device, appending the data to the scans list
    scans = []
    found_devices = []
    for device in devices:
        print("scanning " + device)
        scans.append(nm.scan(
            hosts=device, arguments="-T4 -A -v -p1-100"))

    #For each scan result, create a device object using the data from the scan
    for each in scans:
        ip_address = list(each["scan"].keys())[0]
        ip_address_value = each["scan"][ip_address]["addresses"]["ipv4"]
        device = Device(ip_address_value)
        found_devices.append(device)