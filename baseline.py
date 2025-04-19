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
