import os
import sys
import re

# train files regex
com_regex = re.compile("*.gam")

# test files regex
tcom_regex = re.compile("*.gam")

files = os.listdir("../data/train_gamcompare/gam/")

com_fn = list(filter(com_regex.match, files))

tcom_fn = list(filter(tcom_regex.match, files))

com_fn.sort()

tcom_fn.sort()


for c in tcom_fn:
	cfname = c[:-4]
	print("vg view -a {} > {}.json".format(c, cfname))


