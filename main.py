import json
from collection.hostscan import scan_network_devices
from collection.deepscan import scan_open_ports
from threat.fetch_vulnerability import get_vulnerabilities

dev_list = scan_open_ports(scan_network_devices("10.10.10.10"))
get_vulnerabilities(dev_list)

for index in range(len(dev_list)):
    print(f"\nip: {dev_list[index].ip}\nmac: {dev_list[index].mac}\ncpes: {dev_list[index].get_cpe_list()}\ncves: {dev_list[index].get_cve_list()}")