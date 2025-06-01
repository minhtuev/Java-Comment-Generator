# 🧠 JavaCommentGenerator

**JavaCommentGenerator** is a Python tool that parses Java codebases, automatically generates meaningful comments for classes and methods, and visualizes the architecture via diagrams. It supports both rule-based and LLM-powered (via OpenRouter) comment generation.

---

## ✨ Features

- ✅ Automated Java code commenting  
- ✅ Visual architecture diagrams using Graphviz  
- ✅ Supports heuristic or LLM (GPT/Claude/Mixtral) generation  
- ✅ Non-intrusive: outputs `_commented.java` files  
- ✅ CLI-configurable and `.env`-friendly  

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/minhtuev/Java-Comment-Generator
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Graphviz

#### macOS

```bash
brew install graphviz
```

#### Ubuntu/Debian

```bash
sudo apt install graphviz
```

#### Windows

Download from https://graphviz.org/download and add it to your PATH.

---

## ⚙️ Configuration (Optional)

Create a `.env` file in the project root:

```env
API_KEY=sk-your-openrouter-token
MODEL=your-model-name
```

You can get your API key from https://openrouter.ai

---

## 🚀 Usage

### Basic Heuristic Commenting

```bash
python main.py
```

### LLM-Powered Commenting (via OpenRouter)

```bash
python main.py --token sk-... --model [model-name]
```

Or, if using `.env`:

```bash
python main.py
```

---

## 🔧 CLI Options

| Argument         | Description                                              | Default                      |
|------------------|----------------------------------------------------------|------------------------------|
| `--input`, `-i`  | Path to Java files                                       | `examples/`                  |
| `--output`, `-o` | Output diagram path (no extension)                       | `output/code_structure`      |
| `--token`, `-t`  | OpenRouter API token                                     | `None` (optional via `.env`) |
| `--model`, `-m`  | Model name (e.g. `mistral/mixtral-8x7b-instruct`)        | `None` (required if using LLM) |

---

## 📁 Example Structure

```
examples/
├── HelloWorld.java
├── Greeter.java

output/
├── HelloWorld_commented.java
├── Greeter_commented.java
├── code_structure.png
```

---

## 🧠 Supported OpenRouter Models

✅ Models are validated dynamically against OpenRouter’s live model list.

---

## 🧪 Example `.env`

```env
API_KEY=sk-your-token-here
MODEL=your-model-name
```

---

## 🖼 Output

- `_commented.java` files next to originals
- Diagram image at `output/code_structure.png`


---

## 📜 License

MIT License © 2025 Minh Tue Vo

---

## 🤝 Contributing

Pull requests and issues are welcome! Help us extend support, improve accuracy, or add new features.
