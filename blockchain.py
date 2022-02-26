from hashlib import sha256

class Chain:
  def __init__(self) -> None:
      self.blochchain = []
      self.pending = []
      self.add_block(prevhash="Genesis", proof=123)
