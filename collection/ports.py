import nmap

def scan_open_ports(devices):

    #Provide the path to nmap executable and create a new scanner
    nmap_path = [r"C:\Program Files (x86)\Nmap\Nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)

    #Perform a port scan on each device, appending the data to the scans list
    scans = []
    for device in devices:
        print("scanning " + device)
        scans.append(nm.scan(
            hosts=device, arguments="-sS -T5 -p 1-1024 --min-rate=5000 --max-retries=2"))

    print("Host information:")
    for scan in scans:
        for ip, host in scan['scan'].items():
            print(f"\tIP: {ip}")
            print(f"\tHostname: {host['hostnames'][0]['name']}")
            if 'mac' in scan:
                print(f"\tMAC Address: {host['addresses']['mac']}")
            else:
                print("\tNo mac address found.")

            if 'tcp' in host:
                for port, port_info in host['tcp'].items():
                    print(f"\tPort: {port}")
                    print(f"\t\tState: {port_info['state']}")
                    print(f"\t\tService: {port_info['name']}")
                    print(f"\t\tProduct: {port_info['product']}")
                    print(f"\t\tVersion: {port_info['version']}")
                    print(f"\t\tExtra Info: {port_info['extrainfo']}")
            else:
                print("\tNo open ports found.")
            print("\n\n")
