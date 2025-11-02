
#include <stdio.h> 
int main(){
    int a;
    scanf("%d",&a);
    int q=a%10;
    int w=a/10%10;
    int e=a/100;
    int r=q*100+w*10+e;
    printf("%d",r);
    return 0;
}
