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
    margin: 1em 0;
    padding: 5px 20px;
    font-style: italic;
    color: inherit;
    opacity: 0.85;
  }
  blockquote::before {
    content: none !important;
  }
  table {
    font-size: 20px;
  }
  section:has(div.ccq-columns),
  section:has(div.discussion-columns),
  section:has(div.fill-blank-columns) {
    display: flex;
    flex-direction: column;
  }
  div.ccq-columns {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-top: auto;
    margin-bottom: auto;
  }
  div.ccq-text {
    flex: 70%;
  }
  div.ccq-logo {
    flex: 30%;
    text-align: center;
  }
  div.ccq-logo img {
    width: 100%;
    max-width: 180px;
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
  div.split64, div.split46, div.split55 {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  div.split64 > div.left {
    flex: 60%;
  }
  div.split64 > div.right {
    flex: 40%;
    text-align: center;
  }
  div.split64 > div.right img {
    width: 100%;
    max-width: 320px;
  }
  div.split46 > div.left {
    flex: 40%;
  }
  div.split46 > div.right {
    flex: 60%;
    text-align: center;
  }
  div.split46 > div.right img {
    width: 100%;
    max-width: 480px;
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
header: 'Software Engineering | Chapter 6: Architectural Design'
footer: 'Prof. Nien-Lin Hsueh'
---

# Software Engineering

### Lecture 6: Architectural Design

**Prof. Nien-Lin Hsueh**
Department of Information Engineering and Computer Science
Feng Chia University

---

## Focus Questions

* What is **Architectural Design** and why is software architecture the critical link between requirements and design?
* How does **Architecture in the Small** differ from **Architecture in the Large**?
* What are Kruchten's **4+1 Architectural Views**?
* How do classic **Architectural Patterns** (MVC, Layered, Repository, Client-Server, Pipe & Filter, Microservices) structure software systems?
* How does architectural design impact system non-functional characteristics (Performance, Security, Safety, Availability, Maintainability)?
* How can **AI** assist software architects in Architectural Design, Pattern Selection, and Trade-off Analysis?

---

## What is Architectural Design?

<div class="split55">
  <div class="left">

  * **System Structure:**
    * Architectural design is concerned with understanding how a software system should be organized and designing its overall structure.
  * **Critical Link:**
    * Connects **requirements engineering** to **detailed software design** by identifying principal structural components and their relationships.
  * **Architectural Model:**
    * Outlines communicating components and system boundary interfaces.

  </div>
  <div class="right">
    <img src="images/ch06/robot_packing.png" alt="Robot Packing System Architecture" />
  </div>
</div>

---

## Architectural Abstraction Levels

* **Architecture in the Small:**
  * Concerned with individual programs or applications.
  * Focuses on how a single program is decomposed into sub-components, classes, and packages.
* **Architecture in the Large:**
  * Concerned with complex enterprise systems composed of interacting multi-system networks.
  * Systems are distributed across multiple servers, hardware cores, and cloud infrastructure managed by different teams.

---

## Advantages of Explicit Architecture

1. **Stakeholder Communication:**
   * High-level architectural diagrams act as a common focus of discussion between technical teams, business managers, and clients.
2. **System Analysis:**
   * Enables early verification of whether the system can satisfy key **non-functional requirements** (e.g., performance, security).
3. **Large-Scale Reuse:**
   * Core architectural styles can be reused across product lines in the same domain.

---

## Architecture & System Characteristics

* **Performance:** Localize critical operations in large-grain components; minimize inter-component communication.
* **Security:** Use a **layered architecture** with critical data assets enclosed in inner layers.
* **Safety:** Isolate safety-critical features into dedicated, isolated sub-systems.
* **Availability:** Include redundant components and automated failover mechanisms.
* **Maintainability:** Use fine-grained, loosely coupled, replaceable components.

---

## Architectural Views (Kruchten's 4+1 Model)

<div class="split55">
  <div class="left">

  * **Logical View:** Shows key domain abstractions as object classes.
  * **Process View:** Shows runtime interacting processes and threads.
  * **Development View:** Shows code structure, packages, and sub-systems.
  * **Physical View:** Shows hardware deployment and network distribution.
  * **+1 Use Cases / Scenarios:** Connects all 4 views together.

  </div>
  <div class="right">
    <img src="images/ch06/4plus1_views.png" alt="4+1 Architectural Views" />
  </div>
</div>

---

## Concept Check Question 1

<div class="ccq-columns">
  <div class="ccq-text">

Which architectural view in Kruchten's 4+1 View Model illustrates how software components are deployed across physical hardware and network servers at runtime?

* **A.** Logical View
* **B.** Process View
* **C.** Development View
* **D.** Physical View

  </div>
  <div class="ccq-logo">
    <img src="images/ch06/question_icon.svg" alt="Question" />
  </div>
</div>

---

## Concept Check Question 1: Answer

<div class="ccq-columns">
  <div class="ccq-text">

Which architectural view in Kruchten's 4+1 View Model illustrates how software components are deployed across physical hardware and network servers at runtime?

* **Correct Answer: D**
* **Explanation:** The Physical View (Deployment View) maps software components to physical hardware processors and network topology.

  </div>
  <div class="ccq-logo">
    <img src="images/ch06/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

## What is an Architectural Pattern?

* **Reusable Architectural Knowledge:**
  * A stylized, tested description of good design practice applicable to common architectural scenarios.
* **Pattern Structure:**
  * Defines the pattern name, description, example usage, when to use, advantages, and disadvantages.
* **Common Patterns:**
  * **MVC**, **Layered Architecture**, **Repository Architecture**, **Client-Server**, **Pipe & Filter**, **Microservices**.

---

## Model-View-Controller (MVC) Pattern

<div class="split55">
  <div class="left">

  * **Model:** Manages system data and business logic.
  * **View:** Manages presentation and UI layout to the user.
  * **Controller:** Handles user input events and updates View/Model accordingly.
  * **Advantage:** Separates data management from presentation, enabling multiple views of the same data.

  </div>
  <div class="right">
    <img src="images/ch06/mvc_structure.png" alt="MVC Architecture" />
  </div>
</div>

---

## Layered Architecture Pattern

<div class="split55">
  <div class="left">

  * **Layered Abstraction:**
    * Organizes system into stacked layers. Each layer provides services to the layer directly above it.
  * **Core Layers:**
    * User Interface $\rightarrow$ User Interaction Management $\rightarrow$ Core Business Logic $\rightarrow$ System Database / OS.
  * **Advantage:** Allows complete layer replacement if interfaces remain stable.

  </div>
  <div class="right">
    <img src="images/ch06/generic_layered.png" alt="Generic Layered Architecture" />
  </div>
</div>

---

## Repository Architecture Pattern

<div class="split55">
  <div class="left">

  * **Centralized Data Sharing:**
    * Sub-systems exchange large volumes of data through a shared central database or repository.
  * **Loose Component Coupling:**
    * Sub-systems operate independently; interactions occur via repository state changes.
  * **Examples:** IDEs (Eclipse, VS Code), CAD systems, Medical Record databases.

  </div>
  <div class="right">
    <img src="images/ch06/repository_arch.png" alt="Repository Architecture" />
  </div>
</div>

---

## Client-Server Architecture Pattern

<div class="split55">
  <div class="left">

  * **Distributed Services:**
    * Functionality is split into servers offering specialized services (database, printing, web) and clients making requests over a network.
  * **Advantages:**
    * Servers can be distributed across different machines; scalable network infrastructure.
  * **Disadvantages:**
    * Single point of failure per server; network latency dependencies.

  </div>
  <div class="right">
    <img src="images/ch06/client_server_arch.png" alt="Client Server Architecture" />
  </div>
</div>

---

## Pipe and Filter Architecture Pattern

<div class="split55">
  <div class="left">

  * **Sequential Data Transformation:**
    * Processing is structured as a series of discrete transformation steps (**filters**) connected by data streams (**pipes**).
  * **Unix Shell Model:**
    * Output of one filter becomes the input stream of the next filter (e.g., `cat | grep | sort`).
  * **Best Used For:** Batch data processing, invoice processing, compilers.

  </div>
  <div class="right">
    <img src="images/ch06/pipe_filter_arch.png" alt="Pipe and Filter Architecture" />
  </div>
</div>

---

## Microservices Architecture (MSA) vs. Monolith

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch06/monolith_vs_microservices.svg" style="max-height: 480px;" alt="MSA vs Monolith" />
</div>

---

## Microservices Architecture Characteristics

* **Decoupled Business Services:**
  * Application built as a suite of small, independent services (e.g., *User Service*, *Order Service*, *Payment Service*).
* **Independent Deployment & Databases:**
  * Each service manages its own database and can be updated, deployed, and scaled independently.
* **Lightweight Communication:**
  * Services communicate asynchronously or via lightweight REST APIs (HTTP / Kafka).
* **Resilience:**
  * Failure of one service does not crash the entire application.

---

## AI in Architectural Design: Overview

* **The Architect Copilot Paradigm:**
  * LLMs assist software architects in structuring complex systems, selecting architectural patterns, and evaluating trade-offs.
  * Translates high-level non-functional requirements into structural blueprints.

<div style="text-align: center; margin-top: 10px;">
  <img src="images/ch06/ai_in_architecture.svg" style="max-height: 250px;" alt="AI in Architectural Design" />
</div>

* **Key Benefit:** Accelerates architecture trade-off evaluation and interface contract drafting.

---

## 4 Core AI Applications in Architectural Design

1. **Architectural Pattern Recommendation:**
   * Analyzes non-functional requirements to recommend suitable architectural styles (Microservices, Event-Driven, Layered).
2. **ATAM & Trade-off Analysis Assistance:**
   * Evaluates conflicting quality attributes (e.g., Security vs. Latency, CAP Theorem Consistency vs. Availability).
3. **API & Interface Contract Generation:**
   * Generates OpenAPI (Swagger) specs, gRPC `.proto` schemas, and event payloads to decouple sub-systems.
4. **Threat Modeling & Security Boundary Analysis:**
   * Scans system architecture diagrams for single points of failure (SPOF) and STRIDE security threats.

---

## Human-in-the-Loop: Architectural Risks & Best Practices

* **Risks of Unchecked AI in Architecture:**
  * **Architectural Blind Spots:** AI lacks context regarding team tech stack familiarity, cloud vendor costs, and organizational culture.
  * **Premature Microservices:** AI recommending complex distributed architectures for simple CRUD applications.
* **The Golden Rule:**
  > **AI Proposes Trade-offs; Lead Architects Make Decisions!**
  > Human Architects must own final architectural decisions and long-term system maintainability.

---

## Concept Check Question 2

<div class="ccq-columns">
  <div class="ccq-text">

Which architectural pattern separates user presentation/UI from core data management and user input event handling?

* **A.** Pipe and Filter Pattern
* **B.** Model-View-Controller (MVC) Pattern
* **C.** Repository Pattern
* **D.** Client-Server Pattern

  </div>
  <div class="ccq-logo">
    <img src="images/ch06/question_icon.svg" alt="Question" />
  </div>
</div>

---

## Concept Check Question 2: Answer

<div class="ccq-columns">
  <div class="ccq-text">

Which architectural pattern separates user presentation/UI from core data management and user input event handling?

* **Correct Answer: B**
* **Explanation:** The MVC pattern decouples system data (Model), user UI (View), and input handling (Controller).

  </div>
  <div class="ccq-logo">
    <img src="images/ch06/answer_icon.svg" alt="Answer" />
  </div>
</div>

---

## Recap: Fill-in-the-blank Quiz

<div class="fill-blank-columns">
  <div class="fill-blank-text">

Test your understanding of the core concepts in this chapter:

1. **`___`** architecture structures a system into stacked abstract machines where each layer provides services to the layer above.
2. In the **`___`** pattern, all sub-systems share and exchange data through a central database.
3. Kruchten's **`___`** View Model presents Logical, Process, Development, and Physical perspectives joined by Scenarios.
4. **`___`** architecture decomposes a monolithic application into small, independently deployable services with decentralized data.

  </div>
  <div class="fill-blank-logo">
    <img src="images/ch06/fill_blank_icon.svg" alt="Quiz" />
  </div>
</div>

---

## Recap: Answers & Summary

<div class="fill-blank-columns">
  <div class="fill-blank-text">

Here are the completed concepts:

1. **Layered** architecture structures a system into stacked abstract machines where each layer provides services to the layer above.
2. In the **Repository** pattern, all sub-systems share and exchange data through a central database.
3. Kruchten's **4+1** View Model presents Logical, Process, Development, and Physical perspectives joined by Scenarios.
4. **Microservices** architecture decomposes a monolithic application into small, independently deployable services with decentralized data.

  </div>
  <div class="fill-blank-logo">
    <img src="images/ch06/fill_blank_answer_icon.svg" alt="Quiz Answers" />
  </div>
</div>

---

## References

* **Sommerville Software Engineering Book (Chapter 6)**
  * [Kruchten 4+1 View Model Paper](https://www.cs.ubc.ca/~greg/508/readings/kruchten.pdf)
  * [Martin Fowler Microservices Architecture Guide](https://martinfowler.com/articles/microservices.html)
