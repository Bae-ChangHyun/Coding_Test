#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int N=0,X=0,i=0,A=0;
	
	scanf("%d %d",&N,&X);
	for(i=0;i<N;i++){
		scanf("%d",&A);
		if(A<X)
			printf("%d ",A);
	}
	
	return 0;
}