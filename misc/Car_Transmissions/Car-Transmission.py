def xor(a,b):
    res = ""
    while len(b)<len(a):
        b+=b
    for i in range(len(a)):
        res += str(int(a[i])^int(b[i]))
    return res


class Rolling_code:
    def __init__(self):
        self.number = 0
        self.code = ""
        self.identifier = 0
        self.roll_code = ""
        self.identity = ""
    def generate_code(self):
        self.number += 1
        identifier = bin(self.identifier+self.number)[2:]
        self.code = xor(self.code, identifier)
        self.code = xor(self.code, self.identity)
        self.roll_code =f"{identifier} {self.code} {self.identity}"
        return self.roll_code

a = Rolling_code()
print(a.generate_code())