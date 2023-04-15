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