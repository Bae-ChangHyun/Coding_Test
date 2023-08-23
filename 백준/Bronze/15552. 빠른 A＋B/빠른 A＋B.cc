#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int N=0,i=0,a=0,b=0;
	
	scanf("%d",&N);
	
	for(i=0;i<N;i++){
		scanf("%d %d",&a,&b);
		printf("%d\n",a+b);
	}
	
	return 0;
}