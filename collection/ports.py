import nmap
import json

def scan_open_ports(devices):

    #Provide the path to nmap executable and create a new scanner
    nmap_path = [r"C:\Program Files (x86)\Nmap\Nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)

    #Perform a port scan on each device, appending the data to the scans list
    scans = []
    for device in devices:
        print("scanning " + device)
        scans.append(nm.scan(
            hosts=device, arguments="-T4 -A -v -p1-65535"))

    for each in scans:
        print(json.dumps(each, indent=4))
