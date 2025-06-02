# 🧠 JavaCommentGenerator

**JavaCommentGenerator** is a Python tool that parses Java codebases, automatically generates meaningful comments for classes and methods, and visualizes the architecture via diagrams. It supports both rule-based and LLM-powered (via OpenRouter) comment generation.

---

## ✨ Features

- ✅ Automated Java code commenting  
- ✅ Visual architecture diagrams using Graphviz  
- ✅ Supports heuristic or LLM (GPT/Claude/Mixtral) generation  
- ✅ Non-intrusive: outputs `_commented.java` files  
- ✅ CLI-configurable and `.env`-friendly  
- ✅ Extracts class-level dependencies for diagram links

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/minhtuev/Java-Comment-Generator
cd Java-Comment-Generator
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

### 4. (Optional) Install as CLI Tool

```bash
pip install -e .
```

Then run:

```bash
javacommentgenerator --generator default
```

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

### Heuristic Commenting (Default Generator)

```bash
javacommentgenerator --generator default
```

### LLM-Powered Commenting (OpenRouter)

```bash
javacommentgenerator --generator openrouter --token sk-... --model deepseek/deepseek-r1-0528-qwen3-8b:free
```

Or use values from `.env`:

```bash
javacommentgenerator --generator openrouter
```

---

## 🧩 Using CodeComprehender in Python

```python
from code_comprehender import CodeComprehender
from comment_generators.openrouter_generator import OpenRouterCommentGenerator

generator = OpenRouterCommentGenerator(
    token="sk-your-openrouter-token",
    model="deepseek/deepseek-r1-0528-qwen3-8b:free"
)

comprehender = CodeComprehender("examples", "output/code_structure", generator)
comprehender.run()
```

---

## 🔧 CLI Options

| Argument         | Description                                              | Default                      |
|------------------|----------------------------------------------------------|------------------------------|
| `--input`, `-i`  | Path to Java files                                       | `examples/`                  |
| `--output`, `-o` | Output diagram path (no extension)                       | `output/code_structure`      |
| `--token`, `-t`  | OpenRouter API token                                     | `None` (optional via `.env`) |
| `--model`, `-m`  | Model name (e.g. `deepseek/deepseek-r1-0528-qwen3-8b:free`) | `None` (required if using LLM) |
| `--generator`, `-g` | Comment generator to use (`default` or `openrouter`) | `None` (optional)            |

---

## 📁 Example Java Files

```
examples/
├── hello_world/
│   ├── HelloWorld.java
│   └── Greeter.java
└── parking/
    ├── Car.java
    ├── ParkingGarage.java
    └── Main.java
```

---

## 🖼 Output Artifacts

```
examples/
├── hello_world/
│   ├── HelloWorld_commented.java
│   └── Greeter_commented.java
└── parking/
    ├── Car_commented.java
    ├── ParkingGarage_commented.java
    └── Main_commented.java

output/
└── code_structure.png
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

## 📜 License

MIT License © 2025 Minh Tue Vo

---

## 🤝 Contributing

Pull requests and issues are welcome! Help us extend support, improve accuracy, or add new features.

---

## 🔮 Future Work

- 🚀 Support for Gemini and OpenAI models
- ⚙️ Support for parallel processing (threading & multiprocessing)
- 📂 Support for deep project analysis (inter-package references, method call trees)
