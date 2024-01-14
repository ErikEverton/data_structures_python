class HashMap(object):
    def __init__(self, size) -> None:
        self.data = [[]] * (size)
    
    def _hash(self, key):
        hash_value = 0

        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        
        return hash_value
    
    def set(self, key, value):
        address = self._hash(key)

        if not self.data[address]:
            self.data[address] = []
        self.data[address].append(key, value)
        return self.data

    
