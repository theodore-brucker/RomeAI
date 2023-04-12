class Device:
    def __init__(self, ip, vendor=None, product=None, version=None):
        self.ip = ip
        self.vendor = vendor
        self.product = product
        self.version = version
        self.cve_list = []

    def set_vendor(self, vendor):
        self.vendor = vendor

    def set_product(self, product):
        self.product = product

    def set_version(self, version):
        self.version = version

    def set_isVulnerable(self, bool):
        self.isVulnerable = bool

    def add_cve(self, cve_id):
        self.cve_list.append(cve_id)

    def fetch_cve_list(self):
        return self.cve_list