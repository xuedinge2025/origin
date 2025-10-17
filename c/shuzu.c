#include <stdio.h>
float Sum(float age[]){
    float sum =0.0;
    for (int i=0;i<6;i++){
        sum+=age[i];
    }return sum;
}
int main(){
    float result,age[]={23.4,55,22.6,3,40.5,18};
    result =Sum(age);
    printf("结果=%.2f",result);
    return 0;
}