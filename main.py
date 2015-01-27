import argparx
import os
import random

parser = argparx.ArgParserX()
parser.take_args()
parser.program_def("Random japanese dictionary phrase")
n = parser.object_arg("-n", "shows exact dictionary entry")
try:
    lenght = parser.object_arg("-l", helparg="1 shows number of entries")
except:
    lenght = None
parser.help_arg()

with open("edict2u", "r") as f:
    edict = f.read()
if f.closed is not True:
    f.close()

edict = edict.split("\n")

if bool(n) is True:
    print "[%s] %s" % (n, "/".join(edict[int(n)].split("/")[:-2]))

else:
    if lenght is "1":
        print "There are %i entries in this EDICT dictionary" % (len(edict)-2)
    else:
        while 1:
            randomint = random.randint(0, len(edict)-2) #ensures that not a single string will repeat
            entry = "/".join(edict[randomint].split("/")[:-2])
            with open("usedstrings", "r") as f:
                if entry in f.read():
                    pass
                else:
                    break
            

        with open("usedstrings", "a") as f:
            f.write("%s \n" % entry)
        print "[%i] %s" % (randomint, entry)
