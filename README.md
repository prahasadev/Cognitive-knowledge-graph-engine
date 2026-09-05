# Cognitive Knowledge Graph Engine

A prerequisite-aware knowledge graph designed to represent relationships between concepts and support future student learning analysis.

# V1 — Foundation

V1 establishes the core knowledge graph structure.

# Features

- Concept nodes with names and scores
- Prerequisite and dependent relationships
- Duplicate-node and duplicate-edge protection
- Validation for missing nodes and self-referencing edges
- Score validation
- Node lookup
- Graph summary
- Cycle detection
- Basic graph tests

# Example

The current demo models:

Basic Algebra → Limits & Continuity → Derivatives → Optimization

# Testing

Run:

python test_graph.py

The tests verify node lookup, relationships, valid graph structure, and cycle detection.

# Future Development

- V2: Student data and mastery tracking
- V3: Diagnostic engine
- V4: Research experiment
- V5: Analysis and final system
