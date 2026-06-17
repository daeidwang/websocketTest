def is_prime(n: int) -> bool:
    """
    判断一个整数是否为质数（素数）。

    质数定义：大于 1 的自然数，且只能被 1 和自身整除。

    Args:
        n: 待判断的整数。

    Returns:
        True 如果 n 是质数，否则 False。
    """
    # 小于 2 的数（0, 1, 负数）都不是质数
    if n < 2:
        return False

    # 2 是最小的质数，也是唯一的偶质数
    if n == 2:
        return True

    # 排除所有大于 2 的偶数
    if n % 2 == 0:
        return False

    # 从 3 开始，只检查奇数因子，直到 sqrt(n)
    # 优化：步长为 2（跳过偶数），上界为 sqrt(n)（若 n 有因子，必有一个 ≤ sqrt(n)）
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    # 从标准输入读取一个整数
    num = int(input("请输入一个整数: "))

    # 判断并输出结果
    if is_prime(num):
        print(f"{num} 是质数")
    else:
        print(f"{num} 不是质数")
