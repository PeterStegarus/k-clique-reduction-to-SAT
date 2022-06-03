# Backtracking
Compute all combinations of N nodes taken k. If k-clique found, print True. Otherwise, if all combinations were checked and none satisfied k-clique, print False.

Time complexity: O(n^k * k^2)

# Reduction

    SAT <=p k-Clique: (phi = c1 ^ c2 ^ ... ^ cn)
    k = n
    G:
      V = {xvi for each Lvi from each ci}
      E = (xui, xvj) from E if i != j, Lui != ~Lvj


### k-Clique(k, G) <=p SAT(phi):

(Lvi = True if node v is ith node from k-clique)

n = k

For each i, some node needs to be ith node from k-clique.
For each node v = 1..N, insert clause ci (i = 1..k):

    (ci = L1i V L2i V ... V LNi). (1)

One node can only appear once in the k-clique. For each node v:

    (~Lvi V ~Lvj), i != j (2)

If 2 nodes are not connected, they can not be both in the same k-clique. If u and v not adjacent, insert clause:

    (~Lui V ~Lvj), i != j (i, j pairs of "levels" in k-clique 1 <= i < j <= k) (3)

## Time complexity

SAT input:

    phi = conjunction of all clauses from (1), (2), (3)

(1) k clauses each with N literals: N * k

(2) (N * combinations of k taken 2) clauses with 2 literals: N * k * (k - 1)

(3) (combinations of N taken 2 * combinations of k taken 2) clauses with 2 literals: N * (N - 1) * k * (k - 1)

Total: N * k * (N * k - N + 1) clauses. O(N ^ 2 * K ^ 2). Since k < N, time complexity is polynomial: O(N ^ 4).


## Proof k-Clique(k, G) = 1 <=> SAT(phi) = 1

### 1) k-Clique(k, G) = 1 => SAT(phi) = 1
>k-Clique(k, G) = 1 <=> There be k nodes different and adjacent 2 by 2 to form a k-clique, [v1, v2, ..., vk]. Let there be k literals, [Lv1,1; Lv2,2; ...; Lvk,k], which are true and satisfy the 3 types of clauses:
>
>- There are k nodes in the k-clique satisfies type (1) clauses
>- Nodes are distinct satisfies (2)
>- Nodes are adjacent 2 by 2 satisfies (3)

  Results SAT(phi) = 1

### 2) SAT(phi) = 1 => k-Clique(k, G) = 1

  >SAT(phi) = 1 <=> all ci clauses are true 
  >
  >=> some literals [Lv1,1; Lv2,2; ...; Lvk,k] are therefore true (from the clauses that impose the 3 conditions: there are k literals, imposing rules about distinct nodes, nodes that are connected 2 by 2) 
  >
  >=> nodes [v1, v2,..., vk] (where vi distincy 2 by 2, adjacent 2 by 2) form a k-clique
  >
  >=> k-Clique(k, G) = 1

Examples with pictures in reduction_examples.pdf

# Results, comparisons and favorable cases

It seems that in most categories, backtracking takes less time than the reduction. I have however made the backtracking optimization that I don't look for larger subgraphs than k. And the transformation for the reduction is definitely polynomial.

I think this is due to too small or too large k, in which case the backtracking runs in a polynomial time. For example, for an N large enough (N > 100) and a small k (e.g. k = 3), the complexity is O(N ^ 3) for bkt.

But, if I were to choose tests in which k is N/2 (e.g. N = 100, k = 50), one observes that bkt takes too long (O(N ^ N) because k depends on N).

Locally, for N=50 and k=25, bkt has been running for a few minutes and is not yet finished. Even N=50 and k=6 is too much for bkt, with all the optimizations, while the reduction solves relatively quickly. (N = 50, k = 6: bkt = 92.8s, rdc = 6.7s)

On the other hand, for k = N, bkt is instant while rdc takes too long (n = 50, k = 50: bkt = 0.06s, rdc = 384.7s).

From this I deduce that rdc is more optimal for a k in the middle region of range (1,N) (k = N / 2 being most favorable for rdc), while btk is more optimal for k at the extreme end of the range (k = 1 or k = N most favourable for bkt, but for k = N the largest difference between rdc and bkt is obtained in favour of bkt)

So, for a k close enough to N / 2, it is more optimal to solve with reduction. So k = N / 2 would make the biggest difference in favour of reduction. However, for a small number of nodes N, this cannot be observed. For this reason, I made another category of tests, category4, where there are 2 tests which are in favour of reduction. (local: bkt = 12.7s rdc = 5.1s)

In short, for large enough N and k close enough to N / 2, bkt takes much too long, while rdc is very fast. Then, as k increases and departs from N/2, bkt starts to become more efficient than rdc.
