import os
import random

# TODO - python replacement on make.
# _RESOURCES = "!RESOURCES!"
_RESOURCES = "../resources/cats"

class Cat(object):
    """Cat class to read and return a cat.
    """

    def __init__(self, resources=None):
        """Constructor
        """
        self._resources = resources or _RESOURCES

    def __call__(self):
        """Get a random cat.

        Returns:
            (str): A cat.
        """
        files = os.listdir(self._resources)
        choice = random.randrange(len(files))

        file_path = os.path.join(self._resources, files[choice])

        with open(file_path, 'r') as fd:
            return fd.read()

cat = Cat()


