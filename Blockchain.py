import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')
                    + str(self.timestamp).encode('utf-8'))
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return f'\nBlockHash: {self.hash}\n Timestamp: {self.timestamp}\n Data: {self.data}\n Previous Hash:' \
               f'{self.previous_hash}\n '


class Node:
    def __init__(self, data, previous_hash):
        self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
        self.next = None
        self.tail = None


class BlockChain:
    def __init__(self):
        self.tail = None
        self.head = None

    def append(self, data=None):
        if data is None:
            print("Block is Empty!")
            return

        if not self.head:
            self.head = Node(data, None)
            self.tail = self.head


        else:
            self.tail.next = Node(data, self.tail.block.hash)
            self.tail = self.tail.next

    def __str__(self):
        if self.head is None:
            return "Block Chain is empty"

        current_node = self.head
        result = str()
        while current_node:
            result += str(current_node.block)
            current_node = current_node.next
        return result


# Test 1
block_chain = BlockChain()
print("\nTest 1")
block_chain.append("Bitcoin")
block_chain.append("Dogecoin")
block_chain.append("Ethereum")

current_block = block_chain.head

print(current_block.block)  # Should print the first block

current_block = current_block.next
print(current_block.block)  # Should print the second block

current_block = current_block.next
print(current_block.block)  # Should print the third block

# Test 2
block_chain = BlockChain()
print("\nTest 2")
print(block_chain)  # Should print empty blockchain message

# Test 3
print("\nTest 3")
block_chain = BlockChain()

block_chain.append()
block_chain.append("Meowcoin")

print(block_chain)  # Should print 1 empty blockchain message and 1 filled blockchain
