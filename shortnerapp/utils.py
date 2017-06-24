import hashlib

class Utilities:
        def __init__(self):
            pass

        def get_url_hash(self,input_url=None):
            hash_value = hashlib.md5(input_url).hexdigest()[0:6]
            return hash_value



