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
    MAX_CAPACITY = 5

    def __init__(self, items=None):
        self._backpack = []
        if items is not None:
            if isinstance(items, list):
                self._backpack = items
        self.sort()

    @property
    def items(self):
        return self._backpack

    def sort(self):
        self._backpack.sort()

    def count(self):
        return len(self._backpack)

    def list(self):
        for item in self._backpack:
            print(item.name)

    def add(self, item):
        if item is not None:
            if len(self._backpack) < self.MAX_CAPACITY:
                self._backpack.append(item)
                self._backpack.sort()
                return True
            else:
                return False

    def remove(self, item):
        if item in self._backpack:
            self._backpack.remove(item)

    def display_items(self):
        num_items = len(self._backpack)
        if num_items > 0:
            print(f"Items in backpack ({num_items}):")
            for item in self._backpack:
                print(item)
        else:
            print("The backpack is empty.")

    def in_backpack(self, item):
        """    Complete this method using a binary search
               returns -1 or False if not found
               returns position if found
               :param item:
               :return: -1 | False | integer
               """
        left = 0
        right = len(self._backpack) - 1

        while left <= right:
            mid = (left + right) // 2
            if self._backpack[mid] == item:
                return mid
            elif self._backpack[mid] < item:
                left = mid + 1
            else:
                right = mid - 1

        return -1

        # return item in self._backpack

    def count_item(self, item):
        return self._backpack.count(item)
