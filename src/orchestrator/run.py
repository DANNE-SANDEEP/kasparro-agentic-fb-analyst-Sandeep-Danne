import json
import os
from datetime import datetime
from src.agents.planner_agent import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent
from src.utils.logging_utils import Logger, log_info, log_error  # 👈 NEW


def save_output(filename, content, folder="reports"):
    """Save agent outputs to /reports folder as JSON or Markdown."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    if filename.endswith(".json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"📁 Saved: {path}")
    return path


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
        ██╗  ██╗ █████╗ ███████╗██████╗  █████╗ ██████╗ ██████╗  ██████╗ 
        ██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
        █████╔╝ ███████║███████╗██████╔╝███████║██████╔╝██████╔╝██║   ██║
        ██╔═██╗ ██╔══██║╚════██║██╔═══╝ ██╔══██║██╔══██╗██╔══██╗██║   ██║
        ██║  ██╗██║  ██║███████║██║     ██║  ██║██║  ██║██║  ██║╚██████╔╝
        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
          """)
    print(" 📊 Kasparro Agentic FB Ad Performance Analyzer")
    print(" 🤖 Multi-Agent Reasoning System")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def main():
    display_banner()
    logger = Logger(log_folder="logs")  # 👈 Initialize logger

    user_query = input("\n💬 Enter your analysis request:\n> ")

    # 👉 Planner Agent
    planner_log = logger.start("PlannerAgent")
    planner = PlannerAgent()
    planner_output = planner.run(user_query)
    logger.end(extra={"output_preview": planner_output})
    save_output("planner_output.json", planner_output)

    agent_flow = planner_output.get("agent_flow", ["data_agent"])
    print(f"\n🔀 Agent Execution Flow: {agent_flow}")

    # 👉 Data Agent
    data_log = logger.start("DataAgent")
    data_agent = DataAgent()
    data_output = data_agent.run(planner_output)
    logger.end(extra={"output_preview": list(data_output.keys())})
    save_output("data_output.json", data_output)

    insight_output = None
    eval_output = None
    creative_output = None

    # 🔁 Dynamic Agent Execution
    for agent in agent_flow[1:]:
        if agent == "insight_agent":
            insight_log = logger.start("InsightAgent")
            insight_agent = InsightAgent()
            insight_output = insight_agent.run(
                data_agent_output=data_output,
                objective=planner_output.get("objective")
            )
            logger.end(extra={"hypotheses_count": len(insight_output)})
            save_output("insights.json", insight_output)

        elif agent == "evaluator_agent":
            evaluator_log = logger.start("EvaluatorAgent")
            evaluator_agent = EvaluatorAgent()
            eval_output = evaluator_agent.run(
                objective=planner_output.get("objective"),
                data_agent_output=data_output,
                insight_output=insight_output
            )
            logger.end(extra={"validated_hypotheses": len(eval_output)})
            save_output("evaluation.json", eval_output)

        elif agent == "creative_agent":
            creative_log = logger.start("CreativeAgent")
            creative_agent = CreativeAgent()
            creative_output = creative_agent.run(
                objective=planner_output.get("objective"),
                insight_output=insight_output,
                data_agent_output=data_output
            )
            logger.end(extra={"recommendation_count": len(creative_output)})
            save_output("creatives.json", creative_output)

    # 📁 AUTO-GENERATE report.md
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "report.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 📊 Facebook Ads Performance Analysis Report\n\n")
        f.write(f"🕒 **Generated On:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"💬 **User Query:** {user_query}\n")
        f.write("\n---\n")

        f.write("## 🎯 Planner Objective\n")
        f.write("```json\n")
        f.write(json.dumps(planner_output, indent=4))
        f.write("\n```\n")

        f.write("## 📈 Campaign Performance Summary\n")
        f.write("```json\n")
        f.write(json.dumps(data_output, indent=4))
        f.write("\n```\n")

        if insight_output:
            f.write("\n## 💡 Insights & Hypotheses\n```json\n")
            f.write(json.dumps(insight_output, indent=4))
            f.write("\n```\n")

        if eval_output:
            f.write("\n## 🧪 Hypothesis Evaluation\n```json\n")
            f.write(json.dumps(eval_output, indent=4))
            f.write("\n```\n")

        if creative_output:
            f.write("\n## 🎨 Creative Recommendations\n```json\n")
            f.write(json.dumps(creative_output, indent=4))
            f.write("\n```\n")

        f.write("\n---\n## 📌 Final Marketing Action Plan\n")
        f.write("✔ Avoid inefficient scaling — analyze spend-to-ROAS trend\n")
        f.write("✔ Improve audience freshness to prevent saturation\n")
        f.write("✔ Refresh creatives when CTR drops\n")
        f.write("✔ Standardize campaign naming for better data analysis\n")

    print(f"\n📄 Final Report saved to: {report_path}")
    print("\n✨ All agent outputs and logs saved.")
    print("\n🎯 Final Output Delivered.")


if __name__ == "__main__":
    main()