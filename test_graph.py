from main import KnowledgeGraph

kg = KnowledgeGraph()

kg.add_node("alg", "Basic Algebra", score=90.0)
kg.add_node("lim", "Limits & Continuity", score=75.0)
kg.add_node("der", "Derivatives", score=45.0)

kg.add_edge("alg", "lim")
kg.add_edge("lim", "der")

assert kg.get_node("alg").name == "Basic Algebra"

assert kg.get_node("lim") in kg.get_node("alg").dependents
assert kg.get_node("alg") in kg.get_node("lim").prerequisites

assert kg.validate_graph() is True

cycle_kg = KnowledgeGraph()

cycle_kg.add_node("a", "A")
cycle_kg.add_node("b", "B")

cycle_kg.add_edge("a", "b")
cycle_kg.add_edge("b", "a")

try:
    cycle_kg.validate_graph()
    assert False, "Cycle was not detected"
except ValueError:
    pass

print("All graph tests passed!")
