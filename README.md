# Software Engineering Course Materials

Welcome to the **Software Engineering** course repository maintained by **Prof. Nien-Lin Hsueh** (Department of Information Engineering and Computer Science, Feng Chia University).

This repository contains comprehensive lecture slide decks, interactive concept checks, case studies, and modern software engineering practices—bridging classic software engineering fundamentals (based on Ian Sommerville's *Software Engineering*) with state-of-the-art topics like **Agile/Scrum, SOLID Design Principles, Systematic Testing Methods**, and **AI-Driven Software Development**.

---

## 📚 Course Lecture Slides & Notes Overview

All lecture slides are formatted in **Marp widescreen (16:9)** for modern classroom presentation. You can view the compiled **PDF slides** in [`Slide/`](Slide/) or explore the **Marp Markdown sources** in [`Slide/source/`](Slide/source/). Supplementary lecture notes are organized in [`Lecture/`](Lecture/), lecture video recordings and subtitles are stored in [`Video/`](Video/), and shared image assets reside in [`img/`](img/).

*Naming convention: `e` denotes English, `t` denotes Taiwanese/Traditional Chinese (e.g., `ch01t_intro.md`, `slide01e_intro.md`, `slide01e_intro.pdf`, `slide01e_intro.mp4`).*

| Lecture Module | Topic & Key Concepts | Lecture Notes | PDF Slide Deck | Marp Markdown Source | Video & Subtitles |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Lecture 1** | **Introduction to Software Engineering**<br/>Software crisis, engineering discipline, ISO 9126 quality attributes, software types, and professional ethics. | [📖 Notes](Lecture/ch01t_intro.md) | [📄 PDF](Slide/slide01e_intro.pdf) | [📝 Markdown](Slide/source/slide01e_intro.md) | [🎬 MP4](Video/slide01e_intro.mp4) / [💬 SRT](Video/slide01e_intro.srt) |
| **Lecture 2** | **Software Processes & AI-Driven Development**<br/>Waterfall, Incremental, Iterative, CMMI, and modern AI-driven processes (*Vibe Coding, Spec-Driven AI, Agentic Workflows, empirical research evidence*). | [📖 Notes](Lecture/ch02t_process.md) | [📄 PDF](Slide/slide02e_process.pdf) | [📝 Markdown](Slide/source/slide02e_process.md) |
| **Lecture 3** | **Agile Software Development**<br/>Agile Manifesto, Extreme Programming (XP), Scrum framework, User Stories, and Test-Driven Development (TDD). | [📖 Notes](Lecture/ch03t_agile.md) | [📄 PDF](Slide/slide03e_agile.pdf) | [📝 Markdown](Slide/source/slide03e_agile.md) |
| **Lecture 4** | **Requirements Engineering**<br/>Functional vs. Non-Functional Requirements, Elicitation, Specification, Use Case Modeling, and AI-assisted Requirements Engineering. | [📖 Notes](Lecture/ch04t_reqt.md) | [📄 PDF](Slide/slide04e_reqt.pdf) | [📝 Markdown](Slide/source/slide04e_reqt.md) |
| **Lecture 5** | **System Modeling**<br/>UML 4 perspectives (Context, Interaction, Structural, Behavioral), Sequence & Class Diagrams, and AI in System Modeling. | [📖 Notes](Lecture/ch05t_model.md) | [📄 PDF](Slide/slide05e_model.pdf) | [📝 Markdown](Slide/source/slide05e_model.md) |
| **Lecture 5a** | **Use Case Diagrams in Detail**<br/>Actors, boundary, include/extend relationships, and modeling guidelines. | — | [📄 PDF](Slide/slide05ae_usecase.pdf) | [📝 Markdown](Slide/source/slide05ae_usecase.md) |
| **Lecture 5b** | **Sequence Diagrams in Detail**<br/>Lifelines, synchronous/asynchronous messages, combined fragments (alt, opt, loop), and domain examples. | — | [📄 PDF](Slide/slide05be_sequence.pdf) | [📝 Markdown](Slide/source/slide05be_sequence.md) |
| **Lecture 5c** | **Class Diagrams in Detail**<br/>Classes, attributes, operations, associations, multiplicity, aggregation/composition, and generalization. | — | [📄 PDF](Slide/slide05ce_class.pdf) | [📝 Markdown](Slide/source/slide05ce_class.md) |
| **Lecture 6a** | **Architectural Design**<br/>Kruchten's 4+1 view model, 6 core architectural patterns (MVC, Layered, Repository, Client-Server, Pipe-Filter, Microservices), and AI in Architecture. | [📖 Notes](Lecture/ch06t_arch.md) | [📄 PDF](Slide/slide06ae_arch.pdf) | [📝 Markdown](Slide/source/slide06ae_arch.md) |
| **Lecture 6b** | **Software Design & OO Principles**<br/>4 Design activities, Abstraction, Encapsulation, High Cohesion vs. Low Coupling, SOLID principles with Bad vs. Good code comparisons, and AI Refactoring. | — | [📄 PDF](Slide/slide06be_design.pdf) | [📝 Markdown](Slide/source/slide06be_design.md) |
| **Lecture 7a** | **Fundamental Testing Concepts & Methods**<br/>V&V, Dijkstra's Axiom, 7 ISTQB testing principles, Regression, Fuzzing, Smoke, Sanity, Mutation, Testing Pyramid, and Testing Stages. | [📖 Notes](Lecture/ch07t_testing.md) | [📄 PDF](Slide/slide07ae_testing.pdf) | [📝 Markdown](Slide/source/slide07ae_testing.md) |
| **Lecture 7b** | **Black-Box Testing Techniques**<br/>5 Black-Box techniques, Boundary Value Analysis ($4n+1, 6n+1, 5^n, 7^n$), Equivalence Partitioning (Weak/Strong), Triangle, FCU Pool Fee, Binary Search, `nextDate()`, All-Pairs, and Decision Tables. | — | [📄 PDF](Slide/slide07be_blackbox.pdf) | [📝 Markdown](Slide/source/slide07be_blackbox.md) |
| **Lecture 7c** | **White-Box Structural Testing**<br/>Coverage Subsumption Hierarchy (Statement, Branch, Condition, MC/DC, Path), short-circuit paradox, DO-178B/C safety standards, Basis Path Testing, and the 100% Code Coverage Myth. | — | [📄 PDF](Slide/slide07ce_whitebox.pdf) | [📝 Markdown](Slide/source/slide07ce_whitebox.md) |

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
