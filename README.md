# certified_causal_foresight
Certified Causal Foresight for Power System Operations
Overview

This repository contains the full theoretical and computational implementation of a finite-horizon stochastic certification framework for power system operations under renewable uncertainty.

The project addresses a fundamental limitation in modern grid operation:

Existing tools can simulate or optimize — but cannot certify with statistical confidence that a decision will remain safe over time.

This work introduces a non-asymptotic, distribution-free certification layer that provides finite-sample guarantees on operational safety.

Core Idea (In One Line)

Instead of asking
“Is this decision feasible now?”

we ask
“Can we certify, with statistical confidence, that this decision remains safe over time under uncertainty?”

Research Contributions
1. Reformulation of Power System Operation
Power grid modeled as a discrete-time stochastic dynamical system
States:
Phase angles
Line flows
Reserve margins
Inputs:
Dispatch decisions
Reserve allocations
Disturbances:
Renewable injections (distribution-free)
2. Stochastic Viability Certification
Introduces finite-horizon stochastic viability
Defines:
Safe set (constraints)
Cascading violation event
Objective:
Bound probability of leaving safe region
3. Non-Asymptotic Statistical Guarantees
Uses:
Monte Carlo estimation
Bernstein / Hoeffding inequalities
Produces:
𝑅
(
𝑢
)
≤
𝑅
^
𝑁
(
𝑢
)
+
confidence margin
R(u)≤
R
^
N
	​

(u)+confidence margin
Guarantees:
Distribution-free
Finite sample
No CLT assumption
4. Sample Complexity Characterization
Proven:
𝑁
=
𝑂
(
1
𝜖
2
)
N=O(
ϵ
2
1
	​

)
Tradeoff:
Accuracy vs computation
Confidence vs sample size
5. Structural Risk Analysis

The work rigorously proves:

Monotonicity of risk with load
Continuity of risk surface
Lipschitz robustness
Phase transition behavior (low-risk → high-risk)
6. AC–DC Consistency Result
Shows:
DC approximation is locally valid
Error bounded in small-angle regime
Repository Structure
certified_causal_foresight/
│
├── README.md
├── paper/
│   └── full_paper.pdf
│
├── theory/
│   ├── stochastic_model.md
│   ├── certification_derivation.md
│   ├── concentration_bounds.md
│   └── risk_analysis.md
│
├── simulation/
│   ├── ieee14_case.py
│   ├── dc_power_flow.py
│   ├── monte_carlo_engine.py
│   ├── certification.py
│   └── utils.py
│
├── experiments/
│   ├── risk_surface.py
│   ├── parameter_sweep.py
│   └── results/
│       ├── plots/
│       └── data/
│
├── outputs/
│   ├── figures/
│   ├── logs/
│   └── tables/
│
└── docs/
    ├── methodology.md
    ├── assumptions.md
    └── limitations.md
Methodology Pipeline
Define decision sequence 
𝑢
0
:
𝐻
−
1
u
0:H−1
	​

Generate stochastic disturbances 
𝑤
𝑡
w
t
	​

Simulate system evolution using DC power flow
Detect constraint violations
Estimate violation probability
Apply concentration inequality
Certify or reject decision
Algorithm (Operational Screening)

For each decision:

Generate 
𝑁
N disturbance trajectories
Compute empirical violation rate
Compute confidence bound
Accept if:
Upper Bound
≤
𝛼
Upper Bound≤α

This produces a certified admissible decision set

Simulation Details
Test system: IEEE 14 Bus
Disturbances:
Independent renewable injections
Observations:
Nonlinear certification boundary
Sharp risk transition
Linear computational scaling
Key Results
Certification boundary is nonlinear but continuous
Risk increases monotonically with load
Confidence bounds tighten with sample size
Computational cost scales linearly with samples
What This Work Is (Be Precise)

This is:

A decision certification framework
A statistical safety layer
A theoretical + computational hybrid model
What This Work Is NOT
Not full AC dynamic simulation
Not cascading failure modeling (protection systems)
Not a replacement for OPF

It is a certification layer on top of existing tools

Why This Matters

Modern grids:

High renewable penetration
High uncertainty
Multi-step decision impact

Operators currently lack:

Quantified risk guarantees
Confidence-based decision validation

This work provides:

Mathematically provable operational safety guarantees

How to Run
git clone https://github.com/your-username/certified_causal_foresight.git
cd certified_causal_foresight
pip install -r requirements.txt
python simulation/ieee14_case.py
Example Output
Risk vs Load plots
Certification boundary curves
Monte Carlo convergence graphs
Future Extensions
Full AC power flow integration
Correlated renewable disturbances
Real grid datasets
Real-time certification
Integration with MPC / OPF
Authors
Krishan Kant Pathak
Subodh Kushwaha
Vivek Kesharwani
Utkarsh Gupta

University of Lucknow, India

Citation

If you use this work:

Certified Causal Foresight for Power System Operations
Bharat Electricity Summit 2026
Final Note

This repository represents:

Full theoretical derivation
Mathematical rigor
Practical simulation
Original research framing

It is not just code — it is a complete research system.
