import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block with difficulty: {difficulty}")
        start_time = time.time()

        target = '0' * difficulty
        attempts = 0

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1

        end_time = time.time()

        print(f"Block mined!")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        print(f"Final Hash: {self.hash}")

# Example
difficulty = 4  
block = Block(1, "Some transaction data", "0")
block.mine_block(difficulty)
