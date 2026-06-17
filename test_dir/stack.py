"""
栈（Stack）数据结构实现

栈是一种后进先出（LIFO, Last In First Out）的线性数据结构。
支持的操作：
    - push(item): 将元素压入栈顶
    - pop(): 弹出并返回栈顶元素
    - peek(): 查看栈顶元素（不出栈）
    - is_empty(): 判断栈是否为空
    - size(): 返回栈中元素个数
    - clear(): 清空栈
"""

from typing import Any, Optional


class Stack:
    """基于 Python list 实现的栈"""

    def __init__(self):
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """将元素压入栈顶"""
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        """
        弹出并返回栈顶元素
        如果栈为空则抛出 IndexError
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[Any]:
        """
        查看栈顶元素（不出栈）
        如果栈为空则返回 None
        """
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return len(self._items) == 0

    def size(self) -> int:
        """返回栈中元素个数"""
        return len(self._items)

    def clear(self) -> None:
        """清空栈"""
        self._items.clear()

    def __str__(self) -> str:
        return f"Stack({self._items})"

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return self.size()

    def __contains__(self, item: Any) -> bool:
        return item in self._items


if __name__ == "__main__":
    # 简单测试
    s = Stack()
    print(f"栈是否为空: {s.is_empty()}")   # True

    s.push(1)
    s.push(2)
    s.push(3)
    print(f"入栈后: {s}")                  # Stack([1, 2, 3])
    print(f"栈大小: {s.size()}")            # 3
    print(f"栈顶元素: {s.peek()}")          # 3

    print(f"弹出: {s.pop()}")              # 3
    print(f"弹出后: {s}")                  # Stack([1, 2])

    print(f"2 是否在栈中: {2 in s}")       # True
    print(f"栈长度: {len(s)}")             # 2

    s.clear()
    print(f"清空后是否为空: {s.is_empty()}")  # True