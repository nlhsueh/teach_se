
## 0:00 - 1:00 | Introduction & Aim
Slide 1 & 2
"Good afternoon, everyone. Welcome to Software Engineering. Today, we are diving into an incredibly essential topic for building any successful software: an Introduction to User Experience Design.
In this session, we want to address three core elements:
* What User Experience—or UX—actually is. 
* Why it is absolutely critical to the survival of a product. 
* And How we achieve it using a very famous guideline: Nielsen’s Usability Heuristics, focusing specifically today on the Visibility of System Status. 

Let's start with the basics."

## 1:00 - 2:30 | What is User Experience (UX)?
Slide 3 & 4
"What is User Experience? By definition, UX is how a user interacts with and experiences a product, system, or service. It fundamentally includes a person’s internal perceptions of utility, ease of use, and efficiency.

At its heart, UX is about problem-solving —removing friction to solve real user pain points. However, it also includes psychological phenomena like the aesthetic-usability effect, which shows that users genuinely perceive beautiful designs as more usable.

Let's see this in action with an example we all use daily: a Food Delivery App.
* The Utility is simple: finding the right restaurant when you're hungry. 
* The Ease of Use & Efficiency comes into play when you can check out in just 3 clicks or track your rider moving in real-time on a map. 
* The Problem-Solving removes the friction of the classic 'What should I eat?' dilemma by providing smart recommendations. 
* And finally, the Aesthetic-Usability Effect: high-quality food imagery and a clean user interface don't just look pretty—they make the entire app feel faster, safer, and more reliable to the consumer." 

## 2:30 - 4:00 | Clarifying UI vs. UX & Core Concepts
Slide 5, 6 & 7
"Now, a common mistake people make in software development is confusing UI with UX. But remember: a beautiful UI does not guarantee a good UX.

The User Interface (UI) represents all the external, visual aspects you see and interact with. The User Experience (UX) is your internal cognitive and emotional response during that interaction.

So, The figure in the right side is a popular figure to see their difference. Which one reporesents the UX? A or B?

To give you a real-world analogy, look at this bicycle. Each part inside could be gorgeous and expensive. This state-of-the-art bike is costing ten thousand dollars! But if you ride it and it gives you severe knee and back pain, the User Experience is terrible. Expensive does not guarantee good UX.

Let me test your understanding with three quick questions: (10 second to answer)
1. If a website has no technical bugs and loads instantly, does it automatically have a good UX? 
  * The answer is No. UX user perception, not only technical issues.  
1. Can we evaluate the UX of a physical product, like a microwave or vending machine? 
  * The answer is Yes. UX applies to everything humans interact with. 
1. What if an app is easy to use and beautiful, but doesn't solve any problem or provide any value? 

Please write your answer in the chat, by Yes or No. 

## 4:00 - 5:30 | Why UX Matters (Real-World Failures)
Slide 8, 9, 10, 11 & 12
"So, why is UX important? Because software engineering isn't just about writing code that compiles; it's about humans using that code. When people encounter bad UX, they feel embarrassed, irritated, wronged, confused, frustrated, and angry.

UX is everywhere in life. Take, for example, a concept known as a 'Norman Door'. Have you ever walked up to a door with a massive vertical handle, pulled it with all your might, only to realize it's a 'PUSH' door? The visual design tricked your brain. That's a UX failure in physical architecture.

Look at these other real-life disasters on Slide 12: An ATM built so high that a user literally has to rock climb to press the keys ; a bathroom door with a chunk cut out of it because someone miscalculated the clearance with the toilet ; or a fire hydrant encased tightly behind a staircase handrail so nobody can open it in an emergency. These are hilarious, but dangerous design failures."

5:30 - 7:00 | Web & Mobile App Failures

Slide 13, 14, 15, 16 & 17
"The exact same tragedies happen in digital software engineering. Look at these websites on Slides 13, 14, and 15. They are text-heavy, chaotic, structurally messy, and visually overwhelming. They suffer from extreme cognitive friction.

Let's look at a local mobile app example on Slide 16. During the pandemic, users opened this health app wanting to pre-order face masks. Looking at the initial interface layout, it was highly confusing to know which option to select. Is it option 1? Option 5? Option 6?

Because of user feedback, they later redesigned it—as seen on Slide 17. They clearly highlighted an icon labeled 'eMask' with a distinct graphic. This tiny change instantly transformed a frustrating experience into a successful one."

7:00 - 9:00 | How? Nielsen's Usability Heuristics
Slide 19, 20, 21, 22 & 23

"So, how do we systematically design a system with good UX? It is not easy, but thankfully, we have Nielsen’s Usability Heuristics to guide us. Jakob Nielsen established 10 core heuristics—or general rules of thumb—for interaction design.
Today, let's look at Heuristic #1: Visibility of System Status. The rule states: 'The system should always keep users informed about what is going on, through appropriate feedback within a reasonable time.'

Think of a standard pedestrian traffic light. It doesn't just show a red man; it displays a countdown timer. It tells you exactly how many seconds you have left to wait or cross. That is visibility of status.

In software, look at the contrast on Slide 22. If a user tries to upload 100 files, and the app just displays a static grey box, the user thinks: 'Has the system crashed?' But if you add a progress bar, individual checkmarks, and live status updates, the user feels safe, thinking: 'Great, I know it is actively uploading.'
Good visibility of status means:
* Clearly notifying unread messages (like a red badge on a bell icon). 
* Instant error warnings if someone types an invalid email address right as they type it, rather than waiting until they submit the form. 
* Clearly stating step progression, showing the user they are currently at Step 2 out of 4." 

9:00 - 10:00 | Conclusion & Wrap-Up
Slide 24 & 25

"To wrap up our session today, let’s test our mobile phone calculators with a famous old software glitch: try typing 75 minus 37.5 on an old system. If it equals 0, that's a system processing status bug we need to avoid!
Let's review the Summary Triangle of UX Design:
1. WHAT: UX is more than just raw utility or efficiency; it is active problem-solving beautifully designed to ease user interaction. 
2. WHY: No matter how powerful or revolutionary your backend features are, a system with poor UX will cause severe frustration and user anger, ultimately leading to total product failure. 
3. HOW: We utilize Design Heuristics as an engineering framework to systematically discover interaction bugs, eliminate cognitive friction, and ensure excellent system feedback. 

As software engineers, always remember: build your systems not just for machines, but for the minds of the people using them.
Thank you very much, and I am happy to take any questions!"
