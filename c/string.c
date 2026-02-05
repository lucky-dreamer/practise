#include <stdio.h>


#define REPLY "you are good"

int main(void){
char name[40];
printf("what is your name?");
scanf("%s",name);
printf("Hello,%s,%s\n",name,REPLY);


return 0;
}
