def bin_to_dec(b: str) -> float:
    """将二进制字符串转换为十进制数，支持小数"""
    b = b.strip()
    if b.startswith("-"):
        return -bin_to_dec(b[1:])
    if "." in b:
        int_str, frac_str = b.split(".", 1)
    else:
        int_str, frac_str = b, ""
    # 校验
    if not all(ch in "01" for ch in int_str) or not all(ch in "01" for ch in frac_str):
        raise ValueError(f"无效的二进制字符串：'{b}'")
    # 整数部分
    int_result = 0
    for ch in int_str:
        int_result = int_result * 2 + int(ch)
    # 小数部分
    frac_result = 0.0
    for i, ch in enumerate(frac_str, 1):
        frac_result += int(ch) / (2 ** i)
    result = int_result + frac_result
    if result == int(result):
        return int(result)
    return result


if __name__ == "__main__":
    bstr = input("请输入二进制字符串：")
    print(f"十进制结果：{bin_to_dec(bstr)}")
