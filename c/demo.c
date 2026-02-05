#include <stdio.h>


void practise_pointer(void){
int age = 37;   //varible and valure
int *address = &age; //pointer
printf("now print pointer:%p\n",*address); //print pointer
printf("now print value:%u\n",*address); //print valure
 

}





void pointer_arr(void){
int number[3] = {1,2,3};
printf("now use the pointer way to print the arr_default value:%u\n",*number);
printf("now move the pointer to access another value:%u\n",*(number + 1));
}






int main(void){
practise_pointer();
pointer_arr();
}
