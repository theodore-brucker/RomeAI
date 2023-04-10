from collection.hosts import scan_network_devices
from collection.ports import scan_open_ports
from threat.fetch_vulnerability import get_vulnerabilities


#scan_open_ports(scan_network_devices("10.10.10.10"))
#get_vulnerabilities('microsoft', 'windows_10')