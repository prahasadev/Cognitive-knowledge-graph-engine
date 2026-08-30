class KnowledgeNode:
    def __init__(self, node_id, name, score=0.0):
        self.id = node_id
        self.name = name
        self.score = score
        self.prerequisites = []
        self.dependents = []

    def add_dependent(self, target_node):
        self.dependents.append(target_node)
        target_node.prerequisites.append(self)

    def __repr__(self):
        return f"[{self.name} | Score: {self.score}]"

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id, name, score=0.0):
        if node_id in self.nodes:
            raise ValueError(f"Node ID '{node_id}' already exists.")

        node = KnowledgeNode(node_id, name, score)
        self.nodes[node_id] = node
        return node

    def add_edge(self, prereq_id, dep_id):
        if prereq_id in self.nodes and dep_id in self.nodes:
            self.nodes[prereq_id].add_dependent(self.nodes[dep_id])

    def display_graph(self):
        print("=== V1 Cognitive Knowledge Graph ===\n")
        for node_id, node in self.nodes.items():
            prereqs = [p.name for p in node.prerequisites]
            deps = [d.name for d in node.dependents]
            
            print(f"Node: {node.name} (Score: {node.score})")
            print(f"  Requires: {', '.join(prereqs) if prereqs else 'None'}")
            print(f"  Unlocks:  {', '.join(deps) if deps else 'None'}\n")

if __name__ == "__main__":
    kg = KnowledgeGraph()

    kg.add_node("alg", "Basic Algebra", score=90.0)
    kg.add_node("lim", "Limits & Continuity", score=75.0)
    kg.add_node("der", "Derivatives", score=45.0)
    kg.add_node("opt", "Optimization", score=0.0)

    kg.add_edge("alg", "lim")
    kg.add_edge("lim", "der")
    kg.add_edge("der", "opt")

    kg.display_graph()
