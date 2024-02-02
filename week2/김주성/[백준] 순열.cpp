#include <iostream>
#include <vector>

std::vector<int> tree;

int init(int node, int start, int end){
    if (start == end)
        return tree[node] = 1;
    int mid = (start+end)/2;

    return tree[node] = init(node*2,start,mid)+init(node*2+1,mid+1,end);
}

void Update(int node, int start, int end, int idx){
    if (idx < start || idx > end) return;
    tree[node]--;

    if (start!=end){
        int mid = (start+end)/2;
        Update(node*2,start,mid,idx);
        Update(node*2+1,mid+1,end,idx);
    }
}

int find_Idx(int node, int start, int end, int n){   
    if (start == end) return start;
    int mid = (start+end)/2;
    int left_sum = tree[node*2];
    if (left_sum >= n) return find_Idx(node*2,start,mid,n);
    else return find_Idx(node*2+1, mid+1, end, n-left_sum);
}

int main(){
    int N, idx, count_bigger_num;
    scanf("%d", &N);
    int arr[N];
    int tree_size = 4*N;

    tree.resize(tree_size);
    init(1,0,N-1);

    for (int i=1;i<=N;i++){
        scanf("%d", &count_bigger_num);
        idx = find_Idx(1,0,N-1,count_bigger_num+1);
        arr[idx] = i;
        Update(1, 0, N-1, idx);
    }
    
    for (int i=0;i<N;i++) printf("%d\n", arr[i]);
    return 0;
}