#include <stdio.h>

// 递归计算斐波那契数列第 n 项（n 从 0 开始）
// F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
int fibonacci(int n)
{
    if (n <= 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// 打印斐波那契数列前 n 项
void print_fibonacci(int n)
{
    if (n <= 0) {
        printf("n 必须为正整数\n");
        return;
    }

    printf("斐波那契数列前 %d 项：\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");
}

int main()
{
    int n;
    printf("请输入 n：");
    if (scanf("%d", &n) != 1) {
        printf("输入无效\n");
        return 1;
    }

    print_fibonacci(n);
    return 0;
}
