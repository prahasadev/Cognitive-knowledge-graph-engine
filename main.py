class KnowledgeNode:
    def __init__(self, node_id, name, score=0.0):
        self.id = node_id
        self.name = name
        self.score = score
        self.prerequisites = []
        self.dependents = []

    def add_dependent(self, target_node):
        if target_node not in self.dependents:
            self.dependents.append(target_node)

        if self not in target_node.prerequisites:
            target_node.prerequisites.append(self)

    def __repr__(self):
        return f"[{self.name} | Score: {self.score}]"

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id, name, score=0.0):
        if node_id in self.nodes:
           raise ValueError(f"Node ID '{node_id}' already exists.")

        if not 0 <= score <= 100:
           raise ValueError("Score must be between 0 and 100.")

        node = KnowledgeNode(node_id, name, score)
        self.nodes[node_id] = node
        return node

    def get_node(self, node_id):
        if node_id not in self.nodes:
            raise ValueError(f"Node ID '{node_id}' does not exist.")
        return self.nodes[node_id]

    def add_edge(self, prereq_id, dep_id):
        if prereq_id == dep_id:
            raise ValueError("A node cannot be its own prerequisite.")

        if prereq_id not in self.nodes:
            raise ValueError(f"Prerequisite node '{prereq_id}' does not exist.")

        if dep_id not in self.nodes:
            raise ValueError(f"Dependent node '{dep_id}' does not exist.")

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
