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
header: 'Software Engineering | Chapter 7c: White-Box Testing'
footer: 'Prof. Nien-Lin Hsueh'
---

# Software Engineering

### Lecture 7c: White-Box Structural Testing

**Prof. Nien-Lin Hsueh**
Department of Information Engineering and Computer Science
Feng Chia University

---

## Focus Questions

* What is **White-Box (Structural / Glass-Box) Testing**?
* What is the **Code Coverage Subsumption Hierarchy** (Statement, Branch, Condition, MC/DC, Path)?
* Why does 100% Condition Coverage (CC100) **NOT** guarantee Branch Coverage (BC100)?
* How does **Modified Condition/Decision Coverage (MC/DC)** serve safety-critical software (DO-178B/C)?
* How does **Basis Path Testing** solve the Loop Path Explosion problem?
* Why is the **100% Code Coverage** goal an anti-pattern?

---

## White-Box Structural Testing: Fundamentals

* **White-Box Testing (Structural / Glass-Box Testing):**
  * Evaluates the internal code structure, control flow paths, and implementation logic.
  * **Objective:** Measures how thoroughly the source code is exercised by test cases.
* **Key Coverage Criteria:**
  * **Statement Coverage (SC)** &rarr; **Branch Coverage (BC)** &rarr; **Condition Coverage (CC)** &rarr; **MC/DC** &rarr; **Path Coverage (PC)**.

---
<!-- _class: full-image-slide -->

<div class="centered-image">
  <img src="images/ch07/coverage_subsumption.svg" alt="Code Coverage Subsumption Hierarchy" />
</div>

---

## Statement Coverage vs. Branch Coverage

* **Statement Coverage (SC / SC100):**
  * *Requirement:* Every executable code statement must be executed at least once.
  * *Limitation:* The **weakest criterion**; SC100 can pass even if missing `else` branches or logic operators contain defects.
* **Branch / Decision Coverage (BC / BC100):**
  * *Requirement:* Every decision point (`IF`, `ELSE IF`, `WHILE`) must evaluate to **True** at least once and **False** at least once.
  * *Subsumption:* Achieving BC100 **guarantees 100% Statement Coverage (SC100)**.

---

## Condition Coverage & The Short-Circuit Paradox

* **Condition Coverage (CC / CC100):**
  * *Requirement:* Every individual atomic boolean condition inside a decision must evaluate to True and False at least once.
* **The CC100 vs. BC100 Paradox:**
  * **CC100 does NOT guarantee BC100!**
  * *Example Decision:* `if (p && q)`
    * Test t<sub>1</sub> = (True, False) &rarr; False
    * Test t<sub>2</sub> = (False, True) &rarr; False
    * Both p and q evaluated to True & False (CC100 achieved), BUT the overall decision `p && q` is ALWAYS False (0% Branch True Coverage!).
* **Short-Circuit Evaluation (`&&`, `||`):**
  * Languages skip evaluating remaining terms if early terms determine the outcome, requiring explicit test cases for unevaluated terms.

---

## Safety-Critical Standard: MC/DC Coverage

* **Modified Condition / Decision Coverage (MC/DC):**
  * Required by **aviation & safety-critical software standards (DO-178B/C)** for flight control, medical devices, and automotive systems.
* **MC/DC Core Requirement:**
  1. Every decision has evaluated to True and False at least once (BC100).
  2. Every condition has evaluated to True and False at least once (CC100).
  3. **Condition Independence:** Toggling a single condition C<sub>i</sub> from T &rarr; F (holding all other conditions constant) **must independently toggle the final decision outcome**.
* **Efficiency:** Requires only **N + 1 test cases** for N conditions (vs. 2<sup>N</sup> for full Multiple Condition Combination).

---

## Path Coverage & The Loop Explosion Problem

* **Path Coverage (PC):**
  * Tests every independent execution path from program entry to exit.
  * Represents the **most rigorous structural testing criterion**.
* **The Loop Path Explosion Problem:**
  * If a program contains a loop executing 20 times with 4 internal logic paths:
    Total Paths = 4<sup>20</sup> = 2<sup>40</sup> &approx; 1.1 &times; 10<sup>12</sup> paths!
  * Full path coverage is computationally impossible for non-trivial programs.
* **Basis Path Testing (McCabe's Cyclomatic Complexity V(G)):**
  * Derives a linearly independent set of basis paths to guarantee SC100 and BC100 with V(G) test cases.

---

## The 100% Code Coverage Myth (百分百涵蓋度的迷思)

* **Why 100% Coverage is an Anti-Pattern:**
  1. **Diminishing ROI:** Coverage from 0% to 80% yields high quality gains. Pushing from 95% to 100% requires exponential effort for minimal defect reduction.
  2. **Execution &ne; Correctness:** 100% coverage only proves code was *executed*, not that output assertions are correct, logic is sound (`a - b` vs `a + b`), or missing requirements exist.
  3. **Untestable Defensive Code:** Mocking rare OS interrupts or defensive `switch` defaults adds maintenance overhead.
* **Pragmatic Best Practice:** Target **80% -- 95% coverage** focused on critical core business logic.

---

## Concept Check Question 1

<div class="ccq-columns">
  <div class="ccq-text">

Which statement accurately describes the relationship between Statement Coverage (SC100) and Branch Coverage (BC100)?

* **A.** SC100 guarantees BC100, but BC100 does not guarantee SC100.
* **B.** BC100 guarantees SC100, but SC100 does not guarantee BC100.
* **C.** Neither metric guarantees the other under any circumstances.
* **D.** SC100 and BC100 are mathematically identical metrics.

  </div>
  <div class="ccq-logo">
    <img src="images/ch07c/question_icon.svg" alt="Question" />
  </div>
</div>

---

## Concept Check Question 1: Answer

<div class="ccq-columns">
  <div class="ccq-text">

Which statement accurately describes the relationship between Statement Coverage (SC100) and Branch Coverage (BC100)?

* **Correct Answer: B**
* **Explanation:** Executing every branch (BC100) forces every statement within those branches to be executed (SC100), but statement coverage can bypass unexecuted `else` branches.

  </div>
  <div class="ccq-logo">
    <img src="images/ch07c/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

## Recap: Fill-in-the-blank Quiz

<div class="fill-blank-columns">
  <div class="fill-blank-text">

Test your understanding of the core concepts in this chapter:

1. **`___`** coverage requires every decision point to evaluate to True and False at least once.
2. Under short-circuit evaluation, 100% **`___`** coverage does NOT guarantee branch coverage.
3. The safety-critical standard **`___`** requires each condition to independently affect the decision outcome using N+1 test cases.
4. McCabe's **`___`** Complexity V(G) defines the minimum number of basis paths needed for full structural coverage.

  </div>
  <div class="fill-blank-logo">
    <img src="images/ch07c/fill_blank_icon.svg" alt="Quiz" />
  </div>
</div>

---

## Recap: Answers & Summary

<div class="fill-blank-columns">
  <div class="fill-blank-text">

Here are the completed concepts:

1. **Branch** coverage requires every decision point to evaluate to True and False at least once.
2. Under short-circuit evaluation, 100% **condition** coverage does NOT guarantee branch coverage.
3. The safety-critical standard **MC/DC** requires each condition to independently affect the decision outcome using N+1 test cases.
4. McCabe's **Cyclomatic** Complexity V(G) defines the minimum number of basis paths needed for full structural coverage.

  </div>
  <div class="fill-blank-logo">
    <img src="images/ch07c/fill_blank_answer_icon.svg" alt="Quiz Answers" />
  </div>
</div>

---

## References

* **Prof. Nien-Lin Hsueh Software Testing Course (Ch06 White-Box Testing)**
  * [FAA / RTCA DO-178C Software Considerations in Airborne Systems](https://www.rtca.org/)
  * [McCabe Cyclomatic Complexity Metric Paper (IEEE Trans. Softw. Eng. 1976)](https://ieeexplore.ieee.org/)
