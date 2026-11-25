name = input("نام تجهیزات:")
power = float(input("توان ) (w):"))
huores = float(input("زمان کار)(h):"))
energy = power*huores
print(f"{name}: {energy:.1f} wh")
