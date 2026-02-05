#include <stdio.h>

int main(void)
{
int num;
char eng;
char chi;
char eng_str[10];
char chi_str[10];
printf("please input a num:\n");
scanf("%d",&num);
printf("the value is %d,the zise id %zd\n",num,sizeof(num));
printf("please input a English character:\n");
scanf(" %c",&eng);
printf("the value is %c,the zise id %zd\n",eng,sizeof(eng));
printf("please input a Chinese cahracter:\n");
scanf(" %c",&chi);
printf("the value is %c,the zise id %zd\n",chi,sizeof(chi));
printf("please input a English str:\n");
scanf(" %s",eng_str);
printf("the value is %s,the zise id %zd\n",eng_str,sizeof(eng_str));
printf("please input a Chinese str:\n");
scanf(" %s",chi_str);
printf("the value is %s,the zise id %zd\n",chi_str,sizeof(chi_str));
printf("the value is %s,the zise id %zd\n","zhang",sizeof("zhang"));
return 0;
}
