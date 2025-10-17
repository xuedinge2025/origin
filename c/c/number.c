#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    srand(time(0));
    int number=rand()%100+1;
    int count=0;
    int a=0;
    do{
        printf("请输入一到一百的数：");
        scanf("%d",&a);
        count++;
        if (a>number){
            printf("大了\n");
        }else if(a<number){
            printf("小了\n");
        }
    }while(a!=number);
    printf("你用了%d次机会猜出结果为%d",count,number);
    return 0;
}
