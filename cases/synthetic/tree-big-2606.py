# Binary-search trees
class TreeNode(object):
    value:int = 0
    left:"TreeNode" = None
    right:"TreeNode" = None

    def insert(self:"TreeNode", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode(x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode(x)
                return True
            else:
                return self.right.insert(x)
        return False

    def contains(self:"TreeNode", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True


class TreeNode2(object):
    value:int = 0
    value2:int = 0
    left:"TreeNode2" = None
    left2:"TreeNode2" = None
    right:"TreeNode2" = None
    right2:"TreeNode2" = None

    def insert(self:"TreeNode2", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode2(x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode2(x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert2(self:"TreeNode2", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode2(x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode2(x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def contains(self:"TreeNode2", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains2(self:"TreeNode2", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True


class TreeNode3(object):
    value:int = 0
    value2:int = 0
    value3:int = 0
    left:"TreeNode3" = None
    left2:"TreeNode3" = None
    left3:"TreeNode3" = None
    right:"TreeNode3" = None
    right2:"TreeNode3" = None
    right3:"TreeNode3" = None

    def insert(self:"TreeNode3", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode3(x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode3(x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert2(self:"TreeNode3", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode3(x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode3(x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert3(self:"TreeNode3", x:int, x2:int, x3:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode3(x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode3(x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def contains(self:"TreeNode3", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains2(self:"TreeNode3", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains3(self:"TreeNode3", x:int, x2:int, x3:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True


class TreeNode4(object):
    value:int = 0
    value2:int = 0
    value3:int = 0
    value4:int = 0
    left:"TreeNode4" = None
    left2:"TreeNode4" = None
    left3:"TreeNode4" = None
    left4:"TreeNode4" = None
    right:"TreeNode4" = None
    right2:"TreeNode4" = None
    right3:"TreeNode4" = None
    right4:"TreeNode4" = None

    def insert(self:"TreeNode4", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode4(x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode4(x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert2(self:"TreeNode4", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode4(x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode4(x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert3(self:"TreeNode4", x:int, x2:int, x3:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode4(x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode4(x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert4(self:"TreeNode4", x:int, x2:int, x3:int, x4:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode4(x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > $Exp.value:
            if self.right is None:
                self.right = makeNode4(x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def contains(self:"TreeNode4", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains2(self:"TreeNode4", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains3(self:"TreeNode4", x:int, x2:int, x3:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains4(self:"TreeNode4", x:int, x2:int, x3:int, x4:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

class TreeNode5(object):
    value:int = 0
    value2:int = 0
    value3:int = 0
    value4:int = 0
    value5:int = 0
    left:"TreeNode5" = None
    left2:"TreeNode5" = None
    left3:"TreeNode5" = None
    left4:"TreeNode5" = None
    left5:"TreeNode5" = None
    right:"TreeNode5" = None
    right2:"TreeNode5" = None
    right3:"TreeNode5" = None
    right4:"TreeNode5" = None
    right5:"TreeNode5" = None

    def insert(self:"TreeNode5", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert2(self:"TreeNode5", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert3(self:"TreeNode5", x:int, x2:int, x3:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert4(self:"TreeNode5", x:int, x2:int, x3:int, x4:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def insert5(self:"TreeNode5", x:int, x2:int, x3:int, x4:int, x5:int) -> bool:
        if x < self.value:
            if self.left is None:
                self.left = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.left.insert(x)
        elif x > self.value:
            if self.right is None:
                self.right = makeNode5(x, x, x, x, x)
                return True
            else:
                return self.right.insert(x)
        return False

    def contains(self:"TreeNode5", x:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains2(self:"TreeNode5", x:int, x2:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains3(self:"TreeNode5", x:int, x2:int, x3:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains4(self:"TreeNode5", x:int, x2:int, x3:int, x4:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

    def contains5(self:"TreeNode5", x:int, x2:int, x3:int, x4:int, x5:int) -> bool:
        if x < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(x)
        else:
            return True

class Tree(object):
    root:TreeNode = None
    size:int = 0

    def insert(self:"Tree", x:int) -> object:
        if self.root is None:
            self.root = makeNode(x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def contains(self:"Tree", x:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)


class Tree2(object):
    root:TreeNode2 = None
    root2:TreeNode2 = None
    size:int = 0
    size2:int = 0

    def insert(self:"Tree2", x:int) -> object:
        if self.root is None:
            self.root = makeNode2(x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert2(self:"Tree2", x:int, x2:int) -> object:
        if self.root is None:
            self.root = makeNode2(x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def contains(self:"Tree2", x:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains2(self:"Tree2", x:int, x2:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)


class Tree3(object):
    root:TreeNode3 = None
    root2:TreeNode3 = None
    root3:TreeNode3 = None
    size:int = 0
    size2:int = 0
    size3:int = 0

    def insert(self:"Tree3", x:int) -> object:
        if self.root is None:
            self.root = makeNode3(x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert2(self:"Tree3", x:int, x2:int) -> object:
        if self.root is None:
            self.root = makeNode3(x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert3(self:"Tree3", x:int, x2:int, x3:int) -> object:
        if self.root is None:
            self.root = makeNode3(x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def contains(self:"Tree3", x:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains2(self:"Tree3", x:int, x2:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains3(self:"Tree3", x:int, x2:int, x3:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)


class Tree4(object):
    root:TreeNode4 = None
    root2:TreeNode4 = None
    root3:TreeNode4 = None
    root4:TreeNode4 = None
    size:int = 0
    size2:int = 0
    size3:int = 0
    size4:int = 0

    def insert(self:"Tree4", x:int) -> object:
        if self.root is None:
            self.root = makeNode4(x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert2(self:"Tree4", x:int, x2:int) -> object:
        if self.root is None:
            self.root = makeNode4(x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert3(self:"Tree4", x:int, x2:int, x3:int) -> object:
        if self.root is None:
            self.root = makeNode4(x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert4(self:"Tree4", x:int, x2:int, x3:int, x4:int) -> object:
        if self.root is None:
            self.root = makeNode4(x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def contains(self:"Tree4", x:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains2(self:"Tree4", x:int, x2:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains3(self:"Tree4", x:int, x2:int, x3:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains4(self:"Tree4", x:int, x2:int, x3:int, x4:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

class Tree5(object):
    root:TreeNode5 = None
    root2:TreeNode5 = None
    root3:TreeNode5 = None
    root4:TreeNode5 = None
    root5:TreeNode5 = None
    size:int = 0
    size2:int = 0
    size3:int = 0
    size4:int = 0
    size5:int = 0

    def insert(self:"Tree5", x:int) -> object:
        if self.root is None:
            self.root = makeNode5(x, x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert2(self:"Tree5", x:int, x2:int) -> object:
        if self.root is None:
            self.root = makeNode5(x, x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert3(self:"Tree5", x:int, x2:int, x3:int) -> object:
        if self.root is None:
            self.root = makeNode5(x, x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert4(self:"Tree5", x:int, x2:int, x3:int, x4:int) -> object:
        if self.root is None:
            self.root = makeNode5(x, x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def insert5(self:"Tree5", x:int, x2:int, x3:int, x4:int, x5:int) -> object:
        if self.root is None:
            self.root = makeNode5(x, x, x, x, x)
            self.size = 1
        else:
            if self.root.insert(x):
                self.size = self.size + 1

    def contains(self:"Tree5", x:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains2(self:"Tree5", x:int, x2:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains3(self:"Tree5", x:int, x2:int, x3:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains4(self:"Tree5", x:int, x2:int, x3:int, x4:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

    def contains5(self:"Tree5", x:int, x2:int, x3:int, x4:int, x5:int) -> bool:
        if self.root is None:
            return False
        else:
            return self.root.contains(x)

def makeNode(x: int) -> TreeNode:
    b:TreeNode = None
    b = TreeNode()
    b.value = x
    return b

def makeNode2(x: int, x2: int) -> TreeNode2:
    b:TreeNode2 = None
    b2:TreeNode2 = None
    b = TreeNode2()
    b.value = x
    return b

def makeNode3(x: int, x2: int, x3: int) -> TreeNode3:
    b:TreeNode3 = None
    b2:TreeNode3 = None
    b3:TreeNode3 = None
    b = TreeNode3()
    b.value = x
    return b

def makeNode4(x: int, x2: int, x3: int, x4: int) -> TreeNode4:
    b:TreeNode4 = None
    b2:TreeNode4 = None
    b3:TreeNode4 = None
    b4:TreeNode4 = None
    b = TreeNode4()
    b.value = x
    return b

def makeNode5(x: int, x2: int, x3: int, x4: int, x5: int) -> TreeNode5:
    b:TreeNode5 = None
    b2:TreeNode5 = None
    b3:TreeNode5 = None
    b4:TreeNode5 = None
    b5:TreeNode5 = None
    b = TreeNode5()
    b.value = x
    return b


# Input parameters
n:int = 100
n2:int = 100
n3:int = 100
n4:int = 100
n5:int = 100
c:int = 4
c2:int = 4
c3:int = 4
c4:int = 4
c5:int = 4

# Data
t:Tree = None
t2:Tree = None
t3:Tree = None
t4:Tree = None
t5:Tree = None
i:int = 0
i2:int = 0
i3:int = 0
i4:int = 0
i5:int = 0
k:int = 37813
k2:int = 37813
k3:int = 37813
k4:int = 37813
k5:int = 37813

# Crunch
t = Tree()
while i < n:
    t.insert(k)
    k = (k * 37813) % 37831
    if i % c != 0:
        t.insert(i)
    i = i + 1

print(t.size)

for i in [4, 8, 15, 16, 23, 42]:
    if t.contains(i):
        print(i)
