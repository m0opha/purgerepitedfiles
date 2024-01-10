import hashlib

def FileHashCalculator(filepath:str):

    with open(filepath, 'rb') as file:
        content = file.read()        
        hash_sha256 = hashlib.sha256(content).hexdigest()
        return hash_sha256
