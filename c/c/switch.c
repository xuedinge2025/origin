#include <stdio.h>
int main()
{
    int grade;
    printf("请输入你的成绩");
    do
    {
        scanf("%d", &grade);
    } while ((grade > 100 || grade < 0) && printf("输入的成绩非法 请重新输入\n"));


    grade /= 10;
    switch (grade)
    {
    case 10:
    case 9:
        printf("A\n");
        break;
    case 8:
        printf("B\n");
        break;
    case 7:
        printf("C\n");
        break;
    default:
        printf("进厂吧");
        break;
    }
    return 0;
}
