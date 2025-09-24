#define _GUN_SOURCE
#include <stdlib.h>
#include <unistd.h>


int main(int argc, char *argv[]){

setuid(0);
setgid(0);

char command[1024];

snprintf(command,sizeof(command),"/bin/bash /home/mateng/my_scripts/sudo_tools");

for (int i=1;i< argc;i++){
	strcat(command, " ");
	strcat(command, argv[i]);
	
}


system(command);

return 0;
}
