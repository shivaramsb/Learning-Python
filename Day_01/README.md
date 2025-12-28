# Day 1: Python Basics & Setup 🐍

Welcome to Day 1 of your Python learning journey!

## 📁 Files in This Directory

| File | Description |
|------|-------------|
| `01_tutorial.md` | Complete Day 1 tutorial with all concepts |
| `02_examples.py` | Runnable code examples for all topics |
| `03_exercises.py` | 8 practice exercises with solutions |
| `04_calculator_project.py` | Mini-project: Advanced calculator |
| `README.md` | This file - your starting point |

---

## 🎯 Learning Path

Follow this order for best results:

### Step 1: Read the Tutorial (30-45 min)
Open `01_tutorial.md` and read through all sections:
- Environment setup
- Variables and data types
- Operators
- Input/output
- Code formatting

### Step 2: Run the Examples (30 min)
```bash
python 02_examples.py
```
Study the output and understand each section.

### Step 3: Complete Exercises (2-3 hours)
Open `03_exercises.py` and solve all 8 exercises:
- Try solving each yourself first
- Solutions are at the bottom of the file
- Run individual solutions to test

### Step 4: Build the Calculator (1 hour)
Work on `04_calculator_project.py`:
- Start with the basic version
- Test all operations
- **Bonus**: Implement the enhanced version with history

---

## ✅ Day 1 Checklist

Before moving to Day 2, make sure you:

- [ ] **Setup**: Python installed and working
- [ ] **IDE**: VS Code or PyCharm configured
- [ ] **Understand**: Variables and all 4 data types (int, float, str, bool)
- [ ] **Master**: All 3 operator types (arithmetic, comparison, logical)
- [ ] **Practice**: Input/output with f-strings
- [ ] **Complete**: All 8 exercises in `03_exercises.py`
- [ ] **Build**: Working calculator project
- [ ] **Code Style**: Can write clean, commented code

---

## 🧪 Quick Self-Test

Can you answer these without looking?

1. What's the difference between `/` and `//`?
2. How do you convert a string to an integer?
3. What does the `%` operator do?
4. How do you format a float to 2 decimal places in an f-string?
5. What's the difference between `=` and `==`?

**Answers:**
1. `/` is division (returns float), `//` is floor division (returns int)
2. `int("25")` converts string "25" to integer 25
3. Modulus operator - returns remainder of division
4. `f"{value:.2f}"`
5. `=` is assignment, `==` is comparison

---

## 💡 Pro Tips

### Debugging
```python
# Use print() to debug
x = 10
print(f"x = {x}")  # See what value x has

# Check types when confused
print(type(x))  # <class 'int'>
```

### Common Mistakes
```python
# ❌ Wrong: Trying to add string and number
age = "25"
next_year = age + 1  # TypeError!

# ✅ Correct: Convert first
age = int("25")
next_year = age + 1  # Works!
```

### F-string Power
```python
name = "Alice"
score = 95.567

# Expression support
print(f"{name}'s next score: {score + 5}")

# Formatting
print(f"Score: {score:.2f}")  # 95.57
print(f"{name:>10}")  # Right-align in 10 spaces
```

---

## 🚀 Practice Resources

### Online Practice
- [HackerRank Python](https://www.hackerrank.com/domains/python) - Basic challenges
- [Exercism Python Track](https://exercism.org/tracks/python) - Mentored exercises
- [Python Tutor](http://pythontutor.com/) - Visualize code execution

### Documentation
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

### Videos
- freeCodeCamp - Python for Beginners
- Corey Schafer - Python Basics

---

## ❓ Common Questions

**Q: Do I need to memorize everything?**  
A: No! Focus on understanding concepts. You'll memorize syntax naturally through practice.

**Q: How much time should I spend on Day 1?**  
A: 4-5 hours total. Don't rush - solid basics are crucial!

**Q: What if I'm stuck on an exercise?**  
A: Try for 15-20 minutes, then check the solution. Understand why it works, then try a similar problem.

**Q: Should I install virtual environments now?**  
A: Basic understanding is enough for now. You'll use them from Day 6 onwards for data science packages.

---

## 📝 Notes Section

Use this space to write your own notes:

**Key Learnings:**
- 
- 
- 

**Challenges I Faced:**
- 
- 

**Questions for Later:**
- 
- 

---

## ⏭️ What's Next?

**Tomorrow (Day 2): Control Flow & Functions**

You'll learn:
- `if`, `elif`, `else` statements
- `for` and `while` loops
- Creating functions
- Lambda expressions
- List comprehensions

**Preparation:**
- Make sure you're comfortable with all Day 1 topics
- Complete the calculator project
- Get a good night's sleep! 😴

---

**Remember**: Everyone learns at their own pace. It's okay to spend extra time on Day 1 if needed. Understanding fundamentals is more important than speed!

Happy Coding! 🎉

---

**Need Help?**
- Stack Overflow: [python tag](https://stackoverflow.com/questions/tagged/python)
- Reddit: [r/learnpython](https://reddit.com/r/learnpython)
- Python Discord: [discord.gg/python](https://discord.gg/python)
