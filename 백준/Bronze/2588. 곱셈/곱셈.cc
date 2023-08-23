#include <stdio.h> 
#include <string.h>
#include <stdlib.h>
 

int main(){
	
	int a=0,b=0,c=0,res=0;
	
	scanf("%d %d",&a,&b);
	
	c=a*(b%10);
	printf("%d\n",c);
	b=b/10;
	res=res+c;
	
	c=a*(b%10);
	printf("%d\n",c);
	b=b/10;
	res=res+10*c;
	
	c=a*b;
	printf("%d\n",c);
	res=res+c*100;
	
	printf("%d",res);
	
	return 0;
}