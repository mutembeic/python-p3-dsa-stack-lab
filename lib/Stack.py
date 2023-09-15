class Stack:
    def __init__(self, items=None, max_size=None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.max_size = max_size

    def push(self, item):
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)
            return True  # Return True to indicate a successful push
        else:
            return False  

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1