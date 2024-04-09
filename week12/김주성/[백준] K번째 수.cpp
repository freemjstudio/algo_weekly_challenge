#include <iostream>
#include <algorithm> 

int main(void)
{
    int N, K;
    scanf("%d",&N);
    scanf("%d",&K);

    int start = 1;
    int end = K;
    int answer = K;

    while (start <= end)
    {
        int mid = (start+end)/2;
        int count = 0;

        for (int i=1;i<=N;i++) count += std::min(mid/i,N);
        if (count >= K)
        {
            end = mid-1;
            if (mid<answer) answer = mid;
        }
        else start = mid+1;
    }
    printf("%d", answer);
    return 0;
}