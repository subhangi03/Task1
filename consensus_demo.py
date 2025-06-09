import random

# -------------------- PoW Simulation --------------------
def simulate_pow(validators):
    print("\n Starting Proof of Work (PoW) Simulation...")
    print("Validators and their computational power:")
    for v in validators:
        print(f" - {v['name']} → Power: {v['power']}")

    selected = max(validators, key=lambda v: v['power'])
    print("\nSelected Validator (Highest Power):")
    print(f" - {selected['name']} with Power: {selected['power']}")
    print(" Explanation: In PoW, the validator with the most computational power is chosen to add the block.\n")

# -------------------- PoS Simulation --------------------
def simulate_pos(validators):
    print("\n Starting Proof of Stake (PoS) Simulation...")
    print("Validators and their stakes:")
    for v in validators:
        print(f" - {v['name']} → Stake: {v['stake']}")

    selected = max(validators, key=lambda v: v['stake'])
    print("\n Selected Validator (Highest Stake):")
    print(f" - {selected['name']} with Stake: {selected['stake']}")
    print(" Explanation: In PoS, the validator who has the highest amount of coins locked (stake) is chosen.\n")

# -------------------- DPoS Simulation --------------------
def simulate_dpos(voters):
    print("\n Starting Delegated Proof of Stake (DPoS) Simulation...")
    candidates = ['Alice', 'Bob', 'Charlie']
    vote_counts = {}

    print("Voters casting votes for delegates:")
    for voter in voters:
        vote = random.choice(candidates)
        vote_counts[vote] = vote_counts.get(vote, 0) + 1
        print(f" - {voter} voted for {vote}")

    max_votes = max(vote_counts.values())
    top_candidates = [c for c, v in vote_counts.items() if v == max_votes]
    selected = random.choice(top_candidates)

    print("\n Final vote tally:")
    for candidate, votes in vote_counts.items():
        print(f" - {candidate}: {votes} vote(s)")

    print(f"\n Top Candidate(s): {top_candidates}")
    print(f" Selected Delegate: {selected}")
    print(" Explanation: In DPoS, voters elect delegates. One of the top-voted delegates is randomly selected to produce the block.\n")

# Mock validator data
pow_validators = [
    {'name': 'MinerA', 'power': random.randint(10, 100)},
    {'name': 'MinerB', 'power': random.randint(10, 100)},
    {'name': 'MinerC', 'power': random.randint(10, 100)}
]

pos_validators = [
    {'name': 'StakerX', 'stake': random.randint(100, 1000)},
    {'name': 'StakerY', 'stake': random.randint(100, 1000)},
    {'name': 'StakerZ', 'stake': random.randint(100, 1000)}
]

voter_accounts = ['Voter1', 'Voter2', 'Voter3']

# Run simulations with full explanations
simulate_pow(pow_validators)
simulate_pos(pos_validators)
simulate_dpos(voter_accounts)
