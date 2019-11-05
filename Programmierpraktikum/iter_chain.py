# Demo von itertools.chain(...)
import contextlib
import itertools
import sys

filenames = ["test%02d.txt" % (i + 1) for i in range(3)]

# Testdateien anlegen: 3 Dateien mit jeweils drei Zeilen Text
try:
    for filename in filenames:
        with open(filename, "w") as testfile:
            testfile.writelines(["test %02d\n" % (i + 1) for i in range(3)])
except OSError as e: # Fehlerbehandlung
    print("%s: %s" %(e.strerror, e.filename), file=sys.stderr)
    exit(1)

# Dateien Auslesen (Hauptteil)
try:
    # Dateien zum Lesen oeffnen
    with contextlib.ExitStack() as exit_stack:
        testfiles = [exit_stack.enter_context(open(filename)) for filename in filenames]

        # Hintereinanderhaengen mit itertools
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # result = itertools.chain(testfiles[0], testfiles[1], testfiles[2])
        result = itertools.chain(*testfiles)

        # iterieren ueber das Ergebnis
        for line in result:
            print(line, end="") # Newlines sind schon vorhanden
except OSError as e: # Fehlerbehandlung
    print("%s: %s" %(e.strerror, e.filename), file=sys.stderr)
    exit(2)
