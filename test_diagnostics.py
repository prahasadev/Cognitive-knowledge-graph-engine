from main import KnowledgeGraph, Student, DiagnosticEngine


def test_find_weak_concepts():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")
    kg.add_node("lim", "Limits & Continuity")

    student = Student("s1", "Student 1", kg)
    student.add_assessment("alg", 90)
    student.add_assessment("lim", 40)

    engine = DiagnosticEngine(student)

    assert engine.find_weak_concepts() == ["lim"]


def test_trace_prerequisites():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")
    kg.add_node("lim", "Limits & Continuity")
    kg.add_node("der", "Derivatives")

    kg.add_edge("alg", "lim")
    kg.add_edge("lim", "der")

    student = Student("s1", "Student 1", kg)
    student.add_assessment("alg", 90)
    student.add_assessment("lim", 40)
    student.add_assessment("der", 30)

    engine = DiagnosticEngine(student)

    assert engine.trace_prerequisites("der") == ["lim"]


def test_recommend_study():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")
    kg.add_node("lim", "Limits & Continuity")
    kg.add_node("der", "Derivatives")

    kg.add_edge("alg", "lim")
    kg.add_edge("lim", "der")

    student = Student("s1", "Student 1", kg)
    student.add_assessment("alg", 90)
    student.add_assessment("lim", 40)
    student.add_assessment("der", 30)

    engine = DiagnosticEngine(student)

    assert engine.recommend_study("der") == ["lim"]
