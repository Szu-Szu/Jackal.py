import time
import json
from hashlib import sha3_512
from merkletools import MerkleTools

# Read the tree.json file
with open("benchmark/tree.json", "r") as file:
    raw_tree = file.read()

total = 5
total_time = 0

for i in range(total):
    start_time = int(time.time() * 1e6)  
    for _ in range(100):
       
        leaves = json.loads(raw_tree)
        mt = MerkleTools(hash_type="sha3_512")
        for leaf in leaves:
            mt.add_leaf(leaf, True)
        mt.make_tree()
    end_time = int(time.time() * 1e6) 
    elapsed_time = end_time - start_time
    total_time += elapsed_time
    print(f"Took: {elapsed_time} microseconds.")

average_time = total_time // total
print(f"Took: {average_time} microseconds on average.")

