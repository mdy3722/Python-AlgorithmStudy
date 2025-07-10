n = 10      # 노드 수
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (4, 8),
    (4, 9),
    (5, 10)
]

node1 = 8
node2 = 10

# 가장 가까운 공통 조상을 찾기 위해서는
# 먼저 각 노드의 부모와 깊이를 기록해야 한다.
# 조상을 찾는 과정은 자신의 부모를 끌어올리면서 찾는 것이고
# 깊이를 기록해야 같은 깊이에서 끌어올리면서 공통을 찾을 수 있다.
# DFS를 이용해서 깊이 탐색을 하면 된다. -> 깊이: {키: 깊이}, 부모: {키: 부모}

def DFS(tree, start_node):      # DFS는 tree(graph)와 root(start_node)를 인자로 받는다.
  stack = [(start_node, 0)]     # 깊이도 같이 저장
  visited = set()
  depth = {start_node: 0}
  parent = {start_node: 0}

  while stack:
    current_node, d = stack.pop()
    visited.add(current_node)
    depth[current_node] = d

    for adj_node in tree[current_node]:
      if adj_node not in visited:
        parent[adj_node] = current_node

        stack.append((adj_node, d + 1))

  return depth, parent


# 주어진 간선을 통해 트리 구하기
def get_lca(n, edges, node1, node2):
  tree = {i: [] for i in range(1, n + 1)}
  childset = set()

  for parent, child in edges:
    tree[parent].append(child)
    tree[child].append(parent)
    childset.add(child)

  root = (set(tree.keys()) - childset).pop()
  
  depth, parent = DFS(tree, root)

  while depth[node1] > depth[node2]:
    node1 = parent[node1]

  while depth[node2] > depth[node1]:
    node2 = parent[node2]

  while node1 != node2:
    node1 = parent[node1]
    node2 = parent[node2]

  return node1

print(get_lca(n, edges, node1, node2))

n1 = 11
edges1 = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (4, 6),
    (5, 7),
    (5, 8),
    (3, 9),
    (9, 10),
    (9, 11)
]

node3 = 6
node4 = 8

print(get_lca(n1, edges1, node3, node4))








