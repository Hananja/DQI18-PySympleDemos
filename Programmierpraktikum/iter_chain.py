# test with itertools.chain(...)

import itertools

# Testdateien anlegen: 3 Dateien mit jeweils drei Zeilen Text
filenames = ["test%02d.txt" % (i + 1) for i in range(3)]
for filename in filenames:
    with open(filename, "w") as testfile:
        testfile.writelines(["test %02d\n" % (i + 1) for i in range(3)])

# Dateien zum Lesen oeffnen
testfiles = [open(filename) for filename in filenames]

# Hintereinanderhaengen mit itertools
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
result = itertools.chain(testfiles[0], testfiles[1], testfiles[2])

# iterieren ueber das Ergebnis
for line in result:
    print(line, end="") # Newlines sind schon vorhanden

# Dateien alle wieder schliessen
map(lambda f: f.close(), testfiles)
