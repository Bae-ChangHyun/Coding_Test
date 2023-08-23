#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int N=0,flag=0;
	
	scanf("%d",&N);
	
	if((N%4==0)&&(N%100!=0))
		flag=1;
	if(N%400==0)
		flag=1;
	
	printf("%d",flag);
	
	return 0;
}