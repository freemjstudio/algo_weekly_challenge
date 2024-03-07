#include <iostream>

int n;
int lps[1000000];
char pattern[1000000];
char text[2000000];

void get_pattern()
{
    int idx = 0;
    lps[0] = 0;
    for (int i=1;i<n;i++)
    {
        while (idx > 0 && pattern[i] != pattern[idx]) idx = lps[idx-1];

        if (pattern[i] == pattern[idx])
        {
            idx++;
            lps[i] = idx;
        }
    }
}

int KMP()
{
    int idx = 0;
    int answer = 0;
    for (int i=0;i<n*2-1;i++)
    {
        while (idx > 0 && text[i] != pattern[idx]) idx = lps[idx-1];
        if (text[i] == pattern[idx])
        {
            if (idx == n-1)
            {
                answer++;
                idx = lps[idx];
            }
            else idx++;
        }
    }
    return answer;
}

int main()
{
    scanf("%d", &n);
    for (int i=0;i<n;i++) scanf(" %c", &pattern[i]);
    for (int i=0;i<n;i++) 
    {
        char c;
        scanf(" %c", &c);
        text[i] = c;
        text[i+n] = c;
    }
    get_pattern();

    int possible = KMP();
    while (possible != 1 && n%possible == 0)
    {
        n /= possible;
        possible /= possible;
    }
    printf("%d/%d", possible, n);
    return 0;
}