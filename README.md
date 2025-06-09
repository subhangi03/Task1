# CONSOLE OUTPUTS:
## BLOCKCHAIN SIMULATION (3 linked blocks):

```plaintext
Original Blockchain:
Index: 0
Timestamp: 1749444913.769553
Data: Genesis Block
Previous Hash: 0
Hash: 6a5944b808164772f3d50834f1beeef03bfdca803635caeaa729212a1e1c139f
Nonce: 0

Index: 1
Timestamp: 1749444913.770672
Data: Block 1 Data
Previous Hash: 6a5944b808164772f3d50834f1beeef03bfdca803635caeaa729212a1e1c139f
Hash: 0000e8a0a099915a1def6e4a6ee1778fb83abb3b26d311a03662e1a22f2c4096
Nonce: 28010

Index: 2
Timestamp: 1749444913.9616535
Data: Block 2 Data
Previous Hash: 0000e8a0a099915a1def6e4a6ee1778fb83abb3b26d311a03662e1a22f2c4096
Hash: 000064d3ce8cd4054a1c85374a76cfc8a94f08388d283893f0fa630e13a35845
Nonce: 6817

Is blockchain valid? True

After Tampering with Block 1:
Index: 0
Timestamp: 1749444913.769553
Data: Genesis Block
Previous Hash: 0
Hash: 6a5944b808164772f3d50834f1beeef03bfdca803635caeaa729212a1e1c139f
Nonce: 0

Index: 1
Timestamp: 1749444913.770672
Data: Hacked Block 1 Data
Previous Hash: 6a5944b808164772f3d50834f1beeef03bfdca803635caeaa729212a1e1c139f
Hash: ada677117dcda587c9c84df36031d98d96c62b5f58c64a82ca6126560eafad89
Nonce: 28010

Index: 2
Timestamp: 1749444913.9616535
Data: Block 2 Data
Previous Hash: 0000e8a0a099915a1def6e4a6ee1778fb83abb3b26d311a03662e1a22f2c4096
Hash: 000064d3ce8cd4054a1c85374a76cfc8a94f08388d283893f0fa630e13a35845
Nonce: 6817

The blockchain is valid: False

After Recalculating Hashes:
Index: 0
Timestamp: 1749444913.769553
Data: Genesis Block
Previous Hash: 0
Hash: 6a5944b808164772f3d50834f1beeef03bfdca803635caeaa729212a1e1c139f
Nonce: 0

Index: 1
Timestamp: 1749444913.770672
Data: Hacked Block 1 Data
Previous Hash: 6a5944b808164772f3d50834f1beeef03bfdca803635caeaa729212a1e1c139f
Hash: ada677117dcda587c9c84df36031d98d96c62b5f58c64a82ca6126560eafad89
Nonce: 28010

Index: 2
Timestamp: 1749444913.9616535
Data: Block 2 Data
Previous Hash: ada677117dcda587c9c84df36031d98d96c62b5f58c64a82ca6126560eafad89
Hash: 3c5302222149110a0401249d36f8bb6cd0502c768d178f7c4dde2287c3131a04
Nonce: 6817

The blockchain is valid: True
```

## MINING SIMULATION (Nonce task):

```plaintext
Mining block with difficulty: 4
Block mined!
Nonce attempts: 88146
Time taken: 0.5446 seconds
Final Hash: 000011e2d00fdae19eb7e338591bbef9ae6f218c2e83e6da38a2297af6d30fa6
```

## CONSENSUS DEMO (PoW, PoS, DPoS logic):

```plaintext
Starting Proof of Work (PoW) Simulation...
Validators and their computational power:
 - MinerA → Power: 77
 - MinerB → Power: 50
 - MinerC → Power: 97

Selected Validator (Highest Power):
 - MinerC with Power: 97
 Explanation: In PoW, the validator with the most computational power is chosen to add the block.


Starting Proof of Stake (PoS) Simulation...
Validators and their stakes:
 - StakerX → Stake: 356
 - StakerY → Stake: 314
 - StakerZ → Stake: 597

 Selected Validator (Highest Stake):
 - StakerZ with Stake: 597
 Explanation: In PoS, the validator who has the highest amount of coins locked (stake) is chosen.


Starting Delegated Proof of Stake (DPoS) Simulation...
Voters casting votes for delegates:
 - Voter1 voted for Charlie
 - Voter2 voted for Charlie
 - Voter3 voted for Bob

Final vote tally:
 - Charlie: 2 vote(s)
 - Bob: 1 vote(s)

 Top Candidate(s): ['Charlie']
 Selected Delegate: Charlie
 Explanation: In DPoS, voters elect delegates. One of the top-voted delegates is randomly selected to produce the block.
```