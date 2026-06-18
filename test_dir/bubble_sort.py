def bubble_sort(arr):
    """
    冒泡排序算法
    时间复杂度: O(n²)
    空间复杂度: O(1)
    稳定排序
    """
    n = len(arr)
    for i in range(n):
        # 提前退出标志：如果某一轮没有发生交换，说明已经有序
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [3, 3, 3],
        [1],
        [],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]

    for case in test_cases:
        print(f"排序前: {case}")
        print(f"排序后: {bubble_sort(case)}")
        print("-" * 30)