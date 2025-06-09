import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False

            if curr.previous_hash != prev.hash:
                return False

        return True
    
# Creating a blockchain
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, time.time(), "Block 1 Data", ""))
my_blockchain.add_block(Block(2, time.time(), "Block 2 Data", ""))

print("Original Blockchain:")
my_blockchain.display_chain()
print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")

# Tampering with block 1's data
my_blockchain.chain[1].data = "Hacked Block 1 Data"
my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()  

print("\nAfter Tampering with Block 1:")
my_blockchain.display_chain()
print(f"The blockchain is valid: {my_blockchain.is_chain_valid()}") 

# Fixing the entire chain manually
for i in range(1, len(my_blockchain.chain)):
    my_blockchain.chain[i].previous_hash = my_blockchain.chain[i - 1].hash
    my_blockchain.chain[i].hash = my_blockchain.chain[i].calculate_hash()

print("\nAfter Recalculating Hashes:")
my_blockchain.display_chain()
print(f"The blockchain is valid: {my_blockchain.is_chain_valid()}")