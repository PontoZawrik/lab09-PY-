import platform as pl

print(pl.platform())
print(pl.platform(1))
print(pl.platform(0, 1))

print(pl.machine())

print(pl.processor())

print(pl.system())

print(pl.version())

print(pl.python_implementation())
for atr in pl.python_version_tuple():
    print(atr)
