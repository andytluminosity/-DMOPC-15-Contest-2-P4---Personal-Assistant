import bisect
import sys
from io import StringIO

# Problem: https://dmoj.ca/problem/dmopc15c2p4

# This problem is a classic Weighted Interval Scheduling problem.
# The goal is to select a subset of non-overlapping animes to maximize total happiness.
# We use dynamic programming (DP) and binary search for efficiency.
def max_happiness():
    n = int(input())
    animes = []
    for _ in range(n):
        R, L, H = map(int, input().split())
        # Store each anime as (start, end, happiness)
        animes.append((R, R + L - 1, H))
    # Sort animes by end time to facilitate DP and binary search
    animes.sort(key=lambda x: x[1])
    # Prepare a list of end times for binary search
    ends = [anime[1] for anime in animes]
    # dp[i] = max happiness achievable considering animes up to i (by end time)
    dp = [0] * n
    for i in range(n):
        R, end, H = animes[i]
        # Find the last anime that ends before the current anime starts
        # This ensures no overlap
        j = bisect.bisect_right(ends, R - 1) - 1
        # Two choices:
        # 1. Skip this anime: dp[i-1]
        # 2. Take this anime: dp[j] + H (if j >= 0, aka. an anime was found by binary search), else just H
        
        # Compare the two choices
        if j >= 0:
            dp[i] = max(dp[i - 1] if i > 0 else 0, dp[j] + H) # Compare choices 1 and 2 and take the maximum of the two
        else:
            dp[i] = max(dp[i - 1] if i > 0 else 0, H) # Compare choices 1 and 2 and take the maximum of the two
        # The DP recurrence ensures we always have the optimal solution up to anime i
    # The answer is the maximum happiness achievable up to the last anime
    print(dp[-1])

# Test runner for sample cases
# This is for validation and not part of the competitive solution
# It simulates input and checks output for correctness

def run_tests():
    # List of test cases: each is a tuple (input_string, expected_output)
    samples = [
        # Provided samples
        ("5\n1 2 3\n2 1 5\n3 1 3\n4 2 4\n5 1 5", 13),
        ("4\n1 5 6\n1 3 4\n1 7 5\n4 10 3", 7),
        ("6\n1 1000000000000 1000000000000\n99999 9999 99999\n123456 789 101112\n416647 133337 100000000\n416647 1 9988776655\n9999999999 9999999999 9999999999", 1000000000000),
        # New test cases
        # 1. All non-overlapping
        ("3\n1 2 10\n4 2 20\n7 2 30", 60),
        # 2. All overlapping, only one can be chosen (pick max H)
        ("4\n1 10 5\n2 10 15\n3 10 25\n4 10 10", 25),
        # 3. Single anime
        ("1\n5 3 42", 42),
        # 4. Large gap between animes
        ("2\n1 2 10\n100 2 20", 30),
        # 5. Zero happiness values
        ("3\n1 2 0\n4 2 0\n7 2 0", 0),
        # 6. Overlapping with zero happiness (should skip zero)
        ("3\n1 5 0\n2 2 10\n5 2 20", 30),
        # 7. Multiple optimal solutions (same max happiness)
        ("3\n1 2 10\n3 2 10\n5 2 10", 30),
        # 8. All animes start at the same time (pick max H)
        ("4\n1 2 5\n1 2 10\n1 2 15\n1 2 7", 15),
        # 9. Animes with length 1
        ("5\n1 1 1\n2 1 2\n3 1 3\n4 1 4\n5 1 5", 15),
        # 10. Animes with increasing happiness but overlapping
        ("4\n1 5 1\n2 5 2\n3 5 3\n4 5 10", 10),
    ]
    for idx, (input_str, expected) in enumerate(samples, 1):
        sys.stdin = StringIO(input_str)
        # Print the test case number for clarity
        print(f"Test Case {idx}")
        # Print the input in a readable, multi-line format
        print("Input:")
        lines = input_str.strip().split('\n')
        for line in lines:
            print(line)
        # Print the expected output for the test case
        print(f"Expected Output:\n{expected}")
        try:
            old_stdout = sys.stdout
            sys.stdout = StringIO()
            # Run the solution and capture its output
            max_happiness()
            result = sys.stdout.getvalue().strip()
            sys.stdout = old_stdout
            # Print the computed output from the solution
            print(f"Computed Output:\n{result}")
            # Indicate whether the test passed or failed
            print(f"Result: {'PASS' if str(expected) == result else 'FAIL'}")
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = old_stdout
        # Print a separator for readability between test cases
        print("-" * 40)

if __name__ == "__main__":
    run_tests()
