from graph.planner import planner_node
result = planner_node({"messages": [{"role": "user", "content": "Summarise my notes and create a task for each difficult topic"}]})
print(result)