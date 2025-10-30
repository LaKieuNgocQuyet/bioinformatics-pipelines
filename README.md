# Overview
Pipeline for analyzing sequencing data
# Requirements
*   Unix-like operating system (cannot run on Windows)
*   Python >=3.10
# Install
### Method 1: Using [Docker](https://www.docker.com/) (recommended method)
If you haven't installed Docker , please install Docker Engine following the manufacture guideline document [here](https://docs.docker.com/engine/install/)
### Method 2: Build from source
If you haven't had git, please run the folowing command in the terminal
```bash
sudo apt-get update
sudo apt-get install git
```
Clone repository from github
```bash
git clone https://github.com/LaKieuNgocQuyet/variant_analysis_pipeline.git
```
Then install 
```bash
cd variant_analysis_pipeline
bash install.sh
```
# Prepare reference data
### Download reference genome 
Firstly, we should install wget for the next step by the folowing command
```bash
sudo apt-get update
sudo apt-get install wget
```
If you use GRCh37 human genome, run the folowing command in the terminal
```bash

```
# License
Licensed under the GPL-3.0. See the [LICENSE.txt](https://github.com/LaKieuNgocQuyet/variant_analysis_pipeline/blob/main/LICENSE) file.
# References
* Li, H. (2018). Minimap2: pairwise alignment for nucleotide sequences. Bioinformatics, 34:3094-3100. [doi:10.1093/bioinformatics/bty191](https://academic.oup.com/bioinformatics/article/34/18/3094/4994778?login=false)
* Li, H. (2021). New strategies to improve minimap2 alignment accuracy. Bioinformatics, 37:4572-4574. [doi:10.1093/bioinformatics/btab705](https://academic.oup.com/bioinformatics/article/37/23/4572/6384570?login=false)


