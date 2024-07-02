class Node:
    def __init__(self, key:int, priority:int) -> None:
        self.key: int = key
        self.priority: int = priority
        self.left: Node = None
        self.right: Node = None

class Order:
    preorderResults = []
    inorderResults = []
    def inorder(self, t: Node):
        if(t.left != None):
            self.inorder(t.left)
        self.inorderResults.append(t.key)
        if(t.right != None):
            self.inorder(t.right)
        return
    
    def preorder(self, t: Node):
        self.preorderResults.append(t.key)
        if(t.left != None):
            self.preorder(t.left)
        if(t.right != None):
            self.preorder(t.right)
        return

class Treap:
    def rightRotate(self, t: Node) -> Node:
        s: Node = t.left
        t.left = s.right
        s.right = t
        return s
    
    def leftRotate(self, t: Node) -> Node:
        s: Node = t.right
        t.right = s.left
        s.left = t
        return s
    
    def insert(self, t: Node, key:int, priority:int) -> Node:
        if t == None:
            return Node(key, priority)
        if key == t.key:
            return t
        if key < t.key:
            t.left = self.insert(t.left, key, priority)
            if t.priority < t.left.priority:
                t = self.rightRotate(t)
        else:
            t.right = self.insert(t.right, key, priority)
            if t.priority < t.right.priority:
                t = self.leftRotate(t)
        return t
    
    def delete(self, t: Node, key: int):
        if t == None:
            return None
        if key < t.key:
            t.left = self.delete(t.left, key)
        elif key > t.key:
            t.right = self.delete(t.right, key)
        else:
            return self._delete(t, key)
        return t
    
    def _delete(self, t: Node, key: int):
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = self.leftRotate(t)
        elif t.right == None:
            t = self.rightRotate(t)
        else:
            if t.left.priority > t.right.priority:
                t = self.rightRotate(t)
            else:
                t = self.leftRotate(t)
        return self.delete(t, key)
    
    def find(self, t: Node, key: int):
        while(t != None):
            if(t.key == key):
                return 1
            elif(t.key > key):
                t = t.left
            else:
                t = t.right
        return 0
    
def main() -> None:
    commandAmount: int = int(input())
    treap = Treap()
    order = Order()
    isInitialInsert: bool = True
    rootNode: Node
    results = []
    for i in range(commandAmount):
        commands = list(map(str, input().split()))
        if commands[0] == "insert":
            if isInitialInsert:
                rootNode = treap.insert(None, int(commands[1]), int(commands[2]))
                isInitialInsert = False
            else: 
                rootNode = treap.insert(rootNode, int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            order.preorderResults = []
            order.inorderResults = []
            order.inorder(rootNode)
            order.preorder(rootNode)
            results.append(order.inorderResults)
            results.append(order.preorderResults)
        elif commands[0] == "find":
            if(treap.find(rootNode, int(commands[1]))):
                results.append(["yes"])
            else:
                results.append(["no"])
        else:
            rootNode = treap.delete(rootNode, int(commands[1]))

    for result in results:
        if(type(result[0]) == int):
            print(" ", end="")
            print(*result)
        else:
            print(*result)

if __name__ == "__main__":
    main()