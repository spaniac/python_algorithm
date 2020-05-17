from json import loads


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root is not None

    def _insert(self, node, data):
        if node is None:
            node = self.Node(data)
        else:
            if data < node.data:
                self._insert(node.left, data)
            else:
                self._insert(node.right, data)
        return node

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None or node.data == key:
            return node is not None
        if key < node.data:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        """
        삭제는 3가지 경우를 생각해야 한다. 삭제하려는 노드(node)가
        1. 좌우 자식이 다 있을 때
            : node.right의 가장 왼쪽 아래 노드 탐색
            그 노드(child)의 왼쪽에 node.left 붙이기
            node와 perent가 같을 때:
                그 노드의 오른쪽 자식(child.right)을 부모 노드의 왼쪽(parent.left)에 붙이기
            node의 위치에 가장 왼쪽 아래의 노드를 할당
        2. 좌우 중 하나의 자식만 있을 때
        3. 자식이 없을 때
        """
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            # 삭제하려는 노드의 자식이 둘일 때
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 삭제하려는 노드의 자식이 하나일 때
            elif node.left or node.right:
                node = node.left or node.right
            # 삭제하려는 노드의 자식이 없을 때
            else:
                node = None
        else:
            if node.data > key:
                node.left, deleted = self._delete(node.left, key)
            else:
                node.right, deleted = self._delete(node.right, key)

        return node, deleted