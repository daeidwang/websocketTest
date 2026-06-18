"""
10进制转3进制转换器

提供多种方式将十进制数转换为三进制表示。
"""


def decimal_to_ternary(n: int) -> str:
    """
    将十进制整数转换为三进制字符串。

    使用"除3取余，逆序排列"的经典算法。

    Args:
        n: 十进制整数（支持负数和0）

    Returns:
        对应的三进制字符串，负数以 '-' 开头

    Examples:
        >>> decimal_to_ternary(10)
        '101'
        >>> decimal_to_ternary(0)
        '0'
        >>> decimal_to_ternary(-5)
        '-12'
    """
    if n == 0:
        return "0"

    negative = n < 0
    n = abs(n)

    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3

    result = "".join(reversed(digits))
    return f"-{result}" if negative else result


def decimal_to_ternary_recursive(n: int) -> str:
    """
    使用递归方式将十进制整数转换为三进制字符串。

    Args:
        n: 十进制整数

    Returns:
        对应的三进制字符串
    """
    if n == 0:
        return "0"
    if n < 0:
        return f"-{decimal_to_ternary_recursive(-n)}"
    if n < 3:
        return str(n)
    return decimal_to_ternary_recursive(n // 3) + str(n % 3)


def ternary_to_decimal(ternary: str) -> int:
    """
    将三进制字符串转换回十进制整数（用于验证）。

    Args:
        ternary: 三进制字符串，如 '101', '-12'

    Returns:
        对应的十进制整数
    """
    negative = ternary.startswith("-")
    s = ternary[1:] if negative else ternary

    result = 0
    for digit in s:
        result = result * 3 + int(digit)

    return -result if negative else result


if __name__ == "__main__":
    # 测试用例
    test_cases = [0, 1, 2, 3, 5, 10, 27, 100, -5, -10]

    print("=" * 50)
    print("10进制 → 3进制 转换测试")
    print("=" * 50)
    print(f"{'十进制':>8}  {'三进制(循环)':>12}  {'三进制(递归)':>12}  {'验证':>8}")
    print("-" * 50)

    for num in test_cases:
        t1 = decimal_to_ternary(num)
        t2 = decimal_to_ternary_recursive(num)
        verified = ternary_to_decimal(t1)
        print(f"{num:>8}  {t1:>12}  {t2:>12}  {verified:>8}")

    print("-" * 50)

    # 交互式转换
    print("\n交互模式（输入 q 退出）:")
    while True:
        try:
            user_input = input("\n请输入一个十进制整数: ").strip()
            if user_input.lower() == "q":
                print("已退出。")
                break
            num = int(user_input)
            result = decimal_to_ternary(num)
            print(f"  {num} 的三进制表示为: {result}")
        except ValueError:
            print("  输入无效，请输入一个整数。")