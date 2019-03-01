"""
Interview Questions for Algorithms Fourth Edition on Coursera
Week 1 Union Find
1. Question 1 Social network connectivity. 
Given a social network containing nn members and a log file containing mm timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be m \log nmlogn or better and use extra space proportional to nn.

Use weighted quick union with path compression
"""

class UnionFind:
  def __init__(self, n):
    self.root = [i for i in range(n)]
    self.size = [0 for _ in range(n)]

  def findRoot(self, i):
    while i != self.root[i]:
      self.root[i] = self.root[self.root[i]]
      i = self.root[i]
    return i

  def union(self, p, q):
    root_p = self.findRoot(p)
    root_q = self.findRoot(q)
    if self.size[root_p] < self.size[root_q]:
      self.root[root_p] = root_q
      self.size[root_q] += self.size[root_p]

  def connected(self, p, q):
    return self.root[p] == self.root[q]

uf = UnionFind(n)
for p, q in logfile:
  uf.union(p, q)
  root_p = uf.findRoot(p)
  root_q = uf.findRoot(q)
  if uf.size[root_p] == n - 1 or uf.size[root_q] == n - 1:
    print("All members are connected!")
    break
