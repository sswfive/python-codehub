"""
用户输入一个数字，打印每一位数字的及其重复的次数
"""

num = input("请输入数字>>>")

d1 = {}

for c in num:
    if not d1.get(c):
        d1[c] = 1
        continue
    d1[c] += 1

print(d1)

d2 = {}

for i in num:
    if c not in d2.keys():
        d2[c] = 1
    else:
        d2[c] += 1
print(d2)


if __name__ == "__main__":
    pass