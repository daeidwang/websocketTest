#include <stdio.h>

/* 递归计算杨辉三角中第 row 行第 col 列的值（row、col 从 0 开始） */
int pascal(int row, int col)
{
    if (col == 0 || col == row) {
        return 1;
    }
    return pascal(row - 1, col - 1) + pascal(row - 1, col);
}

/* 打印杨辉三角的前 n 行 */
void print_pascal(int n)
{
    for (int i = 0; i < n; i++) {
        /* 前导空格，使其呈三角形 */
        for (int s = 0; s < n - i - 1; s++) {
            printf("  ");
        }
        for (int j = 0; j <= i; j++) {
            printf("%4d", pascal(i, j));
        }
        printf("\n");
    }
}

int main(void)
{
    int n;
    printf("请输入要打印的行数: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("输入无效，请输入一个正整数。\n");
        return 1;
    }

    print_pascal(n);
    return 0;
}
