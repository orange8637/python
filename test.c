#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
	char c[3]={'A', 'B', 'C'};
	int n[10]={2, 2, 2, 2, 2, 1, 1, 1, 1, 0};
	srand(time(0));
	int count[3]={0};
	for(int i=0; i<10000000; i++)
	{
		int num=rand()%10;
		if(c[n[num]] == 'A')
			count[0]++;
		else if(c[n[num]] == 'B')
			count[1]++;
		else
			count[2]++;
	}
	for(int i=0; i<3; i++)
		printf("%lf\n",count[i]/10000000.0);
	return 0;
}
