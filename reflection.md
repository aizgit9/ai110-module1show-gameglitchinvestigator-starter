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

I used Claude Code. 
In the new game handler, Claude suggested to add two lines:
  st.session_state.status = "playing"
  st.session_state.history = []
This was correct, I verified it by analyzing the issue on my own, testing the code, and identifying the issue to compare with the AI output. 

To be honest, the AI didn't make any mistakes as far as I could tell. I made sure to make all my prompts very specific and clear, and nothing unexpected or misleading was produced.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided whether a bug was fixed by running my test suite and interacting with the streamlit app myself to check everything was working correctly.

In the test_guess_too_high function, I ran the check_guess function with a guess of 60 and the secret as 50. I could tell the code worked correctly if "Too High" was returned.

Yes, building the tests was a pretty basic task that was much more efficient for AI to handle. I prompted it to design minimal tests for each bug I encountered. This saved me a lot of time.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time a user interacts with a Streamlit app, the entire script reruns and all variables are reverted to their original values. The session state variable can be used to store values across reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

A couple habits I want to reuse are reviewing the code carefully on my own in addition to asking AI for help. Also, providing clear and specific prompts is vital for staying on track and preventing errors. I also need to build more robust testing functions for my future projects, as I usually neglect them. Testing is extremely important. I used to think AI generated code was unreliable, but in this project it worked extremely well and I didn't find any problems with it.