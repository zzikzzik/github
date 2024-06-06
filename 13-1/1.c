#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int xpos;
    int ypos;
} Point;

int main(){
    Point* pP = (Point*)malloc(sizeof(Point));
    scanf("%d %d", &(pP->xpos), &(pP->ypos));
    printf("%d %d", pP -> xpos, pP -> ypos);
    free(pP);
    return 0;
}