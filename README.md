# Blockchain

## Task Description
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.
https://video.udacity-data.com/topher/2019/April/5ca8bd1d_untitled-diagram/untitled-diagram.png

## Explanation
Implemented a linked list containing a node block and a pointer which point to the next block. When new data is added, new hash is created with appropriate timestamp. At the same time, information regarding the previous block is also stored. 
Then, the new block is added to the blockchain. 

Appending data, timestamp and previous block information to a fresh block makes the time and space complexity Big O(n)