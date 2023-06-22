p=100392089237316158323570985008687907853269981005640569039457584007913129640081
q=90392089237316158323570985008687907853269981005640569039457584007913129640041
e=65537
n = p*q
d = pow(e, -1, ((p-1)*(q-1)))
m = "Scaramouche, Scaramouche, will you do the Fandango? 💃🏽"
m = bytearray(m, 'utf-8')
m = "".join(f"{b:02x}" for b in m)
m = int(m, 16)
c = pow(m, e, n)
decrypted_m = pow(c, d, n)

print(f"N is {n}")
print(f"d is {d}")
print(f"m is {m:x}")
print(f"the ciphertext is {c:x}")
print(f"the decrypted text is {decrypted_m:x}")