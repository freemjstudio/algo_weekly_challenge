#include <iostream>

int L;
int lps[1000001];
char pattern[1000001];

int main()
{
    scanf("%d",&L);
    scanf("%s",&pattern);
    
    int idx = 0;
    lps[0] = 0;
    for (int i=1;i<L;i++)
    {
        while (idx>0 && pattern[i]!=pattern[idx]) idx=lps[idx-1];
        if (pattern[i]==pattern[idx]) lps[i]=++idx;
    }

    printf("%d ",L-lps[L-1]);
    return 0;
}