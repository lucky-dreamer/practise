#include <stdio.h>
#define ROW 9
#define LINE 9




void multipy(int row,int line);


int main(void)
{
multipy(ROW,LINE);
return 0;
}


void multipy(int row,int line)
{
int row_[]={1,2,3,4,5,6,7,8,9};
int line_[]={1,2,3,4,5,6,7,8,9};
int add_row;
int add_line;
for (add_row=1;add_row<=row;add_row++)
{
	for (add_line=1;add_line<=add_row;add_line++)
		{
			printf("%2d *%2d = %2d  ",line_[add_line-1],row_[add_row-1],row_[add_row-1]*line_[add_line-1]);
		}
printf("\n");
}

}
