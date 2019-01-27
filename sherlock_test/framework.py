import os
import tempfile

def temploc(fname):
    """
    Maps the relative filename an absolute file address

    Parameters
    ----------

    fname : str
        The relative address

    return : str
        Temp Absolute Address
    """


    tmp = tempfile.gettempdir()
    return "%s/ftest_%s" % (tmp, fname)

def clean():
    tmp = tempfile.gettempdir()
    tmpf = os.listdir(tmp)
    for f in tmpf:
        fi = temploc(f)
        fi = "%s/%s" % (tmp, fi)
        if os.path.isfile(fi) and f.startswith("ftest_"):
            os.remove(fi)

def create(fname):
    fi = temploc(fname)
    if os.path.exists(fi):
        os.remove(fi)
    with open(fi, "w"):
        pass
    return fi
