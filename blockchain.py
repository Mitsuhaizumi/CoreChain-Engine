import hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.create_hash()

    def create_hash(self):
        return hashlib.sha256((self.data + self.prev_hash).encode()).hexdigest()
