class Device:
    #Constructor for Device requires at LEAST an IP, any other missing data will default to None
    def __init__(self, ip, mac=None):
        self.ip = ip
        self.mac = mac
        self.vendor = ''
        self.product = ''
        self.version = ''
        self.cpe_list = []
        self.cve_list = []

    #setters for the CPE identification data
    def set_vendor(self, vendor):
        self.vendor = vendor
    def set_product(self, product):
        self.product = product
    def set_version(self, version):
        self.version = version

    #getters for the CPE identification data
    def get_vendor(self):
        return self.vendor
    def get_product(self):
        return self.product
    def get_version(self):
        return self.version

    #set or get if this device is considered vulnerable
    def set_isVulnerable(self, bool):
        self.isVulnerable = bool
    def get_isVulnerable(self):
        return self.isVulnerable

    #add to or get the list of cpe's found for a single host
    def add_cpe(self, cpe):
        self.cpe_list.append(cpe)
    def add_cpe_list(self, cpe_list):
        self.cpe_list = cpe_list
    def get_cpe_list(self):
        return self.cpe_list

    #add to or get the list of cve's that a device is vulnerable too
    def add_cve(self, cve_id):
        self.cve_list.append(cve_id)
    def add_cve_list(self, cve_list):
        self.cve_list = cve_list
    def get_cve_list(self):
        return self.cve_list
    
    