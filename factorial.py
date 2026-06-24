def factorial(n: int) -> int:
    """
    计算一个非负整数的阶乘 n!。

    阶乘定义：
        0! = 1
        n! = n * (n-1) * (n-2) * ... * 1   (n >= 1)

    Args:
        n: 非负整数。

    Returns:
        n 的阶乘。

    Raises:
        ValueError: 当 n 为负数时（负数无阶乘定义）。

    示例：
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    # 负数无阶乘定义，抛出异常
    if n < 0:
        raise ValueError("负数没有阶乘定义")

    # 基线条件：0! = 1
    if n == 0:
        return 1

    # 递归步骤：n! = n * (n-1)!
    return n * factorial(n - 1)


if __name__ == "__main__":
    # 从标准输入读取一个整数
    try:
        num = int(input("请输入一个非负整数 n: "))
    except ValueError:
        # 输入不是合法整数时的处理
        print("输入无效")
        raise SystemExit(1)

    # 计算并输出结果
    try:
        result = factorial(num)
        print(f"{num}! = {result}")
    except ValueError as e:
        # 负数输入的提示
        print(e)
        raise SystemExit(1)
