# Invariants of Nested Hilbert Schemes

This repository contains a SageMath implementation of algorithms to verify conjectures from my research in enumerative algebraic, specifically concerning invariants of nested Hilbert schemes of points on the plane.

- **Paper 1:** [Defects, nested instantons and comet shaped quivers](https://arxiv.org/abs/1907.02771)
- **Paper 2:** [Flags of sheaves, quivers and symmetric polynomials](https://arxiv.org/abs/1911.12787)

## Overview

The core of this project is a computational test of a conjecture that relates a complex generating function over chains of partitions to coefficients of Macdonald polynomials. This serves as an example of using symbolic computation to explore and verify hypotheses in pure mathematics.

## How to Run

This code is built on **SageMath** and is not compatible with a standard Python interpreter.

1.  **Install SageMath:** Follow the installation instructions at [sagemath.org](https://www.sagemath.org/). Using SageMath within a conda environment is often a good approach.

2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/NadirFasola/nested-hilbert-invariants-polynomials.git](hhttps://github.com/NadirFasola/nested-hilbert-invariants-polynomials.git)
    cd nested-hilbert-invariants
    ```

3.  **Launch the Jupyter Notebook in Sage:**
    From your terminal, run:
    ```bash
    sage -n jupyter
    ```
    This will open a Jupyter interface in your browser. Navigate to `notebooks/demonstration.ipynb` to run the examples.

## License

This project is licensed under the [MIT License](LICENSE).
