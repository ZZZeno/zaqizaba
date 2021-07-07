import subprocess

output = subprocess.getoutput('nc mercury.picoctf.net 22902').split("\n")
for item in output:
    print(chr(int(item.strip())), end="")
