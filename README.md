# Software Engineering Course Materials

Welcome to the **Software Engineering** course repository maintained by **Prof. Nien-Lin Hsueh** (Department of Information Engineering and Computer Science, Feng Chia University).

This repository contains comprehensive lecture slide decks, interactive concept checks, case studies, and modern software engineering practices—bridging classic software engineering fundamentals (based on Ian Sommerville's *Software Engineering*) with state-of-the-art topics like **Agile/Scrum, SOLID Design Principles, Systematic Testing Methods**, and **AI-Driven Software Development**.

---

## 📚 Course Lecture Slides & Notes Overview

All lecture slides and notes are organized cleanly into source files and compiled PDF documents. You can view the compiled **PDF slides** in [`Slide/pdf/`](Slide/pdf/), **PDF lecture notes** in [`Lecture/pdf/`](Lecture/pdf/), **Marp slide sources** in [`Slide/source/`](Slide/source/), and **Lecture note sources** in [`Lecture/source/`](Lecture/source/). Video recordings are stored in [`Video/`](Video/), and shared image assets reside in [`img/`](img/).

*Naming convention: `e` denotes English, `t` denotes Taiwanese/Traditional Chinese (e.g., `ch01e_intro.md`, `slide01e_intro.md`, `slide01e_intro.pdf`, `slide01e_intro.mp4`).*

| Lecture Module | Topic & Key Concepts | Lecture Notes (Source / PDF) | Slide Deck (Source / PDF) | Video & Subtitles |
| :--- | :--- | :---: | :---: | :---: |
| **Lecture 1** | **Introduction to Software Engineering**<br/>Software crisis, engineering discipline, ISO 9126 quality attributes, software types, and professional ethics. | [📝 Notes](Lecture/source/ch01e_intro.md) / [📄 PDF](Lecture/pdf/ch01e_intro.pdf) | [📝 Slide](Slide/source/slide01e_intro.md) / [📄 PDF](Slide/pdf/slide01e_intro.pdf) | [🎬 MP4](Video/slide01e_intro.mp4) / [💬 SRT](Video/slide01e_intro.srt) |
| **Lecture 2** | **Software Processes & AI-Driven Development**<br/>Waterfall, Incremental, Iterative, CMMI, and modern AI-driven processes (*Vibe Coding, Spec-Driven AI, Agentic Workflows, empirical research evidence*). | [📝 Notes](Lecture/source/ch02e_process.md) / [📄 PDF](Lecture/pdf/ch02e_process.pdf) | [📝 Slide](Slide/source/slide02e_process.md) / [📄 PDF](Slide/pdf/slide02e_process.pdf) | — |
| **Lecture 3** | **Agile Software Development**<br/>Agile Manifesto, Extreme Programming (XP), Scrum framework, User Stories, and Test-Driven Development (TDD). | [📝 Notes](Lecture/source/ch03t_agile.md) | [📝 Slide](Slide/source/slide03e_agile.md) / [📄 PDF](Slide/pdf/slide03e_agile.pdf) | — |
| **Lecture 4** | **Requirements Engineering**<br/>Functional vs. Non-Functional Requirements, Elicitation, Specification, Use Case Modeling, and AI-assisted Requirements Engineering. | [📝 Notes](Lecture/source/ch04t_reqt.md) | [📝 Slide](Slide/source/slide04e_reqt.md) / [📄 PDF](Slide/pdf/slide04e_reqt.pdf) | — |
| **Lecture 5** | **System Modeling**<br/>UML 4 perspectives (Context, Interaction, Structural, Behavioral), Sequence & Class Diagrams, and AI in System Modeling. | [📝 Notes](Lecture/source/ch05t_model.md) | [📝 Slide](Slide/source/slide05e_model.md) / [📄 PDF](Slide/pdf/slide05e_model.pdf) | — |
| **Lecture 5a** | **Use Case Diagrams in Detail**<br/>Actors, boundary, include/extend relationships, and modeling guidelines. | — | [📝 Slide](Slide/source/slide05ae_usecase.md) / [📄 PDF](Slide/pdf/slide05ae_usecase.pdf) | — |
| **Lecture 5b** | **Sequence Diagrams in Detail**<br/>Lifelines, synchronous/asynchronous messages, combined fragments (alt, opt, loop), and domain examples. | — | [📝 Slide](Slide/source/slide05be_sequence.md) / [📄 PDF](Slide/pdf/slide05be_sequence.pdf) | — |
| **Lecture 5c** | **Class Diagrams in Detail**<br/>Classes, attributes, operations, associations, multiplicity, aggregation/composition, and generalization. | — | [📝 Slide](Slide/source/slide05ce_class.md) / [📄 PDF](Slide/pdf/slide05ce_class.pdf) | — |
| **Lecture 6a** | **Architectural Design**<br/>Kruchten's 4+1 view model, 6 core architectural patterns (MVC, Layered, Repository, Client-Server, Pipe-Filter, Microservices), and AI in Architecture. | [📝 Notes](Lecture/source/ch06t_arch.md) | [📝 Slide](Slide/source/slide06ae_arch.md) / [📄 PDF](Slide/pdf/slide06ae_arch.pdf) | — |
| **Lecture 6b** | **Software Design & OO Principles**<br/>4 Design activities, Abstraction, Encapsulation, High Cohesion vs. Low Coupling, SOLID principles with Bad vs. Good code comparisons, and AI Refactoring. | — | [📝 Slide](Slide/source/slide06be_design.md) / [📄 PDF](Slide/pdf/slide06be_design.pdf) | — |
| **Lecture 7a** | **Fundamental Testing Concepts & Methods**<br/>V&V, Dijkstra's Axiom, 7 ISTQB testing principles, Regression, Fuzzing, Smoke, Sanity, Mutation, Testing Pyramid, and Testing Stages. | [📝 Notes](Lecture/source/ch07t_testing.md) | [📝 Slide](Slide/source/slide07ae_testing.md) / [📄 PDF](Slide/pdf/slide07ae_testing.pdf) | — |
| **Lecture 7b** | **Black-Box Testing Techniques**<br/>5 Black-Box techniques, Boundary Value Analysis ($4n+1, 6n+1, 5^n, 7^n$), Equivalence Partitioning (Weak/Strong), Triangle, FCU Pool Fee, Binary Search, `nextDate()`, All-Pairs, and Decision Tables. | — | [📝 Slide](Slide/source/slide07be_blackbox.md) / [📄 PDF](Slide/pdf/slide07be_blackbox.pdf) | — |
| **Lecture 7c** | **White-Box Structural Testing**<br/>Coverage Subsumption Hierarchy (Statement, Branch, Condition, MC/DC, Path), short-circuit paradox, DO-178B/C safety standards, Basis Path Testing, and the 100% Code Coverage Myth. | — | [📝 Slide](Slide/source/slide07ce_whitebox.md) / [📄 PDF](Slide/pdf/slide07ce_whitebox.pdf) | — |

---

## 🎯 Pedagogical Highlights

* **Interactive Learning Design**: Every chapter includes distributed **Concept Check Questions (CCQs)**, immediate answer explanation slides, and **Recap Fill-in-the-blank Quizzes**.
* **Real-World Code Comparisons**: Lecture 6b features side-by-side **Bad Design vs. Good Design** Java code snippets for every SOLID principle (SRP, OCP, LSP, ISP, DIP).
* **Empirical & AI Integration**: Covers cutting-edge LLM-based development workflows, Text-to-UML modeling, automated SOLID refactoring, and cites empirical research papers (Peng et al. 2023, Ziegler et al. 2022, McKinsey).
* **High-Impact Visuals**: Built with clean, borderless vector SVGs and multi-tier process flowcharts tailored for high readability in 16:9 widescreen presentation.

---

## 🔗 Additional Resources

* **Textbook**: *Software Engineering* (9th/10th Edition) by Ian Sommerville.
* **Original Author Slides**: [Ian Sommerville Slides (Google Drive Folder)](https://drive.google.com/drive/folders/1aU-KsrwQsNMk3Gzlj15wihctOioIMBjN?usp=drive_link)
