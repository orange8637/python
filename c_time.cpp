/*
* Filename: c_time.cpp
* Last modified: 2012-08-17 23:56
* Author: Chen Jiang(姜晨) -- orange8637@gmail.com
* Description: 计算CPU运行时间
*/
#include<iostream>
#include<time.h>
using namespace std;

int main()
{
	clock_t t1, t2;
	t1 = clock();
	for(int i=0; i<100000000; i++)
		;
	t2 = clock();
	cout<<(double)(t2-t1)/CLOCKS_PER_SEC<<endl;
	long long t = time(0);// get real time
	cout<<t<<endl;

	return 0;
}
