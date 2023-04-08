from collection.hosts import scan_network_devices
from collection.ports import scan_open_ports


scan_open_ports(scan_network_devices("10.3.32.0"))