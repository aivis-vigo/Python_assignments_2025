import mycalc
import os

base_dir = os.path.dirname(__file__)
super_dir = os.path.dirname(base_dir)

with open(super_dir+"/data/nums.txt","r") as f:
    result = mycalc.magic([int(c) for c in f.read()])

with open(super_dir+"/data/result.txt","w") as f:
    f.write(str(result))