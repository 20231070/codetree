n = int(input())
pre_order = [int(input()) for _ in range(n)]

def postorder(start, end):
    if start > end:
        return

    root = pre_order[start]
    idx = end + 1  # 오른쪽 서브트리가 없을 수도 있으므로 초기값 설정

    # 루트보다 처음으로 커지는 지점(오른쪽 서브트리의 시작점)을 탐색
    for i in range(start + 1, end + 1):
        if pre_order[i] > root:
            idx = i
            break

    # 1. 왼쪽 서브트리 탐색
    postorder(start + 1, idx - 1)

    # 2. 오른쪽 서브트리 탐색
    postorder(idx, end)

    # 3. 루트 노드 출력
    print(root)

if pre_order:
    postorder(0, len(pre_order) - 1)