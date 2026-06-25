#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c;
    double discriminant, root1, root2, realPart, imagPart;

    printf("求解一元二次方程 ax^2 + bx + c = 0\n");
    printf("请输入系数 a, b, c（空格分隔）: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    // 判断是否为二次方程
    if (a == 0) {
        if (b == 0) {
            if (c == 0) {
                printf("无穷多解（任意 x 都满足）\n");
            } else {
                printf("无解\n");
            }
        } else {
            root1 = -c / b;
            printf("这是一元一次方程，解为: x = %.4f\n", root1);
        }
        return 0;
    }

    discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        // 两个不相等的实根
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("方程有两个不相等的实根:\n");
        printf("  x1 = %.4f\n", root1);
        printf("  x2 = %.4f\n", root2);
    } else if (discriminant == 0) {
        // 两个相等的实根
        root1 = -b / (2 * a);
        printf("方程有两个相等的实根:\n");
        printf("  x1 = x2 = %.4f\n", root1);
    } else {
        // 两个共轭复根
        realPart = -b / (2 * a);
        imagPart = sqrt(-discriminant) / (2 * a);
        printf("方程有两个共轭复根:\n");
        printf("  x1 = %.4f + %.4fi\n", realPart, imagPart);
        printf("  x2 = %.4f - %.4fi\n", realPart, imagPart);
    }

    return 0;
}
