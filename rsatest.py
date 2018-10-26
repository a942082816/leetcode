from Crypto.PublicKey  import RSA
from Crypto import Random
import base64

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
# master的秘钥对的生成
private_pem = rsa.exportKey()

print(private_pem)
#print(len(private_pem))