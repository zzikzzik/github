#include <stdio.h>
#include <string.h>

typedef struct{
    char name[7];
    int score;
}Person;

void printScoreStars(Person* persons, int len){
    for (int i=0;i<len;i++){
        int strLen = strlen(persons[i].name);
        printf("%s", persons[i].name);
        for(int i=0;i<(7-strLen);i++){
            printf(" ");
        }
        int stars = persons[i].score/5;
        for(int i=0;i<stars;i++){
            printf("*");
        }
        printf("\n");
    }
}

int main(){
    Person people[3];

    for(int i=0;i<3;i++){
        scanf("%s %d", &people[i].name, &people[i].score);
    }
    Person* pPeople = &people;
    printScoreStars(pPeople, (int)(sizeof(people)/sizeof(Person)));
}