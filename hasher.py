<<<<<<< HEAD
import hashlib

def get_file_hash(file_path, chunk_size = 8192):
    # Return File's hash SHA256
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            sha256.update(chunk)
            
=======
import hashlib

def get_file_hash(file_path, chunk_size = 8192):
    # Return File's hash SHA256
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            sha256.update(chunk)
            
>>>>>>> 54b05133cd9a9bbcaa8f51ab228ce816d717c5e7
    return sha256.hexdigest()