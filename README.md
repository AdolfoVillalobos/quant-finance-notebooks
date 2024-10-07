# Quant Finance Notebooks

This repository contains a collection of Jupyter notebooks focused on quantitative finance topics. The notebooks cover various aspects of financial analysis, statistics, and modeling using Python.

## Contents

1. Distributions and Random Variables
2. Moments and Statistics
3. Normality Tests
4. Covariance
4. Correlation
5. Cross-correlation

## Setup

This project uses PDM for dependency management. To set up the environment:

1. Install PDM if you haven't already: `pip install pdm`
2. Clone this repository
3. Run `pdm install` in the project root to install dependencies

## Data

The notebooks use cryptocurrency OHLCV (Open, High, Low, Close, Volume) data from Binance. A setup script is provided to fetch this data:

```bash
pdm run python -m setup
```

This script will download the data and save it in the `data` directory.

## Running the Notebooks

To run a notebook, use the following command:

```bash
pdm run jupyter notebook <notebook-name>.ipynb
```

Replace `<notebook-name>` with the name of the notebook you want to run.

