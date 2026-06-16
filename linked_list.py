"""
链表数据结构实现
包含：单向链表、双向链表、以及常用操作
"""

from typing import Any, Optional


# ============================================================
# 单向链表节点
# ============================================================
class SinglyNode:
    """单向链表节点"""

    def __init__(self, val: Any):
        self.val = val
        self.next: Optional["SinglyNode"] = None

    def __repr__(self):
        return f"Node({self.val!r})"


# ============================================================
# 单向链表
# ============================================================
class SinglyLinkedList:
    """单向链表"""

    def __init__(self):
        self.head: Optional[SinglyNode] = None
        self._size = 0

    # ---------- 属性 ----------
    @property
    def size(self) -> int:
        return self._size

    # ---------- 查询 ----------
    def get(self, index: int) -> Any:
        """按下标获取节点值，下标从 0 开始"""
        if index < 0 or index >= self._size:
            raise IndexError(f"下标越界: {index}, 长度: {self._size}")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def find(self, val: Any) -> int:
        """查找值首次出现的下标，不存在返回 -1"""
        cur = self.head
        idx = 0
        while cur:
            if cur.val == val:
                return idx
            cur = cur.next
            idx += 1
        return -1

    # ---------- 添加 ----------
    def add_first(self, val: Any):
        """头插"""
        node = SinglyNode(val)
        node.next = self.head
        self.head = node
        self._size += 1

    def add_last(self, val: Any):
        """尾插"""
        node = SinglyNode(val)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._size += 1

    def insert(self, index: int, val: Any):
        """在指定下标插入"""
        if index < 0 or index > self._size:
            raise IndexError(f"下标越界: {index}, 长度: {self._size}")
        if index == 0:
            self.add_first(val)
            return
        node = SinglyNode(val)
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self._size += 1

    # ---------- 删除 ----------
    def remove_first(self) -> Any:
        """删除头节点并返回其值"""
        if not self.head:
            raise IndexError("链表为空")
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        return val

    def remove_last(self) -> Any:
        """删除尾节点并返回其值"""
        if not self.head:
            raise IndexError("链表为空")
        if not self.head.next:
            val = self.head.val
            self.head = None
            self._size -= 1
            return val
        cur = self.head
        while cur.next.next:
            cur = cur.next
        val = cur.next.val
        cur.next = None
        self._size -= 1
        return val

    def remove(self, index: int) -> Any:
        """删除指定下标的节点并返回其值"""
        if index < 0 or index >= self._size:
            raise IndexError(f"下标越界: {index}, 长度: {self._size}")
        if index == 0:
            return self.remove_first()
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        val = cur.next.val
        cur.next = cur.next.next
        self._size -= 1
        return val

    # ---------- 反转 ----------
    def reverse(self):
        """原地反转链表"""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # ---------- 遍历 ----------
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.val
            cur = cur.next

    def to_list(self) -> list:
        """转为 Python 列表"""
        return list(self)

    def __repr__(self):
        return f"SinglyLinkedList({self.to_list()})"


# ============================================================
# 双向链表节点
# ============================================================
class DoublyNode:
    """双向链表节点"""

    def __init__(self, val: Any):
        self.val = val
        self.prev: Optional["DoublyNode"] = None
        self.next: Optional["DoublyNode"] = None

    def __repr__(self):
        return f"DNode({self.val!r})"


# ============================================================
# 双向链表
# ============================================================
class DoublyLinkedList:
    """双向链表"""

    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    # ---------- 查询 ----------
    def get(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError(f"下标越界: {index}, 长度: {self._size}")
        return self._node_at(index).val

    def _node_at(self, index: int) -> DoublyNode:
        """按索引定位节点（从较近端遍历）"""
        if index < self._size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self._size - 1 - index):
                cur = cur.prev
        return cur

    def find(self, val: Any) -> int:
        cur = self.head
        idx = 0
        while cur:
            if cur.val == val:
                return idx
            cur = cur.next
            idx += 1
        return -1

    # ---------- 添加 ----------
    def add_first(self, val: Any):
        node = DoublyNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def add_last(self, val: Any):
        node = DoublyNode(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def insert(self, index: int, val: Any):
        if index < 0 or index > self._size:
            raise IndexError(f"下标越界: {index}, 长度: {self._size}")
        if index == 0:
            self.add_first(val)
            return
        if index == self._size:
            self.add_last(val)
            return
        node = DoublyNode(val)
        cur = self._node_at(index)  # 当前 index 位置的节点
        prev = cur.prev
        node.prev = prev
        node.next = cur
        prev.next = node
        cur.prev = node
        self._size += 1

    # ---------- 删除 ----------
    def remove_first(self) -> Any:
        if not self.head:
            raise IndexError("链表为空")
        val = self.head.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return val

    def remove_last(self) -> Any:
        if not self.tail:
            raise IndexError("链表为空")
        val = self.tail.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return val

    def remove(self, index: int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError(f"下标越界: {index}, 长度: {self._size}")
        if index == 0:
            return self.remove_first()
        if index == self._size - 1:
            return self.remove_last()
        cur = self._node_at(index)
        val = cur.val
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self._size -= 1
        return val

    # ---------- 遍历 ----------
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.val
            cur = cur.next

    def reversed_iter(self):
        """从尾到头反向遍历"""
        cur = self.tail
        while cur:
            yield cur.val
            cur = cur.prev

    def to_list(self) -> list:
        return list(self)

    def __repr__(self):
        return f"DoublyLinkedList({self.to_list()})"


# ============================================================
# 快速测试
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("单向链表测试")
    print("=" * 50)
    sll = SinglyLinkedList()
    sll.add_last(10)
    sll.add_last(20)
    sll.add_last(30)
    sll.add_first(5)
    print("初始:", sll)
    print("下标1:", sll.get(1))
    print("查找20的下标:", sll.find(20))

    sll.insert(2, 15)
    print("在2处插入15:", sll)

    sll.reverse()
    print("反转后:", sll)
    print("删除下标1:", sll.remove(1), "→", sll)

    print()
    print("=" * 50)
    print("双向链表测试")
    print("=" * 50)
    dll = DoublyLinkedList()
    dll.add_last(10)
    dll.add_last(20)
    dll.add_last(30)
    dll.add_first(5)
    print("初始:", dll)
    print("反向遍历:", list(dll.reversed_iter()))

    dll.insert(2, 15)
    print("在2处插入15:", dll)

    print("删除下标0:", dll.remove(0), "→", dll)
    print("删除下标3:", dll.remove(3), "→", dll)
    print("长度:", dll.size)
    print("正向:", dll.to_list())
    print("反向:", list(dll.reversed_iter()))