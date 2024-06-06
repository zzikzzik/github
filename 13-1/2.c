#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//pArr 은 2중배열로 이뤄짐
//1줄이 n번째 문장임
char** Realloc(char** pArr, int size, int newSize){
    char** newP = (char**)malloc(newSize * sizeof(char*));
    for(int i=0;i<size;i++){
        newP[i] = (char*)malloc((strlen(pArr[i])+1)*sizeof(char));
        strcpy(newP[i],pArr[i]);
        free(pArr[i]);
    }
    free(pArr);
    return newP;
}

int inTheList(char** pArr, char* str, int size){
    for(int i=0;i<size;i++){
        if(!strcmp(pArr[i],str)){
            return 1;
        }
    }
    return 0;
}

int main(){
    char** pArr = NULL;
    int size = 0;
    char str[21];
    while(1){
        printf("Enter a word (Enter 'end' to quit): ");
        scanf("%s", str);
        if(!strcmp(str,"end")){
            break;
        }
        if(inTheList(pArr, str, size)){
            printf("This word already exists. Please enter another word.\n");
            continue;
        }
        pArr = Realloc(pArr,size,size+1);
        pArr[size] = (char*)malloc((strlen(str)+1)*sizeof(char));
        strcpy(pArr[size],str);
        size += 1;
    }
    printf("%d words in the list:\n",size);
    for(int i=0;i<size;i++){ printf("%s ", pArr[i]); }
    printf("\n");
    while(1){
        printf("Enter a word to search (Enter 'end'to quit): ");
        scanf("%s", str);
        if(!strcmp(str,"end")){
            break;
        }
        if(inTheList(pArr, str, size)){ printf("This word is in the list.\n"); }
        else{ printf("This word is NOT in the list.\n"); }
    }
    for(int i=0;i<size;i++){
        free(pArr[i]);
    }
    free(pArr);
}