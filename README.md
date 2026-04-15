# Road to Google: Binary Trees & BST Patterns

This document contains Notion-style summary notes and Anki flashcards extrapolated from the 40+ tree problems solved sequentially.

---

## 📓 Notion Notes: Pattern Recognition

Instead of memorizing the exact logic for every problem, break them down into these overarching patterns. Whenever you see a new tree problem, run through this list.

### 1. The Core Duality: Top-Down (Pre-order) vs. Bottom-Up (Post-order)
Most recursive tree problems fall into one of two categories:

- **Top-Down (Pre-order) "State Passing"**: 
  - **Intuition**: The node needs to know something about its ancestors to do its job.
  - **Pattern**: You pass an accumulated value down the recursive stack. 
  - **Problems**: `branch_sums`, `node_depths`, `has_path_sum`.
  - **Code Structure**: `dfs(node, current_sum)` where `current_sum` is computed before calling left/right children.

- **Bottom-Up (Post-order) "Sub-tree Aggregation"**: 
  - **Intuition**: The node needs information from its descendants to do its job.
  - **Pattern**: You process the left child, process the right child, and then combine those results at the current node. 
  - **Problems**: `diameter_of_binary_tree`, `max_path_sum`, `height_balanced`.
  - **Code/Global State Trap**: Returning the linear single-path for the parent to use, while simultaneously updating a global `max_value` across the `left + right + current_node`.

### 2. The BFS Level-Order Tricks
- **Intuition**: Processing nodes in expanding concentric circles or level-by-level. Always backed by a `Queue` (e.g., `collections.deque`).
- **Standard BFS**: `tree_includes`, basic level orders.
- **The "Right/Left Side View"**: Take the last (or first) element of the queue at the end of every `for _ in range(len(q))` loop.
- **ZigZag Traversal**: Instead of array reversing, use a `deque` for the current level and append either to the left (`appendleft`) or right (`append`) based on a boolean flag that flips each level.

### 3. Modifying / Simultaneous Processing (Two Trees)
- **Intuition**: You are comparing or altering tree structures based on pairing nodes together.
- **Pattern**: Traverse both simultaneously. Base cases often involve checking if *both* are null, or *one* is null. 
- **Problems**: `merge_binary_tree`, `is_symmetric`, `same_BSTs`, `invert_bt`.

### 4. Graph Conversions & Pointers
- **Intuition**: A tree is a Directed Acyclic Graph. When asked to find nodes "at distance K" or navigate "up", standard tree traversals fail because they only go down.
- **Pattern**: 
  - Use an initial traversal (BFS/DFS) to add `parent` pointers to every node, OR build an adjacency list representing an undirected graph.
  - Run a BFS starting from the target node, treating `parent`, `left`, and `right` as valid outward paths, using a `visited` set to prevent infinite loops.
- **Problems**: `nodes_at_distance_k`, `successor_of_a_node`.

### 5. BST Invariants & Properties
BSTs give you free information. If you're doing an $O(N)$ full traversal on a standard BST problem, you are missing the trick.

- **In-order = Sorted Array**: 
  - Any problem asking for the "kth element", "smallest/largest elements", or "successor", relies on the fact that an iterative or recursive In-order traversal processes nodes continuously in ascending order. Stop early when you hit the `k`th element!
- **Binary Search Elimination**: 
  - Since Left < Node < Right, you drop half the tree continuously. Time complexity becomes $O(H)$ (Height of Tree).
  - Use an iterative `while node:` loop to avoid recursive stack overhead when simply searching or doing single-branch logic (e.g. `closest_to_BST`, `search_BST`, `delete_BST`).
- **Validation Ranges**: 
  - `validate_BST` is NOT just `left < node < right`. It's ensuring a node fits within an ancestral `[min_val, max_val]` bound. Pass this bound recursively top-down.

### 6. The Lowest Common Ancestor (LCA)
- **Generic BT LCA**: Post-order. Return the node if we find Target 1 or Target 2. If a node receives non-null values from *both* its left and right children, it is the LCA. If it only receives one, pass that single non-null value upwards.
- **BST LCA**: Top-down. If both target nodes are *smaller* than the current node, go left. If both are *larger*, go right. The *first* node you find where the targets split (one is smaller, one is larger) IS the LCA.

---

## 🗃️ Anki Flashcards for Pattern Recognition

**Card 1**
* **Front**: What is the traversal pattern and fundamental clue for “Top-Down” problems like `Branch Sums` or `Path Sum`?
* **Back**: **Pre-order Traversal**. The current node needs to know its ancestor's state. Pass an accumulated variable down the recursive calls (`dfs(node, running_sum)`).

**Card 2**
* **Front**: When a problem asks to find the `Diameter` or `Max Path Sum` covering any two nodes in a tree, what is the required pattern?
* **Back**: **Bottom-up Post-order Traversal**. You need to calculate the longest standalone path *through* the current node (`left + right + node.val`) to update a **global reference**, BUT return the max **single linear path** (`node.val + max(left, right)`) up to the parent.

**Card 3**
* **Front**: What is the most efficient data structure implementation for a `Zig-Zag Level Order` traversal?
* **Back**: A **Queue (collections.deque)** for standard BFS level sizing, AND an internal **Deque** for the current level's results. Toggle a boolean to either `append` or `appendleft` based on the zigzag direction.

**Card 4**
* **Front**: How do you solve queries that involve moving "Upwards" in a tree or finding `Nodes at Distance K`?
* **Back**: Trees are directed graphs. First, traverse the tree to build an undirected graph (adjacency list or adding `node.parent` properties). Then run **BFS** with a `visited` set starting from the target.

**Card 5**
* **Front**: What is the fundamental property of BST In-order Traversals, and what common problem variants use it?
* **Back**: In-order traversal of a BST yields a globally **sorted array/stream**. It is used to solve `Kth Smallest Element`, `Kth Largest`, or `In-order Successor` by maintaining a counter and stopping early.

**Card 6**
* **Front**: How do you implement `Validate BST`? What is the common pitfall?
* **Back**: Pitfall: Only checking `left.val < node.val < right.val` is insufficient. 
Correct Pattern: **Top-Down State Passing**. Maintain a `(min_bound, max_bound)` for every node. The root starts at `(-infinity, infinity)`. When going left, update the max bound. When going right, update the min bound.

**Card 7**
* **Front**: Describe the structural pattern for finding the Lowest Common Ancestor (LCA) in a normal Binary Tree.
* **Back**: **Bottom-up Post-order**. Return the target `p` or `q` if found. If a node receives non-null values from *both* its left and right subtrees, it is the LCA. If only one is non-null, bubble it upwards.

**Card 8**
* **Front**: Describe the structural pattern for finding the Lowest Common Ancestor (LCA) in a Binary Search Tree.
* **Back**: **BST Property Splitting**. Traverse iteratively. If both `p` and `q` are less than the node, move left. If both are greater, move right. The exact moment the values diverge (one smaller, one larger, or one equals the node itself), you have found the LCA.

**Card 9**
* **Front**: What is the optimal base time complexity for Single-path BST queries (Closest value, Search, Iterative insertions)?
* **Back**: Time: $\mathcal{O}(H)$ or $\mathcal{O}(\log N)$, Space: $\mathcal{O}(1)$. Done using a simple `while node:` loop, going left or right, effectively eliminating half the tree per loop. No recursive stack required.

**Card 10**
* **Front**: When comparing `Two Binary Trees` simultaneously (Symmetric Tree, Same Tree), what is the typical structure of the base cases?
* **Back**: 
1) Return True if *both* nodes are Null.
2) Return False if *one* node is Null (but the other isn't).
3) Return False if `node1.val != node2.val`.
