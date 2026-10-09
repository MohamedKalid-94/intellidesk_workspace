from langgraph.graph import StateGraph, END
from graph.state import AgentState

def noop_node(state):
    return state

g = StateGraph(AgentState)
g.add_node("noop", noop_node)
g.set_entry_point("noop")
g.add_edge("noop", END)
app = g.compile()

result = app.invoke({"messages": [{"role": "user", "content": "hi"}], "plan": None, "current_step": 0, "user_id": "u1", "project_id": "p1"})
print(result)