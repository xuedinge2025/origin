#include <stdio.h>
int main(){
    const int maxinput =100;
    int i;
    double number,average,sum=0.0;
    
    for (i=1;i<=maxinput;++i){
        printf("%d.输入数字：",i);
        scanf("%lf",&number);

        if (number<0.0){
            goto jump;
        }
        sum += number;
    }

jump:
    average = sum / (i-1);
    printf("Sim(总和)=%.2f\n",sum);
    printf("Average(平均值)=%.2f",average);

    return 0;
}