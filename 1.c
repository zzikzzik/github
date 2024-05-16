#include <stdio.h>

typedef struct{
    char name[10];
    int age;
}Point;

int main(){
    Point person;
    scanf("%s %d", &person.name, &person.age);
    printf("name: %s\nage: %d", person.name, person.age);
}