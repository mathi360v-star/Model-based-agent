# 🧠 Model-Based AI Agent

A beginner-friendly implementation of a **Model-Based AI Agent** built using Python.

This project demonstrates how an AI agent can:

* Remember information 🧠
* Store user data 📦
* Retrieve past information 🔍
* Respond based on memory + current input 🤖

---

# 🚀 What is a Model-Based Agent?

A Model-Based Agent is an AI agent that:

> Uses both the **current input** and **stored memory (state)** to make decisions.

Unlike a Simple Reflex Agent, this agent can remember things told by the user.

---

# 🏗️ Architecture

```text
                 +------------------+
                 |    User Input    |
                 +---------+--------+
                           |
                           v
                 +------------------+
                 | Input Processing |
                 +---------+--------+
                           |
                           v
                 +------------------+
                 |  Memory System   |
                 | (Store/Retrieve) |
                 +---------+--------+
                           |
                           v
                 +------------------+
                 | Decision Engine  |
                 +---------+--------+
                           |
                           v
                 +------------------+
                 |      Output      |
                 +------------------+
```

---

# 🔄 Agent Flow

```text
User Input
    ↓
Clean Input
    ↓
Extract Information
    ↓
Store / Retrieve Memory
    ↓
Generate Response
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

# 🧠 Components Explained

| File           | Responsibility                             |
| -------------- | ------------------------------------------ |
| `memory.py`    | Stores and retrieves user information      |
| `processor.py` | Cleans and extracts information from input |
| `rules.py`     | Stores predefined reflex rules             |
| `agent.py`     | Main decision-making logic                 |
| `main.py`      | Runs the application                       |

---

# ⚙️ Features

✅ Stores user name
✅ Stores user location
✅ Retrieves stored memory
✅ Handles input cleaning
✅ Modular architecture
✅ Beginner-friendly design

---

# 🛠️ Technologies Used

* Python 3.12
* Object-Oriented Programming (OOP)
* Rule-Based Processing
* State Management

---

# ▶️ How to Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/model-based-agent.git
```

---

## 2️⃣ Move into Project Folder

```bash
cd model-based-agent
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
py -3.12 -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3.12 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Run the Agent

```bash
python main.py
```

---

# 🧪 Example Conversation

```text
You: my name is Ravi
Agent: Got it! I will remember your name is Ravi

You: i live in Chennai
Agent: Got it! I will remember your location is Chennai

You: what is my name
Agent: Your name is Ravi

You: where do i live
Agent: You live in Chennai
```

---

# 🧠 Memory Example

The agent internally stores data like:

```python
{
    "name": "Ravi",
    "location": "Chennai"
}
```

---

# 🔥 Key Concepts Learned

* Stateful AI Systems
* Memory Management
* Information Extraction
* Input Processing
* Modular Architecture
* Rule-Based Decision Systems

---

# ⚠️ Limitations

❌ No long-term memory persistence
❌ No machine learning
❌ No reasoning/planning
❌ No natural language understanding

This project is designed for learning foundational AI agent architecture.

---

# 🚀 Future Improvements

* Save memory to file/database
* Add multiple users
* Add conversation history
* Add planning system
* Integrate LLMs
* Build Goal-Based Agent

---

# 🎯 Learning Goal

This project teaches the core principle of modern AI systems:

> Current Input + Memory = Smarter Decisions

---

# 👨‍💻 Author

Built while learning different types of AI agents step-by-step.

---
