# 🧠 Model-Based Agent

A Python implementation of a **Model-Based AI Agent** with memory and state management.

---

# 🤖 What is a Model-Based Agent?

A Model-Based Agent can:

✅ remember past information
✅ use memory to make decisions
✅ maintain internal state

Unlike a Simple Reflex Agent, this agent does not rely only on current input.

---

# 🏗️ Architecture

```text
        +------------------+
        |   User Input     |
        +--------+---------+
                 |
                 v
        +------------------+
        |  Input Cleaner   |
        +--------+---------+
                 |
                 v
        +------------------+
        | Information      |
        | Extraction       |
        +--------+---------+
                 |
                 v
        +------------------+
        |     Memory       |
        +--------+---------+
                 |
                 v
        +------------------+
        | Decision Engine  |
        +--------+---------+
                 |
                 v
        +------------------+
        |     Output       |
        +------------------+
```

---

# 🔄 Agent Flow

```text
User → main.py → agent.py → processor.py → memory.py → Response
```

---

# 📂 Project Structure

```text
model-based-agent/
│
├── agent/
│   ├── memory.py
│   ├── processor.py
│   ├── rules.py
│   └── agent.py
│
├── main.py
├── README.md
└── .gitignore
```

---

# ⚙️ Features

✅ Stores user information
✅ Retrieves stored memory
✅ Handles multiple memory types
✅ Modular architecture
✅ Stateful behavior

---

# 🧠 Memory Capabilities

The agent can remember:

* user name
* location
* future expandable memory fields

---

# 🚀 How to Run

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 2️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 3️⃣ Run Agent

```bash
python main.py
```

---

# 🧪 Example Interaction

```text
You: my name is Ravi
Agent: Got it! I will remember your name is Ravi

You: what is my name
Agent: Your name is Ravi

You: i live in Chennai
Agent: Got it! I will remember your location is Chennai

You: where do i live
Agent: You live in Chennai
```

---

# 🧠 Core Concepts Learned

* Stateful agents
* Memory systems
* Information extraction
* Internal state management
* Modular AI architecture

---

# ⚠️ Limitations

* No learning
* No planning
* No reasoning
* Only remembers predefined information

---

# 🚀 Future Improvements

* Persistent memory
* Database integration
* Planning systems
* Multi-step reasoning
* Learning mechanisms

---

# 📚 Learning Outcome

This project demonstrates:

```text
Input + Memory → Decision → Action
```

---

# 🔥 Key Upgrade from Simple Reflex Agent

| Feature           | Simple Reflex | Model-Based |
| ----------------- | ------------- | ----------- |
| Memory            | ❌             | ✅           |
| State             | ❌             | ✅           |
| Context Awareness | ❌             | ✅           |
| Rule-Based        | ✅             | ✅           |

---
