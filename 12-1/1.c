#include <stdio.h>

const double PI = 3.141592;
int main(){
    double r;
    scanf("%lf", &r);
    printf("Perimeter: %lf\nArea: %lf", 2*PI*r, PI*r*r);
}