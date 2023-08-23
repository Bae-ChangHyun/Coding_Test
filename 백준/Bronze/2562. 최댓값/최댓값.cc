#include<stdio.h>
int main(){
    int N=0,cnt=1,tmp=0,i=0,max=0;
	
	
	for(i=0;i<9;i++){
		scanf("%d",&tmp);
		if(i==0)
			max=tmp;
		if(tmp>max){
			max=tmp;
			cnt=i+1;
		}
	}
	printf("%d\n%d",max,cnt);
}