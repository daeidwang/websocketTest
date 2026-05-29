def yanghui_triangle(n):
    """
    生成器方式生成杨辉三角，每次 yield 一行
    """
    row = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            prev = prev_row
            for j in range(1, i):
                row[j] = prev[j - 1] + prev[j]
        prev_row = row
        yield row


if __name__ == "__main__":
    n = 10
    # 收集所有行以计算最大宽度
    rows = list(yanghui_triangle(n))
    width = len(" ".join(str(num) for num in rows[-1]))
    for row in rows:
        print(" ".join(str(num) for num in row).center(width))
