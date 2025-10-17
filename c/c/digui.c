#include <stdio.h>
int sum(int n){
    if (n!=0)
        return n + sum(n-1);
    else
        return n;
}
int main(){
    int number,result;
    printf("请输入一个正整数：");
    scanf ("%d",&number);
    result=sum(number);
    printf("sum=%d",result);
    return 0;
}