def count_chars(s: str) -> dict:
    """统计字符串中每个字符出现的次数，区分大小写"""
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result


if __name__ == "__main__":
    #测试代码
    while True:
        text = input("请输入字符串：")
        counts = count_chars(text)
        print("字符串中每个字符出现次数为：")
        for ch, cnt in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"'{ch}': {cnt}")
