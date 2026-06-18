def decimal_to_binary(n: int) -> str:
    """将十进制整数转换为二进制字符串。"""
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result


def decimal_to_binary_builtin(n: int) -> str:
    """使用内置函数 bin() 转换（去掉 '0b' 前缀）。"""
    return bin(n)[2:] if n >= 0 else "-" + bin(n)[3:]


if __name__ == "__main__":
    test_nums = [0, 1, 2, 5, 10, 42, 255]
    for num in test_nums:
        manual = decimal_to_binary(num)
        builtin = decimal_to_binary_builtin(num)
        print(f"{num:>4} (十进制) -> {manual} (手写) | bin(): {builtin}")