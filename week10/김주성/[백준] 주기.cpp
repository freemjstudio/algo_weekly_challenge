#include <iostream>

int N;
int lps[1000001];
char string[1000001];


int main()
{
    int testcase = 0;
    while(true)
    {
        testcase++;
        scanf("%d",&N);
        if (N == 0) break;
        scanf("%s",string);
        
        printf("Test case #%d\n", testcase);

        int idx = 0;
        for (int i=0;i<1000001;i++) lps[i] = 0;
        for (int i=1;i<N;i++)
        {
            while (idx>0 && string[i]!=string[idx]) idx=lps[idx-1];
            if (string[i]==string[idx]) lps[i]=++idx;
        }

        for (int i=0;i<N;i++) 
        {
            int string_length = i+1 - lps[i];
            if ((i+1)%string_length == 0 && (i+1)/string_length >= 2) printf("%d %d\n",i+1, (i+1)/string_length);
        }
        printf("\n");
    }
    return 0;
}