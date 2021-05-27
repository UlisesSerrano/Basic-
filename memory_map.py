# Memory Map for Virtual Machine
class Memory:
    def __init__(self):
        self.addresses = {}

    def set_value(self, value, address):
        self.addresses[address] = value

    def get_value(self, address):
        if address in self.addresses:
            return self.addresses[address]
        print("ERROR: Address not found", address, self.addresses)
    
    def get_values(self):
        return self.addresses
