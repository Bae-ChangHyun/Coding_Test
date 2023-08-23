#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int N=0,i=0,j=0;
	
	scanf("%d",&N);
	for(i=0;i<N;i++){
		for(j=0;j<i+1;j++){
			printf("*");
		}
		printf("\n");
	}
	
	return 0;
}