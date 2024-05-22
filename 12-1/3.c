#include <stdio.h>

void printString(const char* str){
    printf("%s\n", str);
}

int main(){
    const char* arr[3] = {"One", "Two", "Three"};
    void (*fp)(const char*) = printString;
    for(int i=0;i<3;i++){
        fp(arr[i]);
    }
}