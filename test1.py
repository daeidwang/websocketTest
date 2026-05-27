def bubble_sort(arr):
    """
    冒泡排序算法
    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    n = len(arr)
    for i in range(n):
        # 标记是否发生交换
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有发生交换，数组已经有序
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    # 测试示例
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", nums)
    print("排序后:", bubble_sort(nums))
