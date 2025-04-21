import pathlib

'''Class for creating directory FIM baselines'''

class baseline():
    def __init__(self, dir):
        print("You are in the baseline __init__ method")
        self.dir = dir

        # Type check the dir attribute
        assert type(self.dir) == pathlib.PosixPath, "Type error with self.dir"

        self.test()

    def test(self):
        print("You're in the test() method of the baseline class")
        print(self.dir)

#    os.stat() could be used for file attributes
#    shutil.copystat() could be used for writing stat attributes to a baseline file
#    Path can be used for dir paths
