#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int A=0,B=0;
	
	scanf("%d %d",&A,&B);
	
	if(A>B)
		printf(">");
	else if(A<B)
		printf("<");
	else
		printf("==");
	
	return 0;
}