#include <stdio.h>
#include <stdlib.h>
int main(){
    int size=5;
    size_t total_bytes=size*sizeof(int);
    void *raw_ptr=malloc(total_bytes);
    if(raw_ptr==NULL){
        printf("分配失败\n");
        return 1;
    }
    int *ptr = (int*)raw_ptr;
    printf("int指针%p\n",ptr);
    for(int i=0;i<size;i++){
        ptr[i]=i*10;
        printf("ptr[%d]=%d(地址:%p)\n",i,ptr[i],&ptr[i]);
        printf("地域差值：%td 字节\n",(char*)&ptr[1]-(char*)&ptr[0]);
        free(ptr);
        return 0;
    }
}