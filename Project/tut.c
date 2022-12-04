// #include <stdio.h>

// int main()
// {

//     int n;
//     scanf("%d", &n);
//     for (int i = 0; i < n; i++)
//     {
//         int a, b, c;
//         scanf("%d%d%d", &a, &b, &c);
//         int ary[6] = {b, c, b * 10 + b, b * 10 + c, c * 10 + b, c * 10 + c};
//         int m = 0;
//         for (int j = 0; j < 6; j++)
//         {

//             if (a >= ary[j])
//             {
//                 m = 1;
//                 printf("%d\n", ary[j]);
//             }
//             if (m == 0)
//             {
//                 printf("None\n");
//             }
//         }
//     }

//     return 0;
// }
#include <stdio.h>

int main()
{
    int a = 10, b = 15, n = 10;
    int c = b - a, total = a;
    for (int i = 1; i < n; i++)
    {
        b = c * i + a;
        total = total + b;
        printf("%d\n", b);
        a = b;
    }
    printf("\n");
    printf("%d\n", total);

    return 0;
}