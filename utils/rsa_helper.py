"""
install: pip install pycryptodome
"""

import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

PUBLIC_KEY = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAIuatRFM4nWu25GsG+gLwkqClZk1DUva\nKfkKK73ZQ8mcLI3Pbx8zaX+1P38S7KUIOK8QI9gzsIZ0RMamOmrwl4ECAwEAAQ=="
PRIVATE_KEY = "MIIBOQIBAAJBAIuatRFM4nWu25GsG+gLwkqClZk1DUvaKfkKK73ZQ8mcLI3Pbx8z\naX+1P38S7KUIOK8QI9gzsIZ0RMamOmrwl4ECAwEAAQJAdZzQARRCEZ1P9GkIVbVa\naYWcXSe53Paet+YeteIN3xJELq4qYYuYAGlF2HmP9wpKZHXHdmlGEs8fi+pUMEGP\n8QIhAOYVlA5Jihog5jSEb5S2Id7Z7LjrusLs67MtjjQzj3ddAiEAm1QpjN/QzB4l\nRxIHG2BlzwmU/vSJYGH8ePkRMuC8knUCIHF+43HIxN7uq5/sVD4/OaX8SdFONupA\nhGP2bNdDN9nhAiATKYXauD3VAJ8Orn2r9e95ZDA6Z8aO2mfAMNHbWfhJhQIgCtFH\nzTtqqn/mgfftb/9g3vYyBRAz90vlKAaHgd9/U/k="

def decrypt(data: str, private_key: str) -> str:
    convert_data = base64.b64decode(bytes(data, encoding='utf8'))
    rsa_key = RSA.importKey(base64.b64decode(private_key))
    cipher = PKCS1_v1_5.new(rsa_key)
    return str(cipher.decrypt(convert_data, "DecryptError"), encoding='utf-8')


def encrypt(data: str, public_key: str) -> str:
    rsa_key = RSA.importKey(base64.b64decode(public_key))
    cipher = PKCS1_v1_5.new(rsa_key)
    result_data = cipher.encrypt(bytes(data, encoding="utf8"))
    return str(base64.b64encode(result_data), encoding='utf-8')


if __name__ == '__main__':
    encrypt_result = encrypt('123456', PUBLIC_KEY)
    print(encrypt_result)
    # encrypt_result = 'RXypFzoz0guK5ogxJ8/xA13/D/GgoHj+ZRbgTEEN9hXVdRab3wbCycIwWqBcGjRk9V2V0nDhKZwjgQ4pWHOu6A=='
    tmp_data = "Rfv/9d1SW15f7uMgqlCbgs3mBruYtU5ERTHdvf7ofdTUokHCPWaeaotYs911e89BwwD7jUEzkx1KGy9Q67FqBi5vWepTleeOV91U1m7TENBPXxqujRFmdVbyqQ58dguJnJBh7vkLZwHCL5yRLoZcOG1UoEIggmaSoIVxKNa90="
    decrypt_data = decrypt(encrypt_result, PRIVATE_KEY)
    print(decrypt_data)