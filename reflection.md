# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

After I won the game once and clicked the new game button, a new secret number was generated. I expected the app to provide feedback for my guess once I hit submit, but the submit guess button didn't do anything anymore.

The secret number was 98. I first entered 100, and the app correctly said "go lower." Then I tried 99, and the app said "go higher" when it should've still said "go lower."

The secret number was 90. I entered 50, and the app said "go lower" when it should've said "go higher."

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret: 98 Input 1: 100 Input 2: 99 | "Go lower" "Go lower" | "Go lower" "Go higher" | none |
| Secret: 90 Input: 50 | "Go higher" | "Go lower" | none |
| After correct guess and pressing "New Game." Input: Submit Guess | "Go higher" or "Go lower" | No output | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
