#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int x=0,y=0,loc=0;
	
	scanf("%d",&x);
	scanf("%d",&y);
	
	if(x>0){
		if(y>0)
			loc=1;
		else
			loc=4;
	}
	else{
		if(y>0)
			loc=2;
		else
			loc=3;
	}
	
	printf("%d",loc);
	
	return 0;
}