# Kasparro Agentic FB Ads Analyst
## 🚀 Objective
An agentic AI system that analyzes Facebook ad performance, detects ROAS fluctuations, and generates creative improvement suggestions.

## 📂 Project Structure
```txt
kasparro-agentic-fb-analyst-yourname/
│
├── README.md
├── requirements.txt
├── Makefile / run.sh
├── config/
│   └── config.yaml
│
├── data/
│   ├── synthetic_fb_ads_undergarments.csv
│   └── README.md
│
├── src/
│   ├── orchestrator/
│   │   └── run.py
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   └── creative_agent.py
│   ├── utils/
│   │   ├── data_loader.py
│   │   ├── prompt_templates.py
│   │   ├── config_reader.py
│   │   └── logger.py
│   └── __init__.py
│
├── prompts/
│   ├── planner_prompt.md
│   ├── insight_prompt.md
│   ├── evaluator_prompt.md
│   └── creative_prompt.md
│
├── reports/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
│
├── logs/
│   ├── log_01.json
│   └── langfuse_trace_01.json
│
└── tests/
    ├── test_evaluator.py
    └── test_data_agent.py


## ⚙️ Setup
```bash
pip install -r requirements.txt