# Cognitive Knowledge Graph Engine

A prerequisite-aware knowledge graph designed to represent relationships between concepts and support future student learning analysis.

## V1 — Foundation

V1 establishes the core knowledge graph structure.

###Features

- Concept nodes with names and scores
- Prerequisite and dependent relationships
- Duplicate-node and duplicate-edge protection
- Validation for missing nodes and self-referencing edges
- Score validation
- Node lookup
- Graph summary
- Cycle detection
- Basic graph tests

### Example

The current demo models:

Basic Algebra → Limits & Continuity → Derivatives → Optimization

### Testing

Run:

python test_graph.py

The tests verify node lookup, relationships, valid graph structure, and cycle detection.

## V2 — Student Data and Mastery Tracking

V2 adds a student model that connects individual assessment results to the knowledge graph.

### Features

- Student profiles linked to a knowledge graph
- Assessment tracking for individual concepts
- Multiple assessment scores stored as history
- Validation for concepts and assessment scores
- Mastery calculation from assessment history
- Student model tests

### Example

A student can have multiple assessments for the same concept:

70, 80, 90 → Mastery: 80.0

### Testing

Run:

python test_student.py

The tests verify student creation, assessment history, mastery calculation, and validation.

## V3 — Diagnostic Engine

V3 adds diagnostic features that use student mastery and prerequisite relationships to identify what the student should study.

### Features

- Weak concept detection
- Prerequisite weakness tracing
- Study recommendations
- Diagnostic engine tests

### Example

If a student is weak in Derivatives and also has weak prerequisite knowledge in Limits & Continuity, the engine recommends studying Limits & Continuity first.

### Testing

Run:

python test_diagnostic.py

The tests verify weak concept detection, prerequisite tracing, and study recommendations.

### Future Development
- V4: Research experiment
- V5: Analysis and final system
