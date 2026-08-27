# Software Processes

**本章重點**
> 軟體開發的模式有哪些？優缺點和適用性為何？
> 軟體開發有哪些主要的活動？各自進行的方法與流程為何？
> 如何處理變更？如何降低重工 (re-work)？
> 建立軟體雛形的意義為何？如何與軟體開發流程搭配？
> 漸進式交付是何意？優點為何？
> 企業如何提升軟體工程能力？流程改善的作法為何？現今有哪些模式？
> 軟體工程有哪些相關的度量？


[Slide- Ch2 software process](https://docs.google.com/presentation/d/1e6reT4VGHE7UspwQ4amJlr6TDspo2FQm/edit?usp=sharing&ouid=109022309423128079509&rtpof=true&sd=true)

---

<a href="https://g.co/gemini/share/82f63f87854f"><img src = "https://hackmd.io/_uploads/rk-B5Yrieg.png" width=200></a>


## Process model

* A structured set of activities required to develop a software system. 
* Many different software processes but all involve:
    * **Specification** – defining what the system should do;
    * **Design and implementation** – defining the organization of the system and implementing the system;
    * **Validation** – checking that it does what the customer wants;
    * **Evolution** – changing the system in response to changing customer needs.
* A software process model is an abstract representation of a process. It presents a description of a process from some particular perspective.

---

> 👍 軟體開發流程就是以人為基底的演算法; 一個好的流程是一個有效率的演算法，如期如質的完成軟體專案。

---

Software process models

* The **waterfall** model
    * Plan-driven model. Separate and distinct phases of specification and development.
* **Incremental** development
    * Specification, development and validation are interleaved.
* **Integration and configuration**
    * The system is assembled from existing configurable components.
* In practice, most large systems are developed using a process that incorporates elements from all of these models.

---

### Waterfall model

<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*k66hoz5Y_9DId_a3UrgIpA.jpeg" width="500">

* The main drawback of the waterfall model is the difficulty of accommodating **change** after the process is underway. In principle, a phase has to be complete before moving onto the next phase.
* Inflexible partitioning of the project into distinct stages makes it difficult to respond to changing customer requirements.
* Therefore, this model is only appropriate when the **requirements are well-understood** and changes will be fairly limited during the design process. 
* Few business systems have stable requirements.
* The waterfall model is mostly used for **large** systems engineering projects where a system is developed at several sites. In those circumstances, the plan-driven nature of the waterfall model helps coordinate the work. 

---

### Incremental development model

An incremental process focuses on delivering a product in **functional**, self-contained pieces or "**increments**." You build and deliver one functional part of the product, then the next, and so on, with each new increment adding new functionality to the existing product. The product is not considered complete until all the planned increments are delivered. A good analogy is building a house: you might build the foundation first, then the first floor with a kitchen and living room, and then the second floor with bedrooms. Each new piece is a complete, functional addition to the whole.

* **Focus**: Early deliver; incrementally complete the product.
* **Outcome**: A working product is delivered after the first increment, with each subsequent increment adding more functionality.
* **Use Case**: Best when requirements are well-defined and can be broken down into distinct, prioritized modules.

![image](https://hackmd.io/_uploads/ryrO-VSigg.png)

---

**Benefits of Incremental Approach**

* More **rapid** delivery and deployment of useful software to the customer is possible. 
    * Customers are able to use and gain **value** from the software earlier than is possible with a waterfall process. 
* It is easier to get customer **feedback** on the development work that has been done. 
    * Customers can comment on **demonstrations** of the software and see how much has been implemented. 
* The cost of accommodating changing **customer requirements** is reduced. 

---

### Iterative development model

An **iterative** process focuses on **continuous refinement**. You build a basic, working version of a product and then, in subsequent cycles or "iterations," you continuously **improve** and add detail to the existing features based on feedback. The goal of each iteration is to make the product better and more polished. Think of it like a sculptor starting with a rough block of clay and progressively refining the details until the final statue is complete.

* **Focus**: Refining and improving existing features.
* **Outcome**: A more complete and refined version of the entire product with each iteration.
* **Use Case**: Ideal when initial requirements are unclear or likely to change, as it allows for flexibility and continuous feedback.

---

**Incremental vs. Iterative:**

- **Goal**:
  - **Incremental**: Focuses on adding new features or components in small steps.
  - **Iterative**: Focuses on refining or improving existing parts in cycles.
- **Deliverables**:
  - **Incremental**: Each increment is a fully functional part of the system.
  - **Iterative**: Each iteration refines or modifies what already exists.

- **Usage**: 
  - Incremental development is useful when you want to **deliver** parts of the product progressively to the customer.
  - Iterative development is useful when you want to **refine**, experiment, and improve the product’s quality.


> 💡💡 Incremental 著重在早期交付，後續的增量可能是已經規劃好的; Iterative 著重在改善，後續的版本是基於回饋。

---

![image](https://hackmd.io/_uploads/ry6xbCIRC.png)

👉 In incremental, each increment is a fully functional part of the system. In iterative, you want to refine and improve the product repeatedly. 

❗This diagram is also not quite accurate, because in the incremental method, the first version is also available.

---

### Combined Approach (Incremental and Iterative)

In practice, both approaches are often combined in what is known as an **iterative and incremental model**. This is the foundation of many agile methodologies like **Scrum**. You build the product in small, functional increments (incremental) and then refine and improve those increments over time based on feedback (iterative). This combination allows for both early delivery of working software and the flexibility to adapt to changing needs.

> 💡💡 雖然已經有功能的增量規劃，但在每一次的改善中，也著重使用者的回饋，不斷的改善架構以及功能。

---

![](http://safetydave.net/wp-content/uploads/2014/07/Screen-Shot-2014-07-24-at-9.43.34-pm.png)

 * Incremental 雖然按計劃的完成了工具，但最後使用者不滿意
 * Iterative 每次交付都是可用產品，也會打破既有框架，目的在使用者滿意
 * ❗圖中 Incremental 第一版本是不可用的，是不太合適的隱喻。

---

![](
https://lh5.googleusercontent.com/lSJ6TAbdV3OJ4OHzwCm61jDlL-vUEsxwfoQbP1b7xloOSZYuipeVblQxS5i0ZUnqrAZl6ah6tT95Qmf9R4eJL7er6BNaGqf_CwxSEfpyNk4Kwhr4pylfPvWdxL9jMlKOS7U-mco-)

👉 不是破碎的功能分割，每一個版本應該都是可用的

---

> **💡💬** 開發以下系統，分別以 incremental 及 iterative 為例說明之，請假想情境，規劃每次 INC/ITER 的變化
> * 系所網站
> * 購物網
> * 訂餐系統
> * 旅遊規劃系統
> * 大聯盟球員分析系統


**IECS department web site**
* Introduce our the department
* Sync with FCU database to show profiles of professors
* Events
  * Course events
  * General events
  * Speech events
  * Department Spotlight
* Alumni 
* 💡💬 Compare different process for this project 

---

### Integration and configuration model

* Based on software reuse where systems are integrated from existing **components** or application systems (sometimes called COTS -Commercial-off-the-shelf) systems).
* **Reused** elements may be configured to adapt their behaviour and functionality to a user’s requirements


#### Types of reusable software
* Stand-alone application systems (sometimes called COTS) that are configured for use in a particular environment.
* Collections of objects that are developed as a package to be integrated with a component framework such as .NET or J2EE.
* Web services that are developed according to service standards and which are available for remote invocation. 


💡💬 有哪些軟體框架可以幫助我們快速開發網頁程式？

---

## Process activities

### Requirements process

<img src="https://hackmd.io/_uploads/BkoCF3K26.png" width="500">

👉 Requirement specification process

---

#### Requirement specification

> ✅ The process of establishing what services are **required** and the **constraints** on the system’s operation and development.

Requirements engineering process
* Requirements elicitation and analysis
    * What do the system **stakeholders** require or **expect** from the system?
* Requirements specification	
    * Defining the requirements **in detail**
* Requirements validation
    * Checking the **validity** of the requirements

---

💡💬 針對以下系統，討論可能的 user requirement 及其延伸的 specification.
* 系所網頁
* 購物網

---

### Design and Implementation
 
> ✅ The process of converting the system specification into an executable system.

* Software design
    * Design a **software structure** that realises the specification;
* Implementation
    * Translate this structure into an **executable** program;
* The activities of design and implementation are closely related and may be **interleaved**.


<img src="https://hackmd.io/_uploads/rJZgyht2p.png" width=500>

👉 General design process

---

#### Design
* **Architectural design**, where you identify the overall structure of the system, the principal components (subsystems or modules), their relationships and how they are distributed.
* **Database design**, where you design the system data structures and how these are to be represented in a database. 
* **Interface design**, where you define the interfaces between system components. 
* **Component selection and design**, where you search for reusable components. If unavailable, you design how it will operate. 

---

#### Implementation

* The software is implemented either by **developing** a program or programs or by **configuring** an application system.
* Design and implementation are **interleaved** activities for most types of software system.
* **Programming** is an individual activity with no standard process.
* **Debugging** is the activity of finding program faults and correcting these faults.

---

### Validation

* **Verification and validation** (V & V) is intended to show that a system **conforms** to its specification and meets the requirements of the system customer.
* Involves checking and **review** processes and system **testing**.
* System testing involves executing the system with **test cases** that are derived from the specification of the real data to be processed by the system.
* **Testing** is the most commonly used V & V activity.

---

<img src="https://hackmd.io/_uploads/SyvPy2KnT.png" width="450">

👉 Stage of testing

---

**Testing** 
* **Component testing**
    * **Individual** components are tested independently; 
    * Components may be functions or objects or coherent groupings of these entities.
* **System testing**
    * Testing of the system as a **whole**. Testing of emergent properties is particularly important.
* **Customer testing**
    * Testing with customer data to check that the system meets the **customer’s** needs.


![image](https://hackmd.io/_uploads/BkQpJhY3p.png)

👉 V process model

---

### Evolution

* Software is inherently flexible and can **change**. 
* As requirements change through changing **business** circumstances, the software that supports the business must also evolve and change.
* Although there has been a demarcation between development and evolution (maintenance) this is increasingly irrelevant as fewer and fewer systems are completely new.

---

![image](https://hackmd.io/_uploads/Bk5ge3Fn6.png)

👉 Evolution process

---

## Coping with Change

* Change is **inevitable** in all large software projects.
    * **Business** changes lead to new and changed system requirements
    * New **technologies** open up new possibilities for improving implementations
    * Changing **platforms** require application changes
* Change leads to **rework** so the costs of change include both rework (e.g. re-analysing requirements) as well as the costs of implementing new functionality

---

Reducing the costs of rework

* **Change anticipation**, where the software process includes activities that can anticipate possible changes before significant rework is required. 
    * For example, a prototype system may be developed to show some key features of the system to customers. 
* **Change tolerance**, where the process is designed so that changes can be accommodated at relatively low cost.
    * This normally involves some form of incremental development. Proposed changes may be implemented in increments that have not yet been developed. If this is impossible, then only a single increment (a small part of the system) may have be altered to incorporate the change.

> 💡💬 How to anticipate change?

---

Coping with changing requirements

* **System prototyping**, where a version of the system or part of the system is developed quickly to check the customer’s requirements and the feasibility of design decisions. This approach supports change anticipation. 
* **Incremental delivery**, where system increments are delivered to the customer for comment and experimentation. This supports both change avoidance and change tolerance. 

---

### Prototyping

* A **prototype** is an initial version of a system used to demonstrate concepts and try out design options.
* A prototype can be used in:
    * The **requirements** engineering process to help with requirements elicitation and validation;
    * In **design** processes to explore options and develop a UI design;
    * In the **testing** process to run back-to-back tests.

**Benefits of prototyping**

* Improved system usability.
* A closer match to users’ real needs.
* Improved design quality.
* Improved maintainability.
* Reduced development effort.

---

#### Throw-away prototypes
* Prototypes should be **discarded** after development as they are not a good basis for a production system:
* It may be impossible to tune the system to meet **non-functional** requirements;
* Prototypes are normally **undocumented**;
* The prototype structure is usually **degraded** through rapid change;
* The prototype probably will not meet normal organisational **quality** standards.

---

#### Incremental development and delivery

Incremental development
* Develop the system in increments and **evaluate** each increment before proceeding to the development of the next increment;
    * Normal approach used in agile methods;
    * Evaluation done by user/customer proxy.
* Incremental delivery
    * Deploy an increment for use by **end-users**;
    * More realistic evaluation about practical use of software;

![image](https://hackmd.io/_uploads/BkdiI2KhT.png)

👉 Incremental delivery

---

## Proess improvement model


![image](http://bi-insider.com/wp-content/uploads/2020/12/CMMI-Maturity-Levels.png)

The **Capability Maturity Model Integration (CMMI)** is a process-level improvement framework designed to help organizations improve their processes and performance. It provides a structured way to enhance the quality and efficiency of organizational processes in software engineering, systems engineering, and other areas. CMMI is used to guide process improvement across projects, departments, or entire organizations.

#### Key Focus of CMMI:
- Improving **processes** to achieve higher quality and performance.
- Reducing risks and costs while increasing **predictability**.
- Emphasizing process **maturity** and continuous **improvement**.

---

### CMMI Maturity Levels

CMMI defines **five maturity levels**, each representing an organization's degree of process capability and standardization. These levels are used to evaluate how well an organization’s processes are defined and optimized.

1. **Level 1: Initial (Ad hoc/Chaotic)**
   - **Characteristics**: Processes are unpredictable, poorly controlled, and reactive. Organizations at this level often rely on individual effort and heroics to get things done, with success largely depending on specific individuals rather than defined processes.
   - **Challenges**: High risk, inconsistent outcomes, and a lack of standardized practices.

2. **Level 2: Managed**
   - **Characteristics**: Basic project management processes are established to track cost, schedule, and performance. Processes are planned, documented, performed, and controlled, though they are often reactive. Success is more repeatable compared to Level 1.
   - **Key Processes**: Requirements management, project planning, monitoring, and control.
   
3. **Level 3: Defined**
   - **Characteristics**: Processes are well-characterized and understood and are described in standards, procedures, tools, and methods. Processes are proactive, tailored for the organization’s needs, and are standardized across projects.
   - **Key Features**: Organization-wide standards, greater predictability, and more consistency in process performance.

4. **Level 4: Quantitatively Managed**
   - **Characteristics**: The organization uses quantitative metrics and performance measures to manage processes. Processes are measured, controlled, and continuously improved, with performance becoming more predictable and under statistical control.
   - **Key Focus**: Quantitative goals for product quality and process performance, statistical techniques to improve processes.

5. **Level 5: Optimizing**
   - **Characteristics**: The focus is on continuous process improvement. Organizations at this level use feedback and innovation to proactively enhance processes, aiming for better performance. They can adapt quickly to change and new opportunities through a systematic approach to process improvement.
   - **Key Activities**: Continuous process improvement, root cause analysis, and preventive action.


#### tabel-cmmi-process-area

| **Maturity Level**                   | **Process Areas (PAs)**                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Level 1 - Initial**                | No specific process areas at this level. This is a chaotic, ad-hoc stage with unpredictable outcomes.                                                                                                                                                                                                                                                                                                |
| **Level 2 - Managed**                | - Requirements Management (REQM) <br> - Project Planning (PP) <br> - Project Monitoring and Control (PMC) <br> - Supplier Agreement Management (SAM) <br> - Measurement and Analysis (MA) <br> - Process and Product Quality Assurance (PPQA) <br> - Configuration Management (CM)                                                                                                                   |
| **Level 3 - Defined**                | - Requirements Development (RD) <br> - Technical Solution (TS) <br> - Product Integration (PI) <br> - Verification (VER) <br> - Validation (VAL) <br> - Organizational Process Focus (OPF) <br> - Organizational Process Definition (OPD) <br> - Organizational Training (OT) <br> - Integrated Project Management (IPM) <br> - Risk Management (RSKM) <br> - Decision Analysis and Resolution (DAR) |
| **Level 4 - Quantitatively Managed** | - Organizational Process Performance (OPP) <br> - Quantitative Project Management (QPM)                                                                                                                                                                                                                                                                                                              |
| **Level 5 - Optimizing**             | - Organizational Innovation and Deployment (OID) <br> - Causal Analysis and Resolution (CAR)                                                                                                                                                                                                                                                                                                         |

---

#### CMMI Benefits
- **Improved product quality** by focusing on process improvement.
- **Reduced project risks** through better management and predictability.
- **Enhanced customer satisfaction** with more consistent and reliable outcomes.
- **Increased efficiency and reduced rework** due to well-defined processes and continuous improvement.

CMMI is widely adopted by industries to enhance software quality, reduce defects, and foster a culture of continuous improvement.

---

### Software engineering metrics

In software engineering, **metrics** or **indicators** are essential for measuring various aspects of the development process, product quality, and team performance. These metrics help organizations improve their processes, ensure software reliability, and make data-driven decisions.

Here are some key software engineering metrics:

#### 1. **Code Quality Metrics**
   - **Cyclomatic Complexity**: Measures the complexity of a program by counting the number of linearly independent paths through the code. Higher complexity indicates more difficult-to-test and maintain code.
   - **Code Coverage**: Measures the percentage of code that is executed during testing. It helps to assess how much of the codebase is tested, aiming for higher coverage to reduce the chance of bugs.
   - **Code Churn**: Tracks the amount of code added, modified, or deleted over time. High churn rates may indicate instability or frequent changes, which could reduce code quality.

![](https://docs.devexpress.com/CodeRushForRoslyn/images/testing_coverage122460.png)

👉 Code coverage

#### 2. **Productivity Metrics**
   - **Lines of Code (LOC)**: A traditional metric that counts the number of lines written in the source code. However, it does not account for the quality or complexity of the code, so it is often used alongside other metrics.
   - **Velocity**: In agile development, velocity measures how much work a team can complete in a sprint. It is based on story points or user stories completed and is used to plan future sprints.
   - **Commit Frequency**: Tracks how often developers commit code changes. Regular commits can indicate an active development process and provide more frequent checkpoints for review.

#### 3. **Defect Metrics**
   - **Defect Density**: The number of defects found per unit of code (e.g., per thousand lines of code, or KLOC). It helps identify areas with high defect concentration that need further attention.
   - **Defect Leakage**: The number of defects that escape to later stages of development or production. It indicates the effectiveness of earlier testing phases.
   - **Mean Time to Detect (MTTD)**: Measures the average time taken to identify defects. Shorter MTTD indicates quicker detection and responsiveness.
   - **Mean Time to Repair (MTTR)**: Measures the average time it takes to fix a defect. Lower MTTR indicates efficient debugging and resolution of issues.

![](https://vitalflux.com/wp-content/uploads/2013/02/dd1.jpg)

👉 Defect density

#### 4. **Performance Metrics**
   - **Response Time**: The time it takes for the system to respond to a user request. It is critical for user experience in real-time applications.
   - **Throughput**: The number of transactions a system can process in a given time frame. This metric is crucial for high-performance systems.
   - **Latency**: Measures the delay between a request and the system’s response. Minimizing latency is vital for time-sensitive applications like video streaming or financial systems.

#### 5. **Reliability and Maintainability Metrics**
   - **Mean Time Between Failures (MTBF)**: Measures the average time between system failures. It is used to assess the reliability and robustness of the software.
   - **Mean Time to Failure (MTTF)**: The average time a system runs before it fails. A high MTTF indicates a more reliable system.
   - **Maintainability Index**: A composite metric that uses factors such as lines of code, cyclomatic complexity, and code comments to assess how easy the code is to maintain over time.
   - **Technical Debt**: Measures the effort required to fix code that was developed with quick fixes or shortcuts. High technical debt leads to higher maintenance costs and lower quality over time.

#### 6. **Customer Satisfaction Metrics**
   - **Net Promoter Score (NPS)**: A measure of customer loyalty and satisfaction, NPS gauges how likely users are to recommend the software to others. It’s a strong indicator of the perceived value of a product.
   - **Customer Support Tickets**: The number of user-reported issues can indicate how user-friendly and stable a software product is. A decreasing number of tickets can indicate better product quality or improved customer experience.

#### 7. **Process Metrics**
   - **Cycle Time**: The time required to complete a task from start to finish. Reducing cycle time is key to improving delivery speed.
   - **Sprint Burndown**: In agile, this tracks the progress of a sprint by showing how much work remains compared to what was planned. A well-managed sprint burndown chart reflects a healthy development process.


![](https://pmstudycircle.com/wp-content/uploads/2022/10/graph-showing-burndown-chart-1024x579.png.webp)

👉 Burndown chart

#### 8. **Security Metrics**
   - **Number of Vulnerabilities**: Tracks the number of security flaws or vulnerabilities detected in the code. Fewer vulnerabilities suggest a more secure application.
   - **Time to Patch**: The time taken to patch security vulnerabilities once discovered. Lower times indicate quicker responses to potential threats.

#### 9. **User Experience (UX) Metrics**
   - **User Engagement**: Measures how users interact with the software, such as the frequency of usage, session length, and feature adoption.
   - **Error Rate**: The number of errors users encounter while interacting with the system. Lower error rates reflect a smoother user experience.
   - **Task Completion Rate**: Tracks how often users successfully complete tasks within the software. A higher completion rate indicates a more intuitive and user-friendly interface.

