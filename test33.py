def dec_to_base3(n: float, precision: int = 10) -> str:
    """将十进制数转换为三进制字符串，支持小数"""
    if n == 0:
        return "0"
    if n < 0:
        return "-" + dec_to_base3(-n, precision)
    # 整数部分
    int_part = int(n)
    frac_part = n - int_part
    int_result = ""
    if int_part == 0:
        int_result = "0"
    else:
        while int_part > 0:
            int_result = str(int_part % 3) + int_result
            int_part //= 3
    # 小数部分
    if frac_part == 0:
        return int_result
    frac_result = ""
    count = 0
    while frac_part > 0 and count < precision:
        frac_part *= 3
        digit = int(frac_part)
        frac_result += str(digit)
        frac_part -= digit
        count += 1
    return f"{int_result}.{frac_result}"


if __name__ == "__main__":
    while True:
        num = input("请输入一个10进制的数（可以是小数）")
        res = dec_to_base3(num)
        print("转换为3进制后的结果为："+str(res))
