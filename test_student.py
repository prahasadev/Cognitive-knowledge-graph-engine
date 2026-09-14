from main import KnowledgeGraph, Student


def test_student_creation():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")

    student = Student("s1", "Student 1", kg)

    assert student.id == "s1"
    assert student.name == "Student 1"
    assert student.knowledge_graph == kg


def test_assessment_history():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")

    student = Student("s1", "Student 1", kg)

    student.add_assessment("alg", 70)
    student.add_assessment("alg", 80)
    student.add_assessment("alg", 90)

    assert student.assessments["alg"] == [70, 80, 90]


def test_mastery_calculation():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")

    student = Student("s1", "Student 1", kg)

    student.add_assessment("alg", 70)
    student.add_assessment("alg", 80)
    student.add_assessment("alg", 90)

    assert student.get_mastery("alg") == 80.0


def test_invalid_concept():
    kg = KnowledgeGraph()

    student = Student("s1", "Student 1", kg)

    try:
        student.add_assessment("unknown", 80)
        assert False
    except ValueError:
        assert True


def test_invalid_score():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")

    student = Student("s1", "Student 1", kg)

    try:
        student.add_assessment("alg", 120)
        assert False
    except ValueError:
        assert True


def test_missing_mastery():
    kg = KnowledgeGraph()
    kg.add_node("alg", "Basic Algebra")

    student = Student("s1", "Student 1", kg)

    try:
        student.get_mastery("alg")
        assert False
    except ValueError:
        assert True
