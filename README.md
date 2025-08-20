# Invariants of Nested Hilbert Schemes

This repository contains a SageMath implementation of algorithms to verify conjectures from my research in enumerative algebraic, specifically concerning invariants of nested Hilbert schemes of points on the plane.

- **Paper 1:** [Defects, nested instantons and comet shaped quivers](https://arxiv.org/abs/1907.02771)
- **Paper 2:** [Flags of sheaves, quivers and symmetric polynomials](https://arxiv.org/abs/1911.12787)

## Overview

The core of this project is a computational test of a conjecture that relates a complex generating function over chains of partitions to coefficients of Macdonald polynomials. This serves as an example of using symbolic computation to explore and verify hypotheses in pure mathematics.

## How to Run

This code is built on **SageMath** and is not compatible with a standard Python interpreter.

### Setup and Installation

1. **Clone the Repository**
    
    ```bash
    git clone https://github.com/NadirFasola/nested-hilbert-invariants-polynomials.git](https://github.com/NadirFasola/nested-hilbert-invariants-polynomials.git)
    cd nested-hilbert-invariants-polynomials
    ```

1. **Create the conda environment**
    
    Ensure you have Conda or Mamba installed. Then, create the environment from the provided file:
    
    ```bash
    # Using Mamba (recommended, much faster)...
    mamba env create -f environment.yml

    # ...or using Conda
    conda env create -f environment.yml
    ```

1. **Activate the environment**
    
    ```bash
    conda activate nested-hilbert-env
    ```

1. **Register a Kernel with Jupyter**
    ```bash
    python -m ipykernel install --user --name=nested-hilbert-env --display-name="SageMath (nested-hilbert-env)"
    ```

1. **Install the Project Package**

    With the environment activated, install the 'nested-hilbert-invariants' package in editable mode using UV:

    ```bash
    uv pip install -e
    ```

1. **Launch JupyterLab**

    You can now run the example notebook:
    
    ```bash
    jupyter lab
    ```
    
    Navigate to `notebooks/example.ipynb`.

## Uninstall

To uninstall the package, proceed as follows:

1. **Activate the environment**
    First, you can uninstall the package from your Conda environment.
    ```bash
    conda activate nested-hilbert-env
    ```

1. **Uninstall the package**
    You can now remove the kernel you created.
    ```bash
    pip uninstall nested-hilbert-invariants
    ```

1. **Unregister the Jupyter kernel**
    ```bash
    jupyter kernelspec uninstall nested-hilbert-env
    ```

1. **Deactivate the environment and remove it**
    With package and kernel gone, you can safely remove the Conda environment itself.
    ```bash
    conda deactivate
    conda env remove -n nested-hilbert-env
    ```

1. **Remove the project folder**
    Finally, you can delete your project directory from your filesystem (be careful with these commands!).
    ```bash
    cd ..
    rm -rf nested-hilbert-invariants-polynomials
    ```

## License

This project is licensed under the [MIT License](LICENSE).
