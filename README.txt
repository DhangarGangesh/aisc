AISC EASY MIXED-PYTHON PRACTICAL CODES
======================================

Approach:
- Basic Python is used wherever it keeps the code shorter and clearer.
- NumPy is used for matrix/vector calculations where it simplifies the algorithm.
- No scikit-learn or prebuilt machine-learning models are used.

Files:
01 AI Agent - Vacuum Cleaner
02 BFS - Graph traversal
03 DFS - Graph traversal
04 BFS - Water Jug
05 Linear Regression
06 Polynomial Regression
07 Regression Tree - simple one-split demonstration
08 KNN Classification
09 K-Means Clustering
10 Single Layer Perceptron (SLP)
11 ADALINE
12 Backpropagation Neural Network
13 Hopfield Network
14 Bidirectional Associative Memory (BAM)
15 Fuzzy Logic - simple Mamdani-style demonstration
16 ANFIS - simplified Sugeno demonstration

Requirements:
- Python 3
- NumPy for files whose names include numpy, and for SLP/ADALINE/Backpropagation/Hopfield/BAM.
- BFS, DFS, Water Jug, AI Agent, KNN and Regression Tree use only Python's standard library.

Run a file:
    python filename.py

Important:
Some programs are deliberately small demonstrations for practical learning:
- Regression Tree is a one-split example, not a complete CART implementation.
- ANFIS uses fixed Gaussian premise parameters and least-squares consequent fitting; it is a simplified demonstration, not full hybrid-learning ANFIS.
- Fuzzy Logic is a compact Mamdani-style example; membership functions/rules can be adapted to your lab problem.

Additional Experiment 1 case study: run python3 31_smart_irrigation_five_agents.py
The 01_ai_agent_vacuum.py program demonstrates all five AI agent models.
