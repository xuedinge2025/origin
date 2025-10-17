//
//  main.c
//  c
//
//  Created by 学定饿 on 2025/9/5.
//

#include <stdio.h>
int main()
{   int hour1,hour2;
    int minute1,minute2;
    scanf("%d %d",&hour1,&minute1);
    scanf("%d %d",&hour2,&minute2);
    int ih = hour2-hour1;
    int im =minute2-minute1;
    if(im<0){
        im=60+im;
        ih --;
    }
    
    printf("时间差为%d时%d分",ih,im);
    return 0;
    
    
    
    
}
