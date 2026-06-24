/**
 * factorial.c
 * 求一个整数的阶乘
 *
 * 阶乘定义：
 *   0! = 1
 *   n! = n * (n-1) * (n-2) * ... * 1   (n >= 1)
 *
 * 示例：
 *   0! -> 1
 *   1! -> 1
 *   5! -> 120
 *   10! -> 3628800
 *
 * 注意：阶乘增长极快，32 位 int 只能容纳到 12!，
 *       超出范围会发生溢出。如需更大阶乘请使用 long long 或大数库。
 */

#include <stdio.h>

/**
 * 递归计算 n 的阶乘
 *
 * @param n 非负整数
 * @return n! 的值；n 为负数时返回 -1 表示非法输入
 *
 * 示例：
 *   factorial(0) -> 1
 *   factorial(1) -> 1
 *   factorial(5) -> 120
 */
long long factorial(int n)
{
    // 非法输入：负数无阶乘定义
    if (n < 0) {
        return -1;
    }
    // 基线条件：0! = 1
    if (n == 0) {
        return 1;
    }
    // 递归步骤：n! = n * (n-1)!
    return (long long)n * factorial(n - 1);
}

/**
 * 程序入口：从标准输入读取 n，输出 n 的阶乘
 *
 * @return 程序退出状态：0 正常，1 输入无效
 */
int main()
{
    int n;
    printf("请输入一个非负整数 n：");
    // 读取用户输入，校验是否为合法整数
    if (scanf("%d", &n) != 1) {
        printf("输入无效\n");
        return 1;
    }

    // 调用阶乘函数
    long long result = factorial(n);
    if (result < 0) {
        printf("负数没有阶乘定义\n");
        return 1;
    }

    // 输出结果
    printf("%d! = %lld\n", n, result);
    return 0;
}
