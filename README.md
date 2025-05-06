# -DMOPC-15-Contest-2-P4---Personal-Assistant
The solution and its explanation to the problem: [https://dmoj.ca/problem/dmopc15c2p4](https://dmoj.ca/problem/dmopc15c2p4). Below is a copy of explanation.md:

# Why Does the DP + Binary Search Solution Work?

## Problem
[https://dmoj.ca/problem/dmopc15c2p4](https://dmoj.ca/problem/dmopc15c2p4)

## Problem Recap
Given a list of animes, each with a release time \(R_i\), length \(L_i\), and happiness value \(H_i\), you want to select a subset to maximize total happiness. You can only start an anime at its release time, and if you watch it, you cannot watch any anime that starts before you finish it.

## Approach Overview
This is a classic **Weighted Interval Scheduling** problem, which can be solved efficiently using **Dynamic Programming (DP)** combined with **binary search**.

## DP State Definition
Let:
- \(dp[i]\) = the maximum happiness achievable by considering animes up to and including the one that ends at time \(end_i\), which is the i-th anime in the sorted list by end time.

## DP Transition
For each anime \(i\):
- You have two choices:
    1. **Skip** anime \(i\): dp[i] = dp[i-1] \( The maximum happiness is the same as the previous's\)
    2. **Watch** anime \(i\):
        - Add its happiness \(H_i\)
        - Find the last anime \(j\) that ends **before** anime \(i\) starts (i.e., \(end_j < R_i\)). This ensures no overlap of animes
        - If no such \(j\) exists, use \(H_i\) alone.
- So we compare the two choices:
    - If j exists: \(dp[i] = \max(dp[i-1], dp[j] + H_i)\) 
    - If j does not exist: \(dp[i] = \max(dp[i-1], H_i)\)

## Why Binary Search?
- Since animes are sorted by end time, binary search can be used to efficiently find the last non-overlapping anime for each \(i\).
- This reduces the time complexity from \(O(N^2)\) to \(O(N \log N)\).

## Why Is This Correct?
- The DP state ensures that at each step, you are making the optimal choice (either skipping or taking the current anime) based on all previous possibilities.
- By always considering the last non-overlapping anime, you guarantee that no two selected animes overlap.
- The recurrence covers all possible valid subsets.

## Efficiency
- **Sorting:** \(O(N log N)\)
- **DP with Binary Search:** For each anime, binary search is \(O(\log N)\), so for n animes, the total is \(O(N log N)\).
- **Total:** \(O(N log N)\)

# Why Must We Sort by End Time?

Sorting by end time is essential in this dynamic programming solution for several reasons:

---

## 1. Correctness of the DP Recurrence

The DP state is defined as:
- `dp[i]` = the maximum happiness achievable by considering animes up to and including the one that ends at time `end_i` (the i-th anime in the sorted list).

To ensure that when you consider anime `i`, all possible non-overlapping previous animes (those that end before anime `i` starts) are already considered and their optimal solutions are stored in `dp[j]`, you must process animes in order of their end times.

---

## 2. Efficient Binary Search

When animes are sorted by end time, you can use binary search to quickly find the last anime that ends before the current anime starts. This is crucial for the efficiency of the algorithm, reducing the time complexity from O(N²) to O(N log N).

---

## 3. Avoiding Overlaps

By always considering animes in order of their end times, you guarantee that when you select an anime, you only ever look back at animes that could possibly be non-overlapping. This prevents the possibility of accidentally including overlapping animes in your optimal subset.

Thus, if we did not sort by end time, the DP recurrence would not work as intended, and we could miss optimal solutions or include overlapping intervals.
