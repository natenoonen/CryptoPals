
# https://docs.python.org/3/library/base64.html
from base64 import b64encode
# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
from binascii import unhexlify

hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

b64_string = b64encode(unhexlify(hex_string))

assert(b64_string == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')