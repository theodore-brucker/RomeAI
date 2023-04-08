import nmap

def scan_network_devices(network):
    
    #Provide the path to nmap executable and create a new scanner
    nmap_path = [r"C:\Program Files (x86)\Nmap\Nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)

    #Run a -sn scan on the network and store any live hosts in devices list
    nm.scan(hosts=f"{network}/24", arguments="-sn")
    devices = []
    for host in nm.all_hosts():
        if nm[host]['status']['state'] == 'up':
            devices.append(host)
            print(f"found host on {host}")
    return devices


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

    #Print the data collected from scan for each device
    for device in scans:
        # Print out the host information
        print("\nHost information:")
        for value in device['scan'].items():
            for subkey, subvalue in value.items():
                if subkey == 'addresses':
                    print(f"\t{subkey}:")
                    for addrkey, addrvalue in subvalue.items():
                        print(f"\t\t{addrkey}: {addrvalue}")


scan_open_ports(scan_network_devices("10.3.32.0"))
