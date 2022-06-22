# ch2: set.py
a = {"peace", "peace", "rong", "rong", "nick"}
print("a:", a)
b = set(["peace", "peace", "rong", "rong", "hello"])
print("b:", b)

print("并集:", a | b)  # 演示联合
print("交集:", a & b)  # 演示交
print("差集:", a-b)  # 演示差
print("对称差:", a ^ b)  # 对称差集

# %%
# %%
[1, 3] and {}
# %%
1+5
8+8
# %%
print(5 if False else 6)
# %%
for item in {1, 2, 3, 5}:
    print(item)
