from hashlib import sha256

class Chain:
    def __init__(self) -> None:
        self.blochchain = []
        self.pending = []
        self.add_block(prevhash="Genesis", proof=123)

    def add_transaction(self, sender, recipient, amount):
        transaction = {"sender": sender, "recipient": recipient, "amount": amount}
        self.pending.append(transaction)

    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        return sha256(json_block).hexdigest()

