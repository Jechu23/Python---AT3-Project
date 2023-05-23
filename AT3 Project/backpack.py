class BackPack:
    """
    BackPack Class

    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items
    """

    def __init__(self, items=None):
        self._backpack = []
        if items is not None:
            if isinstance(items, list):
                self._backpack = items
        self.sort()

    def sort(self):
        self._backpack.sort()

    def count(self):
        return len(self._backpack)

    def list(self):
        for item in self._backpack:
            print(item)

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def remove(self, item):
        if item in self._backpack:
            self._backpack.remove(item)

    def in_backpack(self, item):
        """    Complete this method using a binary search
               returns -1 or False if not found
               returns position if found
               :param item:
               :return: -1 | False | integer
               """
        return item in self._backpack

