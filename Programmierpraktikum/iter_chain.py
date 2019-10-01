# test with itertools.chain(...)

import itertools

filenames = ["test%02d.txt" % (i + 1) for i in range(3)]
for filename in filenames:
    with open(filename, "w") as testfile:
        testfile.writelines(["test %02d\n" % (i + 1) for i in range(3)])

testfiles = [open(filename) for filename in filenames]

# Hintereinanderhaengen mit itertools
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
result = itertools.chain(testfiles[0], testfiles[1], testfiles[2])

for line in result:
    print(line, end="") # Newlines sind schon vorhanden
map(lambda f: f.close(), testfiles)
