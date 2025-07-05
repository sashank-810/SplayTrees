# Experimental Justification: Why Splay Trees Work for Frequently Queried Elements

## Goal
To experimentally demonstrate that **splay trees** are a suitable data structure when:
- A set of `n` distinct elements is stored initially.
- A large number of `m` queries are made (with `m >> n`).
- A constant fraction `c.m` of queries are for a frequently accessed element `x`.

We aim to show that **splay trees achieve an *amortized* O(1) access time** for these frequent queries.

## Files Included
- `SplayTree.java` — Original Java implementation of a splay tree.
- `splaytree.py` — Translated Python implementation (functionally equivalent).
- `testcase1.txt` to `testcase7.txt` — Test case files containing insertions and search queries.
- `Plots for Test Cases.docx` — Plots showing access cost trends for different test cases.
- `README.md` — You’re reading it!

---

## What Are Splay Trees?

Splay trees are a type of **self-adjusting binary search tree (BST)**. After every access (search, insert, or delete), the accessed node is moved to the root through a series of tree rotations. This "splaying" ensures that **frequently accessed nodes stay near the root**, minimizing future access costs.

---

## Why Should You Care?

Suppose you use a regular binary search tree or even a hash map. In cases where:
- The access pattern is **highly skewed** toward certain elements (e.g., one value is queried 80% of the time),
- and you care about **dynamic** updates (not just constant-time lookups),

then **splay trees adapt beautifully**:  
➡️ **The more frequently you access a node, the cheaper it becomes to access it again!**

---

## Our Experimental Setup

1. **Insert Phase**: Read `n` numbers from each test case file and insert into the splay tree.
2. **Query Phase**: Run `m` search queries as specified in the file.
   - Many queries repeatedly ask for a small set of values (to simulate real-world skewed access).
3. **Metrics Collected**:
   - Total cost (measured via number of rotations or steps).
   - Cost per query.
   - Plots showing trend of access cost over time.

---

## Observations

📌 In test cases with frequent repeated queries for a few elements, we observe:
- **Significant drop in access costs** for those frequently accessed elements.
- **Amortized O(1) behavior** empirically validated by a flat or decreasing cost curve.

📈 See `Plots for Test Cases.docx` for visuals.

---

## How to Run the Python Version

### Requirements:
- Python 3.x
- matplotlib (optional, for plotting)

### Example Usage:
```bash
python splaytree.py testcase1.txt
```
## Contributors :
[@sashank810](
