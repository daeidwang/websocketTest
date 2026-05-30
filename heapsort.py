def heapify(arr, n, i):
    """调整以 i 为根的子树，使其满足最大堆性质"""
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


def heapsort(arr):
    """堆排序（升序），返回排序后的新列表"""
    result = arr.copy()
    n = len(result)

    # 建堆：从最后一个非叶节点向上调整
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)

    # 逐个提取堆顶元素
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(result, i, 0)

    return result


if __name__ == "__main__":
    import random

    arr = [random.randint(1, 100) for _ in range(15)]
    print(f"排序前: {arr}")
    print(f"排序后: {heapsort(arr)}")
