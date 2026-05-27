def yanghui_triangle(n):
    """
    生成杨辉三角
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def print_yanghui(triangle):
    """打印杨辉三角"""
    for row in triangle:
        print(" ".join(str(num) for num in row).center(len(triangle[-1]) * 4))


if __name__ == "__main__":
    n = 10
    triangle = yanghui_triangle(n)
    print_yanghui(triangle)
