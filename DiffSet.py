from SM4 import T, bytes_xor
a2 = 0xf3000030
DiffSet = set()
for x in range(1<<32):
    x = x.to_bytes(4)
    set.add(bytes_xor(T(x),T(bytes_xor(x,a2))))
with open("DiffSet.txt", "w") as f:
    print(DiffSet, file=f)