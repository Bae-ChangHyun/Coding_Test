#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int h=0,m=0;
	
	scanf("%d %d",&h,&m);
	
	if(m<45){
		h=h-1;
		m=m+60;
	}
	
	if(h<0)
		h=h+24;
	
	printf("%d %d",h,m-45);
	
	return 0;
}