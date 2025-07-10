'''
어려운 문제제

루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요

[입력]
첫 줄에 테스트 케이스의 개수 T가 주어집니다.
각 테스트 케이스마다, 첫째 줄에 트리를 구성하는 노드의 수 N이 주어집니다. (2 ≤ N ≤ 10,000)
그리고 그 다음 N-1개의 줄에 트리를 구성하는 간선 정보가 주어집니다.
한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻입니다. (당연히 정점이 N개인 트리는 항상 N-1개의 간선으로 이루어집니다!)
A와 B는 1 이상 N 이하의 정수로 이름 붙여집니다.
테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.

각 테스트 케이스 별로, 첫 줄에 입력에서 주어진 두 노드의 가장 가까운 공통 조상을 출력합니다.

ex)
[입력]
1
5
2 3
3 4
3 1
1 5
3 5

[출력]
3

2->3->4
    ->1->5

깊이를 탐색? DFS를 떠올려라

tree = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

위 그래프는 간선만 주어졌을 때 표현할 수 있는 방식이다.
이 문제는 입력으로 간선이 들어오므로, 주어진 그래프를 표현 가능하다.

이를 위해 각 노드의 부모를 저장하고, 가장 가까운 공통 부모를 찾기 위해 깊이를 저장해야 함
각 노드의 부모를 저장하는 딕셔너리 => parent = {키: 부모}
각 노드의 깊이를 저장하는 딕셔너리 => depth = {키: 깊이}

'''

import sys

# DFS 순회하면서 각 노드의 부모와 깊이 저장
def dfs(tree, root):
  stack = [(root,0)]    # 시작 노드와 깊이를 같이 저장
  visited = set()       # []가 아닌 set으로 해도 됨. 어차피 중복 불가니까
  parent = {root: 0}
  depth = {root: 0}

  while stack:
    current, d = stack.pop()      # 루트의 깊이는 0
    visited.add(current)          # set형이므로 자료를 투가할 때 add
    depth[current] = d

    for adj_node in tree[current]:
      if adj_node not in visited:
        parent[adj_node] = current      # 루트부터 간선을 타고 내려오니까 visited not in 확인을 통해 adj_node가 자식인 것을 확인할 수 있다.
        stack.append((adj_node, d + 1))         # 여기서 stack에 append할 때 자식이니까 현재 d에서 +1

  return parent, depth

'''입력처리 백준'''
# 트리 만드는 중
count_testcase = int(sys.stdin.readline())

for _ in range(count_testcase):
  n = int(sys.stdin.readline())     # node 수
  tree = {i: [] for i in range(1, n+1)}

  child_set = set()       # 루트 노드를 찾아내기 위해 자식들을 set에..

  for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    # 무방향
    tree[a].append(b)
    tree[b].append(a)
    child_set.add(b)
  
  x, y = map(int, sys.stdin.readline().split())       # 정답을 구해야 할 두 노드

  # 루트 구하기 : set(tree.keys()) - 전체 노드 집합, child_set - 전체 자식 노드 집합
  root = (set(tree.keys()) - child_set).pop()       # 반드시 pop()까지 할 것!

  # DFS를 이용해, 부모와 깊이를 저장
  parent, depth = dfs(tree, root)

  # 공통 조상을 찾아야 하니 깊이를 먼저 맞추자.
  while depth[x] > depth[y]:      # x가 더 깊다면
    x = parent[x]       # x를 부모로 끌어올림

  while depth[y] > depth[x]:    # y도 마찬가지로 진행
    y = parent[y]

  while x != y:       # x와 y의 부모를 끌어올리면서 제일 가까운 공통 조상 찾기
    x = parent[x] 
    y = parent[y]

  print(x)



