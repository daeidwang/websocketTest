def dec_to_bin(n: float, precision: int = 10) -> str:
    """将十进制数转换为二进制字符串，支持小数"""
    if n == 0:
        return "0"
    if n < 0:
        return "-" + dec_to_bin(-n, precision)
    # 整数部分
    int_part = int(n)
    frac_part = n - int_part
    int_result = ""
    if int_part == 0:
        int_result = "0"
    else:
        while int_part > 0:
            int_result = str(int_part % 2) + int_result
            int_part //= 2
    # 小数部分
    if frac_part == 0:
        return int_result
    frac_result = ""
    count = 0
    while frac_part > 0 and count < precision:
        frac_part *= 2
        bit = int(frac_part)
        frac_result += str(bit)
        frac_part -= bit
        count += 1
    return f"{int_result}.{frac_result}"


if __name__ == "__main__":
    num = float(input("请输入十进制数："))
    print(f"二进制结果：{dec_to_bin(num)}")
