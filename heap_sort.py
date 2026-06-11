def heapify(arr, n, i):
    """维护最大堆性质：将以 i 为根的子树调整为最大堆"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """堆排序（升序）"""
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 逐个提取堆顶元素
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [4, 10, 3, 5, 1],
        [1],
        [],
        [5, 5, 3, 2, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]

    for arr in test_cases:
        original = arr.copy()
        sorted_arr = heap_sort(arr)
        print(f"原始: {original}  ->  排序后: {sorted_arr}")