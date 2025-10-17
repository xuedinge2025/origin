#include <stdio.h>
#include <limits.h>
#include <stddef.h>
void compare_types() {
    printf("=== size_t 与 int 的基本区别 ===\n");
    printf("sizeof(size_t): %zu 字节\n", sizeof(size_t));
    printf("sizeof(int):    %zu 字节\n", sizeof(int));
    
    printf("\n取值范围:\n");
    printf("int 最小值: %d\n", INT_MIN);
    printf("int 最大值: %d\n", INT_MAX);
    printf("size_t 最大值: %zu\n", SIZE_T_MAX);
    
    printf("\n符号性:\n");
    printf("int:    有符号类型（可正可负）\n");
    printf("size_t: 无符号类型（只能非负）\n");
}

