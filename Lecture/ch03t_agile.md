# Ch03 Agile Software Development

:::success
本章重點
* 何謂敏捷開發？
* 敏捷開發的基礎原則（敏捷宣言）為何？
* 透過「使用者故事」來描述需求的意義為何？
* XP 是敏捷的實踐方法之一，他的做法為何？
* Scrum 是敏捷的專案管理方法，他的做法為何？
:::

[Slide](https://docs.google.com/presentation/d/1g2CTelhe3jQfVTD2fufTxYvWUTZo1uZW/edit?usp=sharing&ouid=109022309423128079509&rtpof=true&sd=true)

## Rapid software development
* **Rapid** development and delivery is now often the most important requirement for software systems
* Businesses operate in a fast –**changing** requirement and it is practically impossible to produce a set of stable software requirements
* Software has to evolve quickly to reflect changing business needs.
* Plan-driven development is essential for some types of system but does not meet these business needs.
* Agile development methods emerged in the late 1990s whose aim was to radically reduce the delivery time for working software systems

### Agile development
* Program specification, design and implementation are **interleaved**
* The system is developed as a series of versions or increments with **stakeholders** involved in version specification and evaluation
* Extensive tool support (e.g. automated testing tools) used to support development.
* **Minimal documentation** – focus on working code

### Agile methods

Dissatisfaction with the **overheads** involved in software design methods of the 1980s and 1990s led to the creation of agile methods. These methods:
* Focus on the **code** rather than the design
* Are based on an **iterative** approach to software development
* Are intended to deliver working software quickly and evolve this quickly to **meet changing requirements**.
* The aim of agile methods is to reduce overheads in the software process (e.g. by limiting documentation) and to be able to respond quickly to changing requirements without excessive rework.


#### Agile manifesto 

:::info
* Individuals and **interactions** over processes 
* Tools **Working** software over comprehensive documentation 
* **Customer** collaboration over contract negotiation 
* Responding to **change** over following a plan 
:::

#### The principles of agile methods 

* **Customer involvement**: Customers should be closely involved throughout the development process. Their role is provide and prioritize new system requirements and to evaluate the iterations of the system.
* **Incremental delivery**: The software is developed in increments with the customer specifying the requirements to be included in each increment.
* **People not process**: The skills of the development team should be recognized and exploited. Team members should be left to develop their own ways of working without prescriptive processes.
* **Embrace change**: Expect the system requirements to change and so design the system to accommodate these changes.
* **Maintain simplicity**: Focus on simplicity in both the software being developed and in the development process. Wherever possible, actively work to eliminate complexity from the system.
 
#### Agile method applicability
* Product development where a software company is developing a **small** or **medium**-sized product for sale. 
* Virtually all software products and apps are now developed using an agile approach
* Custom system development within an organization, where there is a clear **commitment** from the customer to become **involved** in the development process and where there are few external rules and regulations that affect the software.

:::success
:basketball: 活動

硬幣遊戲
:::

## Extreme programming
XP is a popular agile development technique

##### fig-extreme-programming
![image](https://hackmd.io/_uploads/ByZFmFtnT.png)

* A very influential agile method, developed in the late 1990s, that introduced a range of agile development techniques.
* Extreme Programming (XP) takes an ‘extreme’ approach to iterative development. 
* New versions may be built **several times per day**;
* Increments are delivered to customers every 2 weeks;
* All tests must be run for every build and the build is only accepted if tests run successfully.

#### The extreme programming release cycle 

#### Extreme programming practices

Principle or practice

| Principle                  | Description                                                                                                                                                                                                                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Incremental planning**   | Requirements are recorded on **story cards** and the stories to be included in a release are determined by the time available and their relative priority. The developers break these stories into development ‘Tasks’.                                                                             |
| **Small releases**         | The **minimal** useful set of functionality that provides business value is developed first. Releases of the system are frequent and incrementally add functionality to the first release.                                                                                                          |
| **Simple design**          | **Enough** design is carried out to meet the current requirements and no more.                                                                                                                                                                                                                      |
| **Test-first development** | An **automated** unit test framework is used to write tests for a new piece of functionality before that functionality itself is implemented.                                                                                                                                                       |
| **Refactoring**            | All developers are expected to **refactor** the code continuously as soon as possible code improvements are found. This keeps the code simple and maintainable.                                                                                                                                     |
| **Pair programming**       | Developers work in **pairs**, checking each other’s work and providing the support to always do a good job.                                                                                                                                                                                         |
| **Collective ownership**   | The pairs of developers work on all areas of the system, so that no islands of expertise develop and **all** the developers take **responsibility** for all of the code. Anyone can change anything.                                                                                                |
| **Continuous integration** | As soon as the work on a task is complete, it is integrated into the **whole** system. After any such integration, all the unit tests in the system must pass.                                                                                                                                      |
| **Sustainable pace**       | Large amounts of **overtime** are not considered acceptable as the net effect is often to reduce code quality and medium term productivity                                                                                                                                                          |
| **On-site customer**       | A representative of the **end-user** of the system (the customer) should be available full time for the use of the XP team. In an extreme programming process, the customer is a member of the development team and is responsible for bringing system requirements to the team for implementation. |


Pair programming:
![pair programming](https://miro.medium.com/v2/resize:fit:7676/1*sBJhFwmpfbftanqzxOeK_w.jpeg)

### XP and agile principles
* **Incremental development** is supported through small, frequent system releases.
* **Customer involvement** means full-time customer engagement with the team.
* **People** not process through pair programming, collective ownership and a process that avoids long working hours.
* **Change** supported through regular system releases.
* Maintaining **simplicity** through constant refactoring of code.

#### User stories for requirements
* In XP, a customer or user is part of the XP team and is responsible for making decisions on requirements.
* User requirements are expressed as user stories or scenarios.
* These are written on cards and the development team break them down into implementation tasks. These tasks are the basis of schedule and cost estimates.
* The customer chooses the stories for inclusion in the next release based on their priorities and the schedule estimates.

[More about **story**](https://www.agilebusiness.org/resource/user-stories.html)

#### A ‘prescribing medication’ story 

> Kate is a doctor who wishes to prescribe medication for a patient attending a clinic. The patient record is already displayed on her computer so she clicks on the medication field and can select current medication’, ‘new medication’ or ‘formulary’.
If she selects ‘current medication’, the system asks her to check the dose. If she wants to change the dose, she enters the dose and then confirms the prescription.
If she chooses ‘new medication’, the system assumes that she knows which medication to prescribe. She types the first few letters of the drug name. The system displays a list of possible drugs starting with these letters. She chooses the required medication and the system responds by asking her to check that the medication selected is correct. She enters the dose and then confirms the prescription.
If she chooses ‘formulary’, the system displays a search box for the approved formulary. She can then search for the drug required. She selects a drug and is asked to check that the medication is correct. She enters the dose and then confirms the prescription.
The system always checks that the dose is within the approved range. If it isn’t, Kate is asked to change the dose.
After Kate has confirmed the prescription, it will be displayed for checking. She either clicks ‘OK’ or ‘Change’. If she clicks ‘OK’, the prescription is recorded on the audit database. If she clicks on ‘Change’, she reenters the ‘Prescribing medication’ process.

> 凱特是一名醫生，她希望為去診所就診的患者開藥。病患記錄已經顯示在她的電腦上，因此她點擊藥物欄位，可以選擇「當前藥物」、「新藥物」或「處方集」。如果她選擇“當前藥物”，系統會要求她檢查劑量。 如果她想改變劑量，她可以輸入劑量，然後確認處方。如果她選擇“新藥物”，系統會假設她知道要開哪種藥物。她輸入了藥物名稱的前幾個字母。 系統顯示以這些字母開頭的可能藥物清單。她選擇所需的藥物，系統會做出回應，要求她檢查所選藥物是否正確。她輸入劑量，然後確認處方。如果她選擇“處方集”，系統會顯示已核准處方集的搜尋框。然後她可以尋找所需的藥物。她選擇一種藥物，並被要求檢查藥物是否正確。她輸入劑量，然後確認處方。系統始終檢查劑量是否在核准的範圍內。如果不是，凱特就會被要求改變劑量。凱特確認處方後，會顯示出來供檢查。她點擊“確定”或“更改”。如果她點擊“確定”，處方就會記錄在審核資料庫中。 如果她點擊“更改”，她將重新進入“開藥方”流程。

#### Examples of task cards for prescribing medication 

##### fig-tasks
<img src="https://hackmd.io/_uploads/HJjRW63n6.png" width="500">

:::success
:basketball: 活動
選擇一個系統，描述該系統內一個 story，並依據這個 story 來定義其 tasks：
* Ace 網球會員管理系統
* HappyBear 訂餐系統
* ezGo 旅遊規劃系統
* 喀嚓 相機租借系統
* ShowShow 電影訂位系統
* 逢大 選課系統
:::

#### Refactoring
* Conventional wisdom in software engineering is to design for change. It is worth spending time and effort anticipating changes as this reduces costs later in the life cycle.
* XP, however, maintains that this is not worthwhile as changes cannot be reliably anticipated.
* Rather, it proposes **constant code improvement** (refactoring) to make changes easier when they have to be implemented.
* Programming team look for possible software improvements and make these improvements even where there is no immediate need for them.
* This improves the understandability of the software and so reduces the need for documentation.
* Changes are easier to make because the code is well-structured and clear.
* However, some changes requires architecture refactoring and this is much more expensive.

:::success
:question: 請 LLM 依據房貸規則及滿足以下要求：
1. 寫一個青年房貸試算系統程式，執行速度儘量快
2. 寫一個青年房貸試算系統程式，程式設計儘可能的 "預期變化"

[青年房貸規則](https://www.nta.gov.tw/singlehtml/108)
:::

#### Examples of refactoring
* Re-organization of a class hierarchy to remove **duplicate** code.
* Tidying up and renaming attributes and methods to make them easier to **understand**.
* **Extract Method**: breaking down large or complex methods by extracting smaller, more focused methods. It helps improve readability and reusability. For example, if a method does multiple things, each task can be separated into its own method, making the code cleaner.
* **Rename Variables or Methods**: Giving descriptive names to variables or methods enhances code clarity. This refactoring makes it easier for others (and future you) to understand the code's purpose without needing excessive comments.

Refactoring:
![image alt](https://devopedia.org/images/article/266/1833.1588138932.png)


#### Test-first development
* Testing is central to XP and XP has developed an approach where the program is tested after every change has been made.
* XP testing features:
    * **Test-first** development.
    * Incremental test development from **scenarios**.
    * **User** involvement in test development and validation.
    * **Automated** test harnesses are used to run all component tests each time that a new release is built.
    * Tests are written as **programs** rather than data so that they can be executed automatically. The test includes a check that it has executed correctly.
    * Usually relies on a testing **framework** such as Junit.
    * All previous and new tests are run automatically when **new functionality** is added, thus checking that the new functionality has not introduced errors.

![](https://marsner.com/wp-content/uploads/test-driven-development-TDD.png)

#### Test case description for dose checking 

:::info
Test 4: Dose Checking
Input:
1. A number in mg representing a single dose of the drug.
2. A number representing the number of single doses per day.


Tests:
1. Test for inputs where the single dose is correct but the frequency is too high.
2. Test for inputs where the single dose is too high and too low.
3. Test for inputs where the single dose × frequency is too high and too low.
4. Test for inputs where single dose × frequency is in the permitted range.
Output:
OK or error message indicating that the dose is outside the safe range.
:::


#### Customer involvement
* **Continuous Feedback**: Agile promotes regular and frequent interaction with the customer. Instead of waiting until the end of the project, customers provide feedback throughout the development process, often at the end of each iteration or sprint. This ensures that the product is aligned with customer expectations and allows adjustments to be made quickly.
* **Participation in Planning**: Customers are actively involved in planning the project. They help define priorities, clarify requirements, and make decisions about which features or changes are most valuable. This happens during activities like backlog refinement, sprint planning, and review meetings.
* **Collaboration on User Stories**: Customers (or their representatives) help define user stories, which describe the features or requirements from the user's perspective. This helps the development team understand the desired functionality from a practical, user-centric viewpoint.
* **Sprint Reviews/Demos**: At the end of each sprint, the development team demonstrates the completed work to the customer. This gives the customer the chance to review the progress and suggest changes before the next sprint starts.
* **Prioritization of Work**: Customers play an important role in prioritizing tasks or features. Their feedback helps the team focus on high-value items first, ensuring the product delivers business value incrementally.
* Involving the customer in this iterative process leads to **higher satisfaction, faster delivery of valuable features, and reduced risk of building the wrong product**.
* However, people adopting the customer role have limited time available and so cannot work full-time with the development team. They may feel that providing the requirements was enough of a contribution and so may be reluctant to get involved in the testing process. 


:::success
:basketball: 活動

三角形檢查：為一個三角形型態檢查寫一個函式，在那之前，先寫一個測試案例
* int checkTriangle(int x, int y, int z); or 
* String checkTriangle(int x, int y, int z)
* (x, y, z) 為三邊長

:::


#### Test automation
* Test automation means that tests are written as **executable** components before the task is implemented 
* These testing components should be stand-alone, should simulate the submission of input to be tested and should check that the result meets the output specification. An automated test framework (e.g. Junit) is a system that makes it easy to write executable tests and submit a set of tests for execution. 
* As testing is automated, there is always a set of tests that can be quickly and easily executed
* Whenever any functionality is added to the system, the tests can be run and problems that the new code has introduced can be caught immediately.  

:::info
**Testability** 以下程式該如何切割模組，以提升其可測試性？
> 輸入一個數值(例如10000)，輸出小於該數的所有質數。
:::

version A:
```python=
for num in range(2, 10000):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
```

version B:

```python=
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_less_than(n):
    prime_list = []
    for i in range(2, n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

# 輸入數值
input_number = int(input("請輸入一個數值: "))

# 小於輸入數值的所有質數
result = prime_numbers_less_than(input_number)

print("小於", input_number, "的所有質數為:", result)
```
#### Problems with test-first development
* Programmers prefer programming to testing and sometimes they take short cuts when writing tests. For example, they may write incomplete tests that do not check for all possible exceptions that may occur. 
* Some tests can be very difficult to write incrementally. For example, in a complex user interface, it is often difficult to write unit tests for the code that implements the ‘display logic’ and workflow between screens. 
* It difficult to judge the completeness of a set of tests. Although you may have a lot of system tests, your test set may not provide complete coverage.  

#### Pair programming
* Pair programming involves programmers working in pairs, developing code together.
* This helps develop common **ownership** of code and spreads knowledge across the team.
* It serves as an informal **review** process as each line of code is looked at by more than 1 person.
* It encourages **refactoring** as the whole team can benefit from improving the system code.
* In pair programming, programmers **sit together** at the same computer to develop the software.
* Pairs are created dynamically so that all team members work with each other during the development process.
* The sharing of knowledge that happens during pair programming is very important as it reduces the overall risks to a project when team members leave.
* Pair programming is not necessarily inefficient and there is some evidence that suggests that a pair working together is more efficient than 2 programmers working separately. 


## Agile project management
* The principal responsibility of software project managers is to manage the project so that the software is delivered on time and within the planned budget for the project. 
* The standard approach to project management is plan-driven. Managers draw up a plan for the project showing what should be delivered, when it should be delivered and who will work on the development of the project deliverables. 
* Agile project management requires a different approach, which is adapted to incremental development and the practices used in agile methods. 

### Scrum
* Scrum is an agile method that focuses on **managing** iterative development rather than specific agile practices.

There are three phases in Scrum. 
* The **initial** phase is an outline planning phase where you establish the general objectives for the project and design the software architecture. 
* This is followed by a series of **sprint** cycles, where each cycle develops an increment of the system. 
* The project **closure** phase wraps up the project, completes required documentation such as system help frames and user manuals and assesses the lessons learned from the project.
 

#### Scrum terminology

##### fig-scrum-process

<img src="https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2023-09/scrum-framework-9.29.23.png">

:::success
:basketball: **活動**

註冊 trello, 嘗試 scrum board
:::

| Term                                        | description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Development team**                        | A **self-organizing** group of software developers, which should be no more than 7 people. They are responsible for developing the software and other essential project documents.                                                                                                                                                                                                                                                                                     |
| **Potentially shippable product increment** | The software increment that is delivered from a sprint. The idea is that this should be ‘potentially **shippable**’ which means that it is in a finished state and no further work, such as testing, is needed to  incorporate it into the final product. In practice, this is not always achievable.                                                                                                                                                                  |
| **Product backlog**                         | This is a list of ‘**to do**’ items which the Scrum team must tackle. They may be feature definitions for the software, software requirements, user stories or descriptions of supplementary tasks that are needed, such as architecture definition or user documentation.                                                                                                                                                                                             |
| **Product owner**                           | An individual (or possibly a small group) whose job is to identify **product features** or **requirements**, prioritize these for development and continuously review the product backlog to ensure that the project continues to meet critical business needs. The Product Owner can be a customer but might also be a product manager in a software company or other stakeholder representative.                                                                     |
| **Scrum meeting**                           | A **daily** meeting of the Scrum team that reviews progress and prioritizes work to be done that day. Ideally, this should be a short face-to-face meeting that includes the whole team.                                                                                                                                                                                                                                                                               |
| **ScrumMaster**                             | The ScrumMaster is responsible for ensuring that the Scrum **process** is followed and guides the team in the effective use of Scrum. He or she is responsible for interfacing with the rest of the company and for ensuring that the Scrum team is not diverted by **outside interference**. The Scrum developers are adamant that the ScrumMaster should not be thought of as a project manager. Others, however, may not always find it easy to see the difference. |
| **Sprint**                                  | A development **iteration**. Sprints are usually 2-4 weeks long.                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Velocity**                                | An estimate of how much product backlog effort that a team can cover in a single sprint.  Understanding a team’s velocity helps them estimate what can be covered in a sprint and provides a basis for measuring improving performance.                                                                                                                                                                                                                                |
| **Sprint retrospective**                    | a recurring meeting dedicated to discussing what went well and what can be improved in a sprint.                                                                                                                                                                                                                                                                                                                                                                       |




#### Scrum sprint cycle

* Sprints are fixed length, normally 2–4 weeks.  
* The starting point for planning is the product backlog, which is the list of work to be done on the project.
* The selection phase involves all of the project team who work with the customer to select the features and functionality from the product backlog to be developed during the sprint. 

#### The Sprint cycle
* Once these are agreed, the team **organize themselves** to develop the software. 
* During this stage the team is **isolated** from the customer and the organization, with all communications channelled through the so-called ‘**Scrum master**’. 
* The role of the Scrum master is to protect the development team from external distractions. 
* At the end of the sprint, the work done is reviewed and presented to stakeholders. The next sprint cycle then begins.

:::success
:basketball: 活動

敏捷遊戲：拋球與接球
:::

#### Teamwork in Scrum
* The **Scrum master** is a facilitator who arranges daily meetings, tracks the backlog of work to be done, records decisions, measures progress against the backlog and communicates with customers and management outside of the team.
* The whole team attends short **daily meetings** (Scrums) where all team members share information, describe their progress since the last meeting, problems that have arisen and what is planned for the following day. 
* This means that everyone on the team knows **what is going on** and, if problems arise, can re-plan short-term work to cope with them. 

#### Scrum benefits
* The product is broken down into a set of **manageable** and **understandable** chunks.
* Unstable requirements do not **hold up progress**.
* The whole team have **visibility** of everything and consequently team communication is improved.
* Customers see **on-time delivery** of increments and gain feedback on how the product works.
* **Trust** between customers and developers is established and a positive culture is created in which everyone expects the project to succeed.

