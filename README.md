# 🚀 Kasparro Agentic FB Ads Performance Analyzer

## 📌 Project Overview
An end-to-end multi-agent reasoning system designed to analyze Facebook Ads dataset, extract performance metrics, generate insights, validate hypotheses, and recommend creative improvements.

---

## ⚙️ Technology Stack
**Core Libraries Used**  
- Python 3.10+  
- Pandas, NumPy  
- ReportLab (PDF Generation)  
- Rich, Logging  
- Langchain-style LLM pipeline (Custom)  
- Gemini LLM API  
- JSON-based agent interfacing  

---

## 🧠 Agent Architecture & Execution Flow
```
User Query
   ↓
Planner Agent — Generates route & parameters
   ↓
Data Agent — Extracts & processes relevant dataset
   ↓
Insight Agent — Finds hypotheses, patterns, trends
   ↓
Evaluator Agent — Validates hypotheses & confirms evidence
   ↓
Creative Agent — Generates optimized creative suggestions
   ↓
report.md — Final compiled marketing report
```

---

## 🛠 Installation & Setup

### 🔹 Clone Repository
```bash
git clone <https://github.com/DANNE-SANDEEP/kasparro-agentic-fb-analyst-Sandeep-Danne.git>
cd project_folder
```

### 🔹 Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows
```

### 🔹 Install Requirements
```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure
```
src/
 ├── agents/
 │   ├── planner_agent.py
 │   ├── data_agent.py
 │   ├── insight_agent.py
 │   ├── evaluator_agent.py
 │   └── creative_agent.py
 ├── utils/
 │   ├── data_utils.py
 │   ├── logging_utils.py
 │   └── llm.py
 ├── orchestrator/
 │   └── run.py
 └── prompts/
     ├── planner.md
     ├── data_agent.md
     ├── insight_agent.md
     ├── evaluator.md
     └── creative.md
reports/
 ├── planner_output.json
 ├── data_output.json
 ├── insights.json
 ├── evaluation.json
 └── report.md
```

---

## ▶️ How to Run
Run the complete agent pipeline using:
```bash
python -m src.orchestrator.run
```

This will:
✔ Read user query  
✔ Execute agents based on planner strategy  
✔ Generate individual outputs (JSON)  
✔ Auto-generate final `report.md` inside `/reports`

---

## 📝 Example User Prompts

| Query Type | Example |
|------------|---------|
| Campaign Performance | *Give me spend, CTR, ROAS for Men ComfortMax last 14 days* |
| Root Cause | *Why did ROAS drop for Men ComfortMax in last week?* |
| Comparison | *Compare Men ComfortMax with Women FlexFit* |
| Hypothesis Validation | *Is creative fatigue causing ROAS drop?* |
| Creative Boost | *Suggest new ad variations for high CTR* |

---

## 🔍 Resulting Output Files

| File | Description |
|------|-------------|
| `planner_output.json` | Agent flow & task plan |
| `data_output.json` | Processed dataset summary |
| `insights.json` | Generated hypotheses |
| `evaluation.json` | Hypothesis validation |
| `creatives.json` | Recommended ad creatives |
| `report.md` | Final marketer-friendly report |

---

## 🧪 Validation Strategy
Evaluator Agent validates using:
- Metric trend consistency  
- Correlation between spend, CTR, ROAS  
- Audience saturation indicators  
- Data fragmentation detection  
- Cross-campaign logic integrity  

---

## 📌 Final Recommendations
✔ Standardize campaign naming to avoid fragmentation  
✔ Closely monitor ROAS after scaling budgets  
✔ Refresh creatives when CTR drops continuously  
✔ Use creative_agent suggestions to improve ad variations  
✔ Extend system with scheduling + auto-refresh  

---

📄 *Generated automatically using Kasparro Agentic FB Ad Intelligence System*  