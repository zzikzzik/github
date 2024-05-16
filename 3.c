#include <stdio.h>

void getSumDiff(int a, int b, int* pSum, int* pDiff){
    *pSum = a + b;
    *pDiff = a - b;
}

int main(){
    int a, b, sum, diff;
    int *pSum = &sum;
    int *pDiff = &diff;
    scanf("%d %d", &a, &b);
    getSumDiff(a, b, pSum, pDiff);
    printf("sum: %d\ndiff: %d", sum, diff);
}