#include <stdio.h>

/*
 * 求解二元一次方程组:
 *   a1*x + b1*y = c1
 *   a2*x + b2*y = c2
 */

int main() {
    double a1, b1, c1;
    double a2, b2, c2;
    double det, x, y;

    printf("二元一次方程组求解\n");
    printf("形式: a1*x + b1*y = c1\n");
    printf("      a2*x + b2*y = c2\n\n");

    printf("请输入 a1 b1 c1 (空格分隔): ");
    scanf("%lf %lf %lf", &a1, &b1, &c1);

    printf("请输入 a2 b2 c2 (空格分隔): ");
    scanf("%lf %lf %lf", &a2, &b2, &c2);

    det = a1 * b2 - a2 * b1;

    if (det == 0) {
        // 判断是无穷多解还是无解
        if (a1 * c2 == a2 * c1 && b1 * c2 == b2 * c1) {
            printf("\n方程组有无穷多解。\n");
        } else {
            printf("\n方程组无解。\n");
        }
    } else {
        x = (c1 * b2 - c2 * b1) / det;
        y = (a1 * c2 - a2 * c1) / det;
        printf("\n解为: x = %.4f, y = %.4f\n", x, y);
    }

    return 0;
}
