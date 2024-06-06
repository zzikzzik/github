#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char name[11];
    int score;
} Person;

void printScoreStars(Person* persons, int len){
    int stars = 0;
    for (int i=0;i<len;i++){
        stars = persons[i].score/5;
        printf("%s ",persons[i].name);
        for(int i=0;i<stars;i++){
            printf("*");
        }
        printf("\n");
    }
}

Person* Realloc(Person* persons,int len, int newLen){
    Person* newP = (Person*)malloc(newLen * sizeof(Person));
    for (int i=0;i<len;i++){
        newP[i] = persons[i];
    }
    free(persons);
    return newP;
}

int main(){
    Person* persons = NULL;
    int len = 0;
    int Score;
    char Name[11];
    //Name Score 를 입력받을것.
    while(1){
        scanf("%s %d", Name, &Score);
        if(!strcmp(Name,"END") && Score==0){
            break;
        }
        persons = Realloc(persons, len, len+1);
        strcpy(persons[len].name,Name);
        persons[len].score = Score;
        len += 1;
    }
    printScoreStars(persons, len);
    free(persons);
    return 0;
}