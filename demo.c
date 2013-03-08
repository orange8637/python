#include<stdio.h>

int binary_search(int *data, int low, int high, int value)
{
	while(low <= high)
	{
		int mid = (low + high) / 2;
		if(data[mid] < value)
			low = mid + 1;
		else if(data[mid] > value)
			high = mid - 1;
		else
			return mid;
	}
	return -1;
}

int main()
{
	int d[10];
	for(int i=0; i<10; i++)
	{
		d[i] = i;
	}
	int n;
	while(scanf("%d", &n))
	{
		printf("%d\n", binary_search(d, 0, 9, n));
	}
	return 0;
}

