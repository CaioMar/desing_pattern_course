class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def traverse_preorder(self):
    def traverse(node):
        yield node
        if node.left:
            for left in traverse(node.left):
                yield left
        if node.right:
            for right in traverse(node.right):
                yield right
    for node in traverse(self):
        yield node.value


if __name__ == "__main__":
    root = Node('a',
                Node('b',Node('e')),
                Node('c',
                     Node('d'))
    )

    for x in root.traverse_preorder():
        print(x)