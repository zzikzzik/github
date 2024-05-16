#include <stdio.h>

typedef struct{
    int xpos;
    int ypos;
}Point;

Point getScale2xPoint(Point p){
    Point newP;
    newP.xpos = p.xpos * 2;
    newP.ypos = p.ypos * 2;
    return newP;
}

int main(){
    Point p;
    scanf("%d %d", &p.xpos, &p.ypos);
    Point newP = getScale2xPoint(p);
    printf("%d %d", newP.xpos, newP.ypos);
}