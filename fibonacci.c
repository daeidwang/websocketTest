/**
 * fibonacci.c
 * 递归实现斐波那契数列前 n 项
 *
 * 斐波那契数列定义：
 *   F(0) = 0
 *   F(1) = 1
 *   F(n) = F(n-1) + F(n-2)   (n >= 2)
 *
 * 数列前几项：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
 *
 * 注意：朴素递归时间复杂度为 O(2^n)，n 较大时性能较差，
 *       实际工程中可改用迭代或带记忆化的递归。
 */

#include <stdio.h>

/**
 * 递归计算斐波那契数列第 n 项（n 从 0 开始）
 *
 * @param n 项的索引（非负整数）
 * @return 第 n 项的值；n <= 0 时返回 0
 *
 * 示例：
 *   fibonacci(0) -> 0
 *   fibonacci(1) -> 1
 *   fibonacci(6) -> 8
 */
int fibonacci(int n)
{
    // 基线条件 1：n 为 0 或负数，返回 0
    if (n <= 0) {
        return 0;
    }
    // 基线条件 2：n 为 1，返回 1
    if (n == 1) {
        return 1;
    }
    // 递归步骤：F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2);
}

/**
 * 打印斐波那契数列前 n 项
 *
 * @param n 要打印的项数（正整数）
 */
void print_fibonacci(int n)
{
    // 参数校验：n 必须为正整数
    if (n <= 0) {
        printf("n 必须为正整数\n");
        return;
    }

    printf("斐波那契数列前 %d 项：\n", n);
    // 循环调用递归函数，依次打印 F(0) ~ F(n-1)
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
}

/**
 * 程序入口：从标准输入读取 n，打印斐波那契数列前 n 项
 *
 * @return 程序退出状态：0 正常，1 输入无效
 */
int main()
{
    int n;
    printf("请输入 n：");
    // 读取用户输入，校验是否为合法整数
    if (scanf("%d", &n) != 1) {
        printf("输入无效\n");
        return 1;
    }

    // 调用打印函数输出结果
    print_fibonacci(n);
    return 0;
}
