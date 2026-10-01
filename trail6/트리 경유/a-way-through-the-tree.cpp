#include <iostream>

#define MAX_N 1200000

using namespace std;

// 변수 선언
int n, q;
int colored[MAX_N + 1];

int LastColoredNode(int dest) {
    // 가는 길에 색칠된 노드가 없다면 0을 반환합니다.
    int ret = 0;

    while(dest) {
        // 해당 위치의 노드가 색칠되었다면 반환할 값을 갱신합니다.
        if(colored[dest]) 
            ret = dest;

        // dest에서 2를 나눠줄 때마다 자신의 부모 노드로 가게 됩니다.
        dest /= 2;
    }

    return ret;
}

int main() {
    // 입력:
    cin >> n >> q;

    // q개의 줄에 걸쳐 노드를 입력받습니다.
    while(q--) {
        int dest;
        cin >> dest;

        // 입력받은 노드를 따라 갈 때, 색칠된 노드가 있는지 확인합니다.
        int ans = LastColoredNode(dest);
        cout << ans << endl;

        // 만약 색칠된 노드가 없었다면 dest 노드에 색칠해줍니다.
        if(ans == 0) 
            colored[dest] = 1;
    }

    return 0;
}


