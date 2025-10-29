#! /bin/bash
conda env create -f environment.yml
conda activate VariantCalling
pip install -e .