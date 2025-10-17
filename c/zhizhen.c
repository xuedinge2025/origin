#include <stdio.h>
int main(){
int *pc,c,d;
c=5;
d=-15;
pc=&c;printf("%d\n",*pc);
pc=&d;printf("%d %d",*pc,c);
return 0;

}