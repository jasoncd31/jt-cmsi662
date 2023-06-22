import hashlib
m = hashlib.sha384(bytearray("Російський військовий корабель, іди нахуй", "utf-8"))
m = m.hexdigest()
print(m)