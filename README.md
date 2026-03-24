# Certified Causal Foresight for Power System Operations

## Overview

This repository presents a complete theoretical and computational framework for **certifying power system operational safety under renewable uncertainty**.

Modern power grids operate under high variability due to renewable energy. Traditional tools can simulate or optimize system behavior, but they **do not provide statistical guarantees** that a sequence of decisions will remain safe over time.

This work introduces a **Certified Causal Foresight framework**, which enables:

- Finite-horizon safety certification
- Distribution-free statistical guarantees
- Decision validation under uncertainty with explicit confidence

---

## Core Problem

In real power systems:

- Decisions (dispatch, reserves) affect future system states
- Renewable uncertainty introduces stochastic disturbances
- A decision safe at one time step may cause violations later

The key question addressed:

> Can we certify, with statistical confidence, that a sequence of operational decisions will remain within safe limits over time?

---

## Key Contributions

### 1. Stochastic System Modeling

- Power system modeled as a **discrete-time stochastic dynamical system**
- State variables:
  - Voltage phase angles
  - Line flows
  - Reserve margins
- Disturbances:
  - Renewable injections (distribution-free, finite variance)

---

### 2. Finite-Horizon Viability Framework

- Defines a **safe set** based on operational constraints
- Introduces **cascading violation event**:
  - First time system leaves safe region
- Objective:
  - Bound probability of violation over finite horizon

---

### 3. Non-Asymptotic Statistical Certification

- Uses:
  - Monte Carlo simulation
  - Bernstein / Hoeffding concentration inequalities

- Certification condition:

\[
R(u) \le \hat{R}_N(u) + \text{confidence margin}
\]

- Properties:
  - Distribution-free
  - Finite-sample guarantee
  - No Gaussian assumption
  - No reliance on CLT

---

### 4. Sample Complexity Analysis

- Proven scaling:

\[
N = O\left(\frac{1}{\epsilon^2}\right)
\]

- Trade-off:
  - Higher accuracy → more samples
  - Higher confidence → more computation

---

### 5. Structural Risk Analysis

The framework proves:

- Monotonic increase of risk with load
- Continuity of risk surface
- Lipschitz robustness to parameter changes
- Sharp but continuous transition between safe and unsafe regions

---

### 6. DC–AC Consistency

- Shows DC approximation remains valid:
  - Under small-angle conditions
- Provides bounded error between:
  - DC-based certification
  - True AC system behavior

---

## Methodology

1. Define decision sequence \( u_{0:H-1} \)
2. Generate stochastic disturbances \( w_t \)
3. Simulate system evolution (DC power flow)
4. Detect constraint violations
5. Estimate violation probability
6. Apply concentration inequality
7. Certify decision based on confidence bound

---

## Algorithm (Operational Screening)

For each decision \( u \):

1. Generate \( N \) disturbance trajectories  
2. Compute empirical violation rate  
3. Compute upper confidence bound  
4. Accept decision if:

\[
U_N(u) \le \alpha
\]

This produces a **certified admissible decision set**.

---
## Repository Structure

```text
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
```
## Simulation Details

- Test System: IEEE 14 Bus
- Model: DC Power Flow
- Disturbances: Independent renewable injections
- Approach: Monte Carlo simulation

---

## Key Observations

- Certification boundary is nonlinear but continuous
- Risk increases monotonically with system load
- Sharp transition between safe and unsafe regions
- Computational cost scales linearly with sample size

---

## What This Work Is

- A **decision certification framework**
- A **statistical safety layer for power systems**
- A **theoretical + computational research contribution**

---

## What This Work Is NOT

- Not full AC dynamic simulation
- Not cascading failure modeling (protection systems)
- Not a replacement for optimal power flow

It is a **certification layer built on top of existing methods**

---

## Why This Matters

With increasing renewable penetration:

- Uncertainty is unavoidable
- Decisions have multi-step consequences
- Safety must be quantified probabilistically

This framework provides:

> **Provable guarantees on operational safety with explicit confidence**

---
Author :- Krishan Kant Pathak
Co-Author:- Subodh Kushwaha, Vivek Kesharwani, Utkarsh Gupta

University of Lucknow, India
Certified Causal Foresight for Power System Operations
Bharat Electricity Summit 2026
## Repository Structure
## How to Run

```bash
git clone https://github.com/your-username/certified_causal_foresight.git
cd certified_causal_foresight
pip install -r requirements.txt
python simulation/ieee14_case.py
Future Work
Full AC power flow integration
Correlated renewable models
Real-world grid data validation
Real-time certification systems
Integration with MPC and OPF


