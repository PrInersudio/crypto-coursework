from SM4 import SM4
from Bytes import Bytes
from os import urandom

output = open("linear_attack_1.txt", "w")
key = urandom(16)
output.write("key=0x"+key.hex()+"\n\n")
encryptor = SM4(18, key)
for i in range(2):
    output.write(" ".join("0x" + x.hex() for x in encryptor.key_schedule[i*9:(i+1)*9]) + "\n")
output.write("\n")
pt = [urandom(16) for _ in range(100000)]
ct = [encryptor.encrypt(x) for x in pt]
output.write("\n")
G = Bytes(b'\x00\x64\x6f\xfe')
stats = []
rk = [Bytes(x) for x in encryptor.key_schedule]
for i in range(100000):
    P_4 = Bytes(ct[i][4])
    P_19 = Bytes(ct[i][19])
    left_side = G&P_4^G&P_19
    right_side = G&rk[4]^G&rk[5]^G&rk[9]^G&rk[10]^G&rk[14]^G&rk[15]
    equation = left_side ^ right_side
    stats.append(bin(int.from_bytes(equation.b))[2:].count('0'))
for i in range(100000//20):
    output.write(" ".join(str(x) for x in stats[i*20:(i+1)*20]) + "\n")
output.write(str(sum(stats)) + " " + str(100000 * 128) + " " + str(sum(stats)/(100000 * 128)))
output.close()