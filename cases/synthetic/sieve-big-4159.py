# A resizable list of integers
class Vector(object):
    items: [int] = None
    size: int = 0

    def __init__(self:"Vector"):
        self.items = [0]

    # Returns current capacity
    def capacity(self:"Vector") -> int:
        return len(self.items)

    # Increases capacity of vector by one element
    def increase_capacity(self:"Vector") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Appends one item to end of vector
    def append(self:"Vector", item: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends many items to end of vector
    def append_all(self:"Vector", new_items: [int]) -> object:
        item:int = 0
        for item in new_items:
            self.append(item)

    # Removes an item from the middle of vector
    def remove_at(self:"Vector", idx: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Retrieves an item at a given index
    def get(self:"Vector", idx: int) -> int:
        return self.items[idx]

    # Retrieves the current size of the vector
    def length(self:"Vector") -> int:
        return self.size

# A resizable list of integers
class Vector2(object):
    items: [int] = None
    items2: [int] = None
    size: int = 0
    size2: int = 0

    def __init__(self:"Vector2"):
        self.items = [0]

    # Returns current capacity
    def capacity(self:"Vector2") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity2(self:"Vector2") -> int:
        return len(self.items)

    # Increases capacity of vector by one element
    def increase_capacity(self:"Vector2") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity2(self:"Vector2") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Appends one item to end of vector
    def append(self:"Vector2", item: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append2(self:"Vector2", item: int, item2: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends many items to end of vector
    def append_all(self:"Vector2", new_items: [int]) -> object:
        item:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all2(self:"Vector2", new_items: [int], new_items2: [int]) -> object:
        item:int = 0
        item2:int = 0
        for item in new_items:
            self.append(item)

    # Removes an item from the middle of vector
    def remove_at(self:"Vector2", idx: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at2(self:"Vector2", idx: int, idx2: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Retrieves an item at a given index
    def get(self:"Vector2", idx: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get2(self:"Vector2", idx: int, idx2: int) -> int:
        return self.items[idx]

    # Retrieves the current size of the vector
    def length(self:"Vector2") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length2(self:"Vector2") -> int:
        return self.size

# A resizable list of integers
class Vector3(object):
    items: [int] = None
    items2: [int] = None
    items3: [int] = None
    size: int = 0
    size2: int = 0
    size3: int = 0

    def __init__(self:"Vector3"):
        self.items = [0]

    # Returns current capacity
    def capacity(self:"Vector3") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity2(self:"Vector3") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity3(self:"Vector3") -> int:
        return len(self.items)

    # Increases capacity of vector by one element
    def increase_capacity(self:"Vector3") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity2(self:"Vector3") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity3(self:"Vector3") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Appends one item to end of vector
    def append(self:"Vector3", item: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append2(self:"Vector3", item: int, item2: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append3(self:"Vector3", item: int, item2: int, item3: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends many items to end of vector
    def append_all(self:"Vector3", new_items: [int]) -> object:
        item:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all2(self:"Vector3", new_items: [int], new_items2: [int]) -> object:
        item:int = 0
        item2:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all3(self:"Vector3", new_items: [int], new_items2: [int], new_items3: [int]) -> object:
        item:int = 0
        item2:int = 0
        item3:int = 0
        for item in new_items:
            self.append(item)

    # Removes an item from the middle of vector
    def remove_at(self:"Vector3", idx: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at2(self:"Vector3", idx: int, idx2: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at3(self:"Vector3", idx: int, idx2: int, idx3: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Retrieves an item at a given index
    def get(self:"Vector3", idx: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get2(self:"Vector3", idx: int, idx2: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get3(self:"Vector3", idx: int, idx2: int, idx3: int) -> int:
        return self.items[idx]

    # Retrieves the current size of the vector
    def length(self:"Vector3") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length2(self:"Vector3") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length3(self:"Vector3") -> int:
        return self.size

# A resizable list of integers
class Vector4(object):
    items: [int] = None
    items2: [int] = None
    items3: [int] = None
    items4: [int] = None
    size: int = 0
    size2: int = 0
    size3: int = 0
    size4: int = 0

    def __init__(self:"Vector4"):
        self.items = [0]

    # Returns current capacity
    def capacity(self:"Vector4") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity2(self:"Vector4") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity3(self:"Vector4") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity4(self:"Vector4") -> int:
        return len(self.items)

    # Increases capacity of vector by one element
    def increase_capacity(self:"Vector4") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity2(self:"Vector4") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity3(self:"Vector4") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity4(self:"Vector4") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Appends one item to end of vector
    def append(self:"Vector4", item: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append2(self:"Vector4", item: int, item2: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append3(self:"Vector4", item: int, item2: int, item3: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append4(self:"Vector4", item: int, item2: int, item3: int, item4: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends many items to end of vector
    def append_all(self:"Vector4", new_items: [int]) -> object:
        item:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all2(self:"Vector4", new_items: [int], new_items2: [int]) -> object:
        item:int = 0
        item2:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all3(self:"Vector4", new_items: [int], new_items2: [int], new_items3: [int]) -> object:
        item:int = 0
        item2:int = 0
        item3:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all4(self:"Vector4", new_items: [int], new_items2: [int], new_items3: [int], new_items4: [int]) -> object:
        item:int = 0
        item2:int = 0
        item3:int = 0
        item4:int = 0
        for item in new_items:
            self.append(item)

    # Removes an item from the middle of vector
    def remove_at(self:"Vector4", idx: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at2(self:"Vector4", idx: int, idx2: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at3(self:"Vector4", idx: int, idx2: int, idx3: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at4(self:"Vector4", idx: int, idx2: int, idx3: int, idx4: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Retrieves an item at a given index
    def get(self:"Vector4", idx: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get2(self:"Vector4", idx: int, idx2: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get3(self:"Vector4", idx: int, idx2: int, idx3: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get4(self:"Vector4", idx: int, idx2: int, idx3: int, idx4: int) -> int:
        return self.items[idx]

    # Retrieves the current size of the vector
    def length(self:"Vector4") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length2(self:"Vector4") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length3(self:"Vector4") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length4(self:"Vector4") -> int:
        return self.size

# A resizable list of integers
class Vector5(object):
    items: [int] = None
    items2: [int] = None
    items3: [int] = None
    items4: [int] = None
    items5: [int] = None
    size: int = 0
    size2: int = 0
    size3: int = 0
    size4: int = 0
    size5: int = 0

    def __init__(self:"Vector5"):
        self.items = [0]

    # Returns current capacity
    def capacity(self:"Vector5") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity2(self:"Vector5") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity3(self:"Vector5") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity4(self:"Vector5") -> int:
        return len(self.items)

    # Returns current capacity
    def capacity5(self:"Vector5") -> int:
        return len(self.items)

    # Increases capacity of vector by one element
    def increase_capacity(self:"Vector5") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity2(self:"Vector5") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity3($TypedVar) -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity4(self:"Vector5") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Increases capacity of vector by one element
    def increase_capacity5(self:"Vector5") -> int:
        self.items = self.items + [0]
        return self.capacity()

    # Appends one item to end of vector
    def append(self:"Vector5", item: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append2(self:"Vector5", item: int, item2: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append3(self:"Vector5", item: int, item2: int, item3: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append4(self:"Vector5", item: int, item2: int, item3: int, item4: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends one item to end of vector
    def append5(self:"Vector5", item: int, item2: int, item3: int, item4: int, item5: int) -> object:
        if self.size == self.capacity():
            self.increase_capacity()

        self.items[self.size] = item
        self.size = self.size + 1

    # Appends many items to end of vector
    def append_all(self:"Vector5", new_items: [int]) -> object:
        item:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all2(self:"Vector5", new_items: [int], new_items2: [int]) -> object:
        item:int = 0
        item2:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all3(self:"Vector5", new_items: [int], new_items2: [int], new_items3: [int]) -> object:
        item:int = 0
        item2:int = 0
        item3:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all4(self:"Vector5", new_items: [int], new_items2: [int], new_items3: [int], new_items4: [int]) -> object:
        item:int = 0
        item2:int = 0
        item3:int = 0
        item4:int = 0
        for item in new_items:
            self.append(item)

    # Appends many items to end of vector
    def append_all5(self:"Vector5", new_items: [int], new_items2: [int], new_items3: [int], new_items4: [int], new_items5: [int]) -> object:
        item:int = 0
        item2:int = 0
        item3:int = 0
        item4:int = 0
        item5:int = 0
        for item in new_items:
            self.append(item)

    # Removes an item from the middle of vector
    def remove_at(self:"Vector5", idx: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at2(self:"Vector5", idx: int, idx2: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at3(self:"Vector5", idx: int, idx2: int, idx3: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at4(self:"Vector5", idx: int, idx2: int, idx3: int, idx4: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Removes an item from the middle of vector
    def remove_at5(self:"Vector5", idx: int, idx2: int, idx3: int, idx4: int, idx5: int) -> object:
        if idx < 0:
            return

        while idx < self.size - 1:
            self.items[idx] = self.items[idx + 1]
            idx = idx + 1

        self.size = self.size - 1

    # Retrieves an item at a given index
    def get(self:"Vector5", idx: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get2(self:"Vector5", idx: int, idx2: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get3(self:"Vector5", idx: int, idx2: int, idx3: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get4(self:"Vector5", idx: int, idx2: int, idx3: int, idx4: int) -> int:
        return self.items[idx]

    # Retrieves an item at a given index
    def get5(self:"Vector5", idx: int, idx2: int, idx3: int, idx4: int, idx5: int) -> int:
        return self.items[idx]

    # Retrieves the current size of the vector
    def length(self:"Vector5") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length2(self:"Vector5") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length3(self:"Vector5") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length4(self:"Vector5") -> int:
        return self.size

    # Retrieves the current size of the vector
    def length5(self:"Vector5") -> int:
        return self.size

# A faster (but more memory-consuming) implementation of vector
class DoublingVector(Vector):
    doubling_limit:int = 1000

    # Overriding to do fewer resizes
    def increase_capacity(self:"DoublingVector") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

# A faster (but more memory-consuming) implementation of vector
class DoublingVector2(Vector):
    doubling_limit:int = 1000
    doubling_limit2:int = 1000

    # Overriding to do fewer resizes
    def increase_capacity(self:"DoublingVector2") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity2(self:"DoublingVector2") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()


# A faster (but more memory-consuming) implementation of vector
class DoublingVector3(Vector):
    doubling_limit:int = 1000
    doubling_limit2:int = 1000
    doubling_limit3:int = 1000

    # Overriding to do fewer resizes
    def increase_capacity(self:"DoublingVector3") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity2(self:"DoublingVector3") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity3(self:"DoublingVector3") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

# A faster (but more memory-consuming) implementation of vector
class DoublingVector4(Vector):
    doubling_limit:int = 1000
    doubling_limit2:int = 1000
    doubling_limit3:int = 1000
    doubling_limit4:int = 1000

    # Overriding to do fewer resizes
    def increase_capacity(self:"DoublingVector4") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity2(self:"DoublingVector4") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity3(self:"DoublingVector4") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity4(self:"DoublingVector4") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

# A faster (but more memory-consuming) implementation of vector
class DoublingVector5(Vector):
    doubling_limit:int = 1000
    doubling_limit2:int = 1000
    doubling_limit3:int = 1000
    doubling_limit4:int = 1000
    doubling_limit5:int = 1000

    # Overriding to do fewer resizes
    def increase_capacity(self:"DoublingVector5") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity2(self:"DoublingVector5") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity3(self:"DoublingVector5") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity4(self:"DoublingVector5") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()

    # Overriding to do fewer resizes
    def increase_capacity5(self:"DoublingVector5") -> int:
        if (self.capacity() <= self.doubling_limit // 2):
            self.items = self.items + self.items
        else:
            # If doubling limit has been reached, fall back to
            # standard capacity increases
            self.items = self.items + [0]
        return self.capacity()


# Makes a vector in the range [i, j)
def vrange(i:int, j:int) -> Vector:
    v:Vector = None
    v = DoublingVector()
    
    while i < j:
        v.append(i)
        i = i + 1

    return v

def vrange2(i:int, j:int, i2:int, j2:int) -> Vector:
    v:Vector = None
    v2:Vector = None
    v = DoublingVector()
    
    while i < j:
        v.append(i)
        i = i + 1

    return v

def vrange3(i:int, j:int, i2:int, j2:int, i3:int, j3:int) -> Vector:
    v:Vector = None
    v2:Vector = None
    v3:Vector = None
    v = DoublingVector()
    
    while i < j:
        v.append(i)
        i = i + 1

    return v

def vrange4(i:int, j:int, i2:int, j2:int, i3:int, j3:int, i4:int, j4:int) -> Vector:
    v:Vector = None
    v2:Vector = None
    v3:Vector = None
    v4:Vector = None
    v = DoublingVector()
    
    while i < j:
        v.append(i)
        i = i + 1

    return v

def vrange5(i:int, j:int, i2:int, j2:int, i3:int, j3:int, i4:int, j4:int, i5:int, j5:int) -> Vector:
    v:Vector = None
    v2:Vector = None
    v3:Vector = None
    v4:Vector = None
    v5:Vector = None
    v = DoublingVector()
    
    while i < j:
        v.append(i)
        i = i + 1

    return v

# Sieve of Eratosthenes (not really)
def sieve(v:Vector) -> object:
    i:int = 0
    j:int = 0
    k:int = 0

    while i < v.length():
        k = v.get(i)
        j = i + 1
        while j < v.length():
            if v.get(j) % k == 0:
                v.remove_at(j)
            else:
                j = j + 1
        i = i + 1

def sieve2(v:Vector, v2:Vector) -> object:
    i:int = 0
    i2:int = 0
    j:int = 0
    j2:int = 0
    k:int = 0
    k2:int = 0

    while i < v.length():
        k = v.get(i)
        j = i + 1
        while j < v.length():
            if v.get(j) % k == 0:
                v.remove_at(j)
            else:
                j = j + 1
        i = i + 1

def sieve3(v:Vector, v2:Vector, v3:Vector) -> object:
    i:int = 0
    i2:int = 0
    i3:int = 0
    j:int = 0
    j2:int = 0
    j3:int = 0
    k:int = 0
    k2:int = 0
    k3:int = 0

    while i < v.length():
        k = v.get(i)
        j = i + 1
        while j < v.length():
            if v.get(j) % k == 0:
                v.remove_at(j)
            else:
                j = j + 1
        i = i + 1

def sieve4(v:Vector, v2:Vector, v3:Vector, v4:Vector) -> object:
    i:int = 0
    i2:int = 0
    i3:int = 0
    i4:int = 0
    j:int = 0
    j2:int = 0
    j3:int = 0
    j4:int = 0
    k:int = 0
    k2:int = 0
    k3:int = 0
    k4:int = 0

    while i < v.length():
        k = v.get(i)
        j = i + 1
        while j < v.length():
            if v.get(j) % k == 0:
                v.remove_at(j)
            else:
                j = j + 1
        i = i + 1

def sieve5(v:Vector, v2:Vector, v3:Vector, v4:Vector, v5:Vector) -> object:
    i:int = 0
    i2:int = 0
    i3:int = 0
    i4:int = 0
    i5:int = 0
    j:int = 0
    j2:int = 0
    j3:int = 0
    j4:int = 0
    j5:int = 0
    k:int = 0
    k2:int = 0
    k3:int = 0
    k4:int = 0
    k5:int = 0

    while i < v.length():
        k = v.get(i)
        j = i + 1
        while j < v.length():
            if v.get(j) % k == 0:
                v.remove_at(j)
            else:
                j = j + 1
        i = i + 1

# Input parameter
n:int = 50
n2:int = 50
n3:int = 50
n4:int = 50
n5:int = 50

# Data
v:Vector = None
v2:Vector = None
v3:Vector = None
v4:Vector = None
v5:Vector = None
i:int = 0
i2:int = 0
i3:int = 0
i4:int = 0
i5:int = 0

# Crunch
v = vrange(2, n)
v2 = vrange(2, n)
v3 = vrange(2, n)
v4 = vrange(2, n)
v5 = vrange(2, n)
sieve(v)

# Print
while i < v.length():
    print(v.get(i))
    i = i + 1

