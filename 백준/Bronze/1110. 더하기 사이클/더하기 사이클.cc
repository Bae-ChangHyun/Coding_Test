#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 


int main()
{
	int N=0,a=0,b=0,res=0,tmp=0,cnt=0;
	
	scanf("%d",&N);
	tmp=N;
	
	while(1){
		if(N<10){
			a=0;
			b=N;
		}
		else{
			b=N%10;
			a=N/10;
		}
		res=a+b;
		N=b*10+res%10;
		cnt++;
		if(N==tmp){
			printf("%d",cnt);
			break;
		}
	}
	
	return 0;
}
