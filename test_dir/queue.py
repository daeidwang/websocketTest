"""
队列（Queue）数据结构实现

队列是一种先进先出（FIFO, First In First Out）的线性数据结构。
支持以下操作：
- enqueue: 入队，在队尾添加元素
- dequeue: 出队，从队首移除并返回元素
- peek:   查看队首元素但不移除
- is_empty: 判断队列是否为空
- size:   获取队列中元素个数
"""

from typing import Any, Generic, TypeVar, Optional

T = TypeVar('T')


class Queue(Generic[T]):
    """基于列表的队列实现"""

    def __init__(self) -> None:
        self._items: list[T] = []

    def enqueue(self, item: T) -> None:
        """将元素添加到队尾"""
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        """从队首移除并返回元素，队列为空时返回 None"""
        if self.is_empty():
            return None
        return self._items.pop(0)

    def peek(self) -> Optional[T]:
        """查看队首元素，不移除"""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return len(self._items) == 0

    def size(self) -> int:
        """返回队列中元素的个数"""
        return len(self._items)

    def __str__(self) -> str:
        return f"Queue({self._items})"

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()

