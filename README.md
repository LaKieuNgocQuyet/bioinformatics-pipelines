# Overview
Pipeline for analyzing sequencing data
# Requirements
*   Unix-like operating system (cannot run on Windows)
*   Python >=3.10
# Install
### Using [Docker](https://www.docker.com/)
If you haven't installed Docker, please run the folowing command in the terminal
```
sudo apt-get update
```
### Build from source
If you haven't had git, please run the folowing command in the terminal
```
sudo apt-get update
sudo apt-get install git
```
Clone repository from github
```
git clone https://github.com/LaKieuNgocQuyet/variant_analysis_pipeline.git
```
Build and active conda vitrual environment
```
cd variant_analysis_pipeline
conda env create -f environment.yml
conda activate VariantCalling
```
Install site-packages
```
pip install -e .
```
# Prepare reference data
### Download reference genome 
Firstly, we should install wget for the next step by the folowing command
```
sudo apt-get update
sudo apt-get install wget
```
If you use GRCh37 human genome, run the folowing command in the terminal
```

```
# License
Licensed under the GPL-3.0. See the LICENSE.txt file.
# References
