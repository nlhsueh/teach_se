---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f5
color: #333
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    padding: 40px;
    font-size: 24px;
  }
  h1 {
    color: #0b3c5d;
  }
  h2 {
    color: #328cc1;
  }
  footer {
    font-size: 0.5em;
    color: #777;
  }
  header {
    font-size: 0.5em;
    color: #aaa;
    text-align: right;
  }
  blockquote {
    background: transparent;
    border-left: 4px solid #328cc1;
    padding-left: 20px;
    margin: 20px 0;
    font-style: italic;
    color: #555;
  }
  div.centered-image {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80%;
  }
  div.centered-image img {
    max-width: 90%;
    max-height: 480px;
    object-fit: contain;
  }
  .full-image-slide {
    padding: 20px !important;
  }
  .full-image-slide div.centered-image {
    height: 100% !important;
  }
  .full-image-slide div.centered-image img {
    max-width: 98% !important;
    max-height: 600px !important;
  }
  div.ccq-columns {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: auto;
    margin-bottom: auto;
  }
  div.ccq-text {
    flex: 75%;
  }
  div.ccq-logo {
    flex: 25%;
    text-align: center;
  }
  div.ccq-logo img {
    width: 100%;
    max-width: 150px;
  }
  div.fill-blank-columns {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: auto;
    margin-bottom: auto;
  }
  div.fill-blank-text {
    flex: 75%;
  }
  div.fill-blank-logo {
    flex: 25%;
    text-align: center;
  }
  div.fill-blank-logo img {
    width: 100%;
    max-width: 150px;
  }
  div.split55 {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  div.split55 > div.left {
    flex: 50%;
  }
  div.split55 > div.right {
    flex: 50%;
    text-align: center;
  }
  div.split55 > div.right img {
    width: 100%;
    max-width: 400px;
  }
header: 'Software Engineering | Chapter 7b: Black-Box Testing'
footer: 'Prof. Nien-Lin Hsueh'
---

# Software Engineering

### Lecture 7b: Black-Box Testing Techniques

**Prof. Nien-Lin Hsueh**
Department of Information Engineering and Computer Science
Feng Chia University

---

## Focus Questions

* What is **Black-Box (Specification-Based) Testing**?
* What are the 4 **Boundary Value Testing Formulas** (4n+1, 6n+1, 5<sup>n</sup>, 7<sup>n</sup>) and Single Fault Assumption?
* How do **Weak Coverage (Weak EP)** and **Strong Coverage (Strong EP)** differ?
* How do we design test suites for **Triangle Classification, Exam Scores, FCU Swimming Pool Fee, Binary Search, and nextDate()**?
* How does **All-Pairs (Pairwise) Testing** solve combinatorial explosion?
* How do **Decision Table Testing** and **State Transition Testing** model system logic?

---

## Black-Box vs. White-Box Testing

* **Black-Box Testing (Functional / Specification-Based):**
  * **Definition:** A testing method where the internal code structure, implementation details, and source code are **completely hidden** from the tester.
  * **Focus:** Tests system behavior against functional specifications by sending inputs and validating expected outputs.
* **White-Box Testing (Structural / Glass-Box Testing):**
  * **Definition:** A testing technique where internal code structure and control flow are **fully visible**.

---
<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="images/ch07/black_vs_white_box.svg" alt="Black Box vs White Box" />
</div>

---

## 5 Major Black-Box Testing Methods

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/black_box_methods.svg" style="max-height: 480px;" alt="5 Black-Box Testing Techniques" />
</div>

---

## Boundary Value Testing Taxonomy

* **Single Fault Assumption (單一錯誤假設):**
  * Assumes a system failure is caused by a defect in a *single variable* rather than simultaneous defects across multiple variables.
* **Independent vs. Non-Independent (Worst-Case):**
  * **Independent:** Variables do not interact; test boundary of 1 variable holding others at `norm`.
  * **Non-Independent (Worst-Case):** Variables interact in logic statements (e.g. `if (exam <= 60 && hw <= 60)`). Requires Cartesian cross-product of boundary values.

---

## The 4 Boundary Testing Formulas

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/boundary_taxonomy.svg" style="max-height: 380px;" alt="Boundary Value Taxonomy" />
</div>

---

## Boundary Case Study: Triangle Classification

> **Requirement:** Inputs <code>a, b, c &isin; [1, 200]</code>. Output: *Equilateral*, *Isosceles*, *Scalene*, *Non-Triangle*.

* **Independent Normal Boundary (4n+1 = 13 cases):**
  * Hold b, c at <code>norm=100</code>, test a &isin; {1, 2, 199, 200}. Repeat for b and c, plus 1 `norm` case.
* **The Diversity Deficit & Solution:**
  * Independent testing (13 cases) only produces *Isosceles* and *Equilateral* triangles, missing *Scalene* triangles!
  * **Solutions:** Use dynamic random `norm` values or apply **Output-Guided Partitioning**.
* **Non-Independent Worst-Case:** 5<sup>3</sup> = 125 test cases (5 &times; 5 &times; 5).

---

## Equivalence Partitioning: Weak vs. Strong Coverage

* **Equivalence Partitioning Concept:**
  * Divides input/output space into classes where all values are processed identically.
* **Weak Coverage (Weak EP):**
  * Based on Single Fault Assumption. Every partition of every variable is tested **at least once**.
  * Total test cases = max(Partitions of v<sub>1</sub>, ..., v<sub>n</sub>).
* **Strong Coverage (Strong EP):**
  * For non-independent interacting variables. Tests the **Cartesian product** of all partitions across all variables (P<sub>1</sub> &times; P<sub>2</sub> &times; ... &times; P<sub>n</sub>).

---

## EP Case Study 1: Single-Variable Domain (Exam Scores)

> **Requirement:** An online grading system accepts exam scores between **0** and **100** inclusive.

* **Partition 1: Invalid Low (Score &lt; 0)**
  * *Representative Test Value:* **-15** &rarr; *Expected Output:* Error ("Score cannot be negative").
* **Partition 2: Valid Range (0 &le; Score &le; 100)**
  * *Representative Test Value:* **75** &rarr; *Expected Output:* Valid grade recorded.
* **Partition 3: Invalid High (Score &gt; 100)**
  * *Representative Test Value:* **135** &rarr; *Expected Output:* Error ("Score exceeds maximum 100").

---

## EP Case Study 2: Multi-Variable FCU Swimming Pool Fee

> **Requirement:** Public pool ticket price depends on **Age**, **Time Slot**, and **Membership**.

* **Input Partitions:**
  * **Age:** Child (&lt; 12), Adult (12&ndash;64), Senior (&ge; 65), Invalid (&lt; 0).
  * **Time Slot:** Off-Peak (Morning) vs. Peak (Evening).
  * **Membership:** Member (Discount) vs. Non-Member (Full Price).

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/swimming_pool_ep.svg" style="max-height: 230px;" alt="Swimming Pool EP Matrix" />
</div>

---

## EP Case Study 3: Binary Search Partition Plan

> **Spec:** `Search(Key: int, A: Array) -> (Found: bool, Index: int)`

* **Input Array Partitions:**
  * Empty array (a<sup>0</sup>: empty), Single element (a<sup>1</sup>: 1 element), Multiple elements (a<sup>*</sup>: multiple elements).
* **Output & Position Partitions:**
  * **Found (f<sup>t</sup>):** Key at first position (c<sup>1</sup>), middle position (c<sup>m</sup>), or last position (c<sup>l</sup>).
  * **Not Found (f<sup>f</sup>):** Key not present in array.
  * **Invalid Type (k<sup>!</sup>):** Error handling for corrupted input.
* **Weak Coverage Goal:** Derive 8 structured test cases (R<sub>1</sub> &ndash; R<sub>8</sub>) covering all input and output partitions.

---

## EP Case Study 3: Binary Search Test Suite

> **Concrete Test Suite (R1 &ndash; R8) covering all Equivalence Partitions:**

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/binary_search_ep_table.svg" style="max-height: 380px;" alt="Binary Search Test Cases Table" />
</div>

---

## Boundary & EP Case Study: nextDate Plan

> **Spec:** `nextDate(month: int, day: int, year: int) -> String` (Date in 1800&ndash;2048)

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/nextdate_case_study.svg" style="max-height: 250px;" alt="nextDate Case Study" />
</div>

* **Key Boundary Test Points:**
  * **Month End:** `2024-01-31` &rarr; `2024-02-01` | **Year End:** `2024-12-31` &rarr; `2025-01-01`
  * **30-Day Boundary:** `2024-04-30` &rarr; `2024-05-01` (Day `31` in April is Invalid).
  * **Leap Year Boundary:** `2024-02-28` &rarr; `2024-02-29` vs. `2023-02-28` &rarr; `2023-03-01`.

---

## Boundary & EP Case Study: nextDate Test Suite

> **Concrete Test Suite (TC1 &ndash; TC8) covering all Boundary & Equivalence Classes:**

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/nextdate_ep_table.svg" style="max-height: 380px;" alt="nextDate Test Cases Table" />
</div>

---

## All-Pairs (Pairwise) Testing

* **The Combinatorial Explosion Problem:**
  * Testing all combinations (Strong EP / Cartesian Product) across <i>k</i> variables requires <b>O(N<sup>k</sup>)</b> test cases (e.g. 3<sup>10</sup> = 59,049 tests).
* **Core Empirical Principle:**
  * *Most software bugs are triggered by interactions between at most 2 parameters (pairs)* rather than complex 5-way interactions.

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/all_pairs_testing.svg" style="max-height: 220px;" alt="All-Pairs Testing" />
</div>

* **Benefit:** Ensures **every pair of input parameters is tested together at least once**, reducing 59,049 test cases down to &approx; 15&ndash;20 test cases!

---

## Black-Box Method 3: Decision Table Testing

* **Concept:**
  * A structured tabular approach to model complex business logic containing multiple conditional rules.
  * **Structure:** Combines input conditions (True/False) with resulting system actions.

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch07/decision_table.svg" style="max-height: 280px;" alt="Decision Table Example" />
</div>

---

## Black-Box Method 4 & 5: State & Use Case Testing

* **Method 4: State Transition Testing:**
  * Tests how the system transitions between discrete finite states in response to user events.
  * Verifies both **valid transitions** (e.g. *Unauthenticated* &rarr; Login &rarr; *Authenticated*) and **invalid transitions** (e.g. attempting checkout while unauthenticated).
* **Method 5: Use Case / Scenario Testing:**
  * Test cases are derived directly from high-level **Use Cases** or user stories.
  * Verifies end-to-end user goals, basic normal flows, alternate paths, and exception flows.

---

## Concept Check Question 1

<div class="ccq-columns">
  <div class="ccq-text">

In Black-Box Test Case Design, why is Boundary Value Analysis (BVA) used alongside Equivalence Partitioning?

* **A.** Because white-box code source files are required for boundary testing.
* **B.** Because software defects occur most frequently at the edges/boundaries of input partitions.
* **C.** Because boundary values eliminate the need for unit testing.
* **D.** Because BVA only tests valid partitions and ignores invalid inputs.

  </div>
  <div class="ccq-logo">
    <img src="images/ch07b/question_icon.svg" alt="Question" />
  </div>
</div>

---

## Concept Check Question 1: Answer

<div class="ccq-columns">
  <div class="ccq-text">

In Black-Box Test Case Design, why is Boundary Value Analysis (BVA) used alongside Equivalence Partitioning?

* **Correct Answer: B**
* **Explanation:** Off-by-one errors (&lt; vs &le;) mean defects concentrate heavily at boundaries.

  </div>
  <div class="ccq-logo">
    <img src="images/ch07b/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

## Recap: Fill-in-the-blank Quiz

<div class="fill-blank-columns">
  <div class="fill-blank-text">

Test your understanding of the core concepts in this chapter:

1. **`___`** testing divides input domains into classes processed identically by the system.
2. Under Single Fault Assumption, Independent Normal Boundary testing requires **`___`** test cases for n variables.
3. For interacting non-independent variables, worst-case boundary testing requires **`___`** test cases.
4. **`___`** testing ensures every pair of input parameters is tested together at least once, avoiding combinatorial explosion.

  </div>
  <div class="fill-blank-logo">
    <img src="images/ch07b/fill_blank_icon.svg" alt="Quiz" />
  </div>
</div>

---

## Recap: Answers & Summary

<div class="fill-blank-columns">
  <div class="fill-blank-text">

Here are the completed concepts:

1. **Equivalence partitioning** testing divides input domains into classes processed identically by the system.
2. Under Single Fault Assumption, Independent Normal Boundary testing requires **4n + 1** test cases for n variables.
3. For interacting non-independent variables, worst-case boundary testing requires **5<sup>n</sup>** test cases.
4. **All-pairs (pairwise)** testing ensures every pair of input parameters is tested together at least once.

  </div>
  <div class="fill-blank-logo">
    <img src="images/ch07b/fill_blank_answer_icon.svg" alt="Quiz Answers" />
  </div>
</div>

---

## References

* **Prof. Nien-Lin Hsueh Software Testing Course (Ch05 Black-Box Testing)**
  * [IEEE 829 Standard for Software Test Documentation](https://standards.ieee.org/)
  * [Pairwise / All-Pairs Testing Tool PICT](https://github.com/microsoft/pict)
