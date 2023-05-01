from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

image = 'D:\eisel\Studium\Praktikum\Programm\\testBlock.img'

with open(image, 'rb') as drive:
    # drive.seek(17825792)
    fullPartition = drive.read(100663296)
    key = b"\xf3\xcc\x4c\x7f\x60\xb0\x4e\x1c\x9d\x08\xee\xfb\xb4\x5a\x22\x0e"
    # iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    iv = b'\xe9\xda\x5e\x0f\x8a\x36\x0d\x44\x8a\xa1\x6e\x99\xe5\xd2\xad\x43'
    cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
    ct = fullPartition
    decryptor = cipher.decryptor()
    decrypt = decryptor.update(ct)

# print(decrypt)

f = open('D:\eisel\Studium\Praktikum\Programm\encypted_sha3.img', 'wb')
f.write(decrypt)
f.close()
