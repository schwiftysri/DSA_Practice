# Study Roadmap

Built from `reference/`, following labuladong's own article ordering (site ToC:
Chapter 0 Essential Techniques → Chapter 1 Data Structures → Chapter 2 Brute
Force Search → Chapter 3 Dynamic Programming → Chapter 4 Other Techniques).
Only local files present in `reference/` are included as drill topics; a few
non-DSA articles are listed separately at the bottom as optional reading.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` template/problems done

---

## Phase 0 — Essential Technique Frameworks
*(the core "building blocks" this whole repo drills — do these first, in order)*

- [ ] **Two Pointers** (array left/right + linked-list fast/slow)
  `reference/algorithmic-thinking/two-pointers.md`
  Prereq: none (first topic)

- [ ] **Sliding Window**
  `reference/algorithmic-thinking/sliding-window.md`
  Prereq: Two Pointers (sliding window = a fast/slow pointer pair with a window between them)

- [ ] **Binary Search**
  `reference/algorithmic-thinking/binary-search.md`
  Prereq: none, but drilled after two pointers/sliding window per site order

- [ ] **Backtracking Framework**
  `reference/algorithmic-thinking/backtracking.md`
  Prereq: basic tree/N-ary tree traversal (conceptual, no local article)

- [ ] **BFS Framework**
  `reference/algorithmic-thinking/bfs-framework.md`
  Prereq: Backtracking Framework (BFS is explained as level-order brute-force search, same "traverse the tree" mental model as DFS/backtracking)

- [ ] **Dynamic Programming Framework** (top-down recursion → memoization → bottom-up DP)
  `reference/dynamic-programming/dp-framework.md`
  Prereq: none structurally, but easiest after recursion/backtracking is comfortable

- [ ] **DP Optimal Substructure / FAQ** (dp array sizing, traversal direction, overlapping subproblems)
  `reference/dynamic-programming/optimal-substructure.md`
  Prereq: DP Framework

---

## Phase 1 — Data Structure Algorithms

### Linked List
- [ ] **Reverse Linked List (recursive tricks)**
  `reference/data-structures/reverse-linked-list.md`
  Prereq: Two Pointers

- [ ] **Palindrome Linked List**
  `reference/interview/palindrome-linked-list.md`
  Prereq: Reverse Linked List

### Array
- [ ] **2D Array / Matrix Traversal Tricks**
  `reference/algorithmic-thinking/matrix-traversal.md`
  Prereq: Two Pointers

- [ ] **Prefix Sum**
  `reference/algorithmic-thinking/prefix-sum.md`
  Prereq: none (basic array technique)

- [ ] **Difference Array**
  `reference/algorithmic-thinking/difference-array.md`
  Prereq: Prefix Sum (dual technique — diff array is to updates what prefix sum is to range queries)

- [ ] **Binary Search in Action** (practical problem patterns)
  `reference/interview/binary-search-in-action.md`
  Prereq: Binary Search

- [ ] **Weighted Random Selection**
  `reference/interview/random-weight.md`
  Prereq: Prefix Sum, Binary Search

### Stack / Queue
- [ ] **Queue/Stack Interconversion** (implement one with the other)
  `reference/data-structures/queue-stack.md`
  Prereq: none

- [ ] **Monotonic Stack** (Next Greater Element template)
  `reference/data-structures/monotonic-stack.md`
  Prereq: Queue/Stack basics

- [ ] **Monotonic Queue** (sliding window max/min)
  `reference/data-structures/monotonic-queue.md`
  Prereq: Queue/Stack basics, Sliding Window

### Binary Tree / BST
- [ ] **Binary Tree Recursion Mindset (Overview)**
  `reference/data-structures/binary-tree-summary.md`
  Prereq: none (foundational recursion framework — everything below depends on it)

- [ ] **Binary Tree in Action I**
  `reference/data-structures/binary-tree-practice1.md`
  Prereq: Binary Tree Summary

- [ ] **Binary Tree in Action II**
  `reference/data-structures/binary-tree-practice2.md`
  Prereq: Binary Tree in Action I

- [ ] **BST in Action I** (in-order / validate / search)
  `reference/data-structures/bst-part1.md`
  Prereq: Binary Tree Summary

- [ ] **BST in Action II** (insert / delete operations)
  `reference/data-structures/bst-part2.md`
  Prereq: BST in Action I

### Design Data Structures
- [ ] **LRU Cache**
  `reference/interview/lru-cache.md`
  Prereq: Queue/Stack, hash table basics

- [ ] **Implement a Calculator**
  `reference/data-structures/calculator.md`
  Prereq: Queue/Stack basics (stack-based expression evaluation)

### Graph
- [ ] **Union-Find (Disjoint Set)**
  `reference/algorithmic-thinking/union-find.md`
  Prereq: basic graph/N-ary tree concepts

- [ ] **Topological Sort**
  `reference/data-structures/topological-sort.md`
  Prereq: BFS Framework or Backtracking/DFS Framework

- [ ] **Dijkstra's Algorithm**
  `reference/data-structures/dijkstra.md`
  Prereq: BFS Framework (Dijkstra generalizes BFS shortest-path to weighted graphs)

- [ ] **The Celebrity Problem**
  `reference/interview/celebrity-problem.md`
  Prereq: basic graph concepts

---

## Phase 2 — Brute Force Search (DFS / Backtracking / BFS in Action)

- [ ] **Island Problems (DFS on grids)**
  `reference/interview/island-problems.md`
  Prereq: Backtracking Framework, Binary Tree Summary

- [ ] **Permutations / Combinations / Subsets**
  `reference/interview/subset-permutation-combination.md`
  Prereq: Backtracking Framework

- [ ] **Partition to K Equal Sum Subsets**
  `reference/algorithmic-thinking/set-partition.md`
  Prereq: Backtracking Framework

---

## Phase 3 — Dynamic Programming

### Subsequence Problems
- [ ] **Edit Distance**
  `reference/dynamic-programming/edit-distance.md`
  Prereq: DP Framework, DP Optimal Substructure

- [ ] **Longest Common Subsequence**
  `reference/dynamic-programming/longest-common-subsequence.md`
  Prereq: DP Framework

- [ ] **Subsequence Problem Patterns** (general dp[i][j] template)
  `reference/dynamic-programming/subsequence-problems.md`
  Prereq: Edit Distance, Longest Common Subsequence

### Knapsack & Backtracking→DP Conversion
- [ ] **Converting Backtracking to DP (Word Break)**
  `reference/dynamic-programming/word-break.md`
  Prereq: Backtracking Framework, DP Framework

- [ ] **Knapsack Problems (0-1 / subset / unbounded)**
  `reference/dynamic-programming/knapsack.md`
  Prereq: DP Framework

- [ ] **State Compression DP** (bitmask DP)
  `reference/dynamic-programming/state-compression.md`
  Prereq: DP Framework, Knapsack

### DP Games / Classic Problems
- [ ] **Dungeon / Magic Tower Problem**
  `reference/dynamic-programming/magic-tower.md`
  Prereq: DP Framework

- [ ] **Regular Expression Matching**
  `reference/dynamic-programming/regular-expression.md`
  Prereq: DP Framework, Edit Distance-style 2D dp

- [ ] **Super Egg Drop**
  `reference/dynamic-programming/egg-drop.md`
  Prereq: DP Framework, DP Optimal Substructure

- [ ] **Game Theory DP (Stone Game / Predict the Winner)**
  `reference/dynamic-programming/game-theory.md`
  Prereq: DP Framework

- [ ] **House Robber (I/II/III unified method)**
  `reference/dynamic-programming/house-robber.md`
  Prereq: DP Framework

- [ ] **Stock Buy/Sell Problems (unified state machine)**
  `reference/dynamic-programming/stock-problems.md`
  Prereq: DP Framework

### Greedy (special case of DP)
- [ ] **Interval Scheduling (Greedy)**
  `reference/dynamic-programming/interval-scheduling.md`
  Prereq: DP Framework (article frames greedy as a special, faster case of DP)

- [ ] **Meeting Rooms II (Scan Line Technique)**
  `reference/interview/meeting-rooms.md`
  Prereq: Interval Scheduling

---

## Phase 4 — Other Common Techniques

### Math
- [ ] **Bit Manipulation Tricks**
  `reference/algorithmic-thinking/bit-manipulation.md`
  Prereq: none

- [ ] **Missing / Duplicate Element**
  `reference/interview/missing-duplicate-element.md`
  Prereq: Bit Manipulation Tricks

- [ ] **Counting Primes Efficiently**
  `reference/interview/count-primes.md`
  Prereq: none

- [ ] **Probability Problems**
  `reference/algorithmic-thinking/probability-problems.md`
  Prereq: none

- [ ] **String Multiplication**
  `reference/algorithmic-thinking/string-multiplication.md`
  Prereq: none

- [ ] **Pancake Sorting**
  `reference/algorithmic-thinking/pancake-sorting.md`
  Prereq: none (recursive divide-style sorting trick)

### Classic Interview Problems
- [ ] **Trapping Rain Water**
  `reference/interview/trapping-rain-water.md`
  Prereq: Two Pointers

---

## Supplementary Reading (optional — not core DSA drills)

These exist in `reference/` but are outside labuladong's core DSA-technique
sequence (general CS background or meta/contribution docs). Read opportunistically,
not part of the drill loop:

- `reference/technical/problem-solving-tips.md` — how to practice LeetCode effectively
- `reference/technical/cryptography.md` — modern encryption intro
- `reference/technical/session-and-cookie.md` — web session/cookie fundamentals
- `reference/technical/linux-process.md` — Linux processes/threads/fds
- `reference/technical/linux-shell.md` — shell tips
- `reference/multi-language-solutions/contribution-guide.md` — repo contribution guide (meta, not a lesson)
- `reference/multi-language-solutions/solution_code.md` — misc translated solution notes (meta, not a lesson)

---

## Notes
- Phases are ordered per labuladong's site structure (see `reference/README.md`
  Table of Contents); within each phase, topics are ordered by their stated
  prerequisites (each file's own `::: info Prerequisites` block was checked).
- Update the checkboxes as drills/problems are completed; log recurring
  mistakes in `progress.md` under "Common Errors" per topic (see CLAUDE.md).
