#include <stdio.h>
int max(int a,int b){
    int ret;
    if(a>b){
        ret=a;
    }else{
        ret=b;
    }
    return ret;
}

int main(){
    int a,b;
    printf("分别输入a和b的值");
    scanf("%d %d",&a,&b);
    printf("max为%d",max(a,b));
    return 0;
}