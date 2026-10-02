from graph.planner import needs_planning

print(needs_planning({"messages": [{"role": "user", "content": "What is 15% of 840?"}]}))       # False
print(needs_planning({"messages": [{"role": "user", "content": "Summarise my notes and create tasks for the hard topics"}]}))  # True