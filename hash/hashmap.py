class HashMap(object):
    def __init__(self, size) -> None:
        self.data = [[]] * (size)
    
    def _hash(self, key):
        hash_value = 0

        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        
        return hash_value
    
    

