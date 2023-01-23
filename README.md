# CoronaAssembly

## Introduction

In order to combat COVID-19 worldwide, we have developed the ```CoronaAssembly pipeline```, which is based on the ```artic pipeline```, allowing you to do genomic assembly of data from ```Oxford Nanopore technology``` (ONT).


## Prerequisite:

You must first install the following packages to use this pipeline:

* Anaconda

https://docs.anaconda.com/anaconda/install/ 

* Artic pipeline

https://artic.readthedocs.io/en/latest/installation/ 

## Installation

This pipeline can be used directly on the terminal. To do this, you must first download it using the following code:
```
git clone https://github.com/KhadimGueyeKGY/CoronaAssembly.git
```

## Input 
This workflow uses the ```fastq_pass``` received after sequencing, along with a file containing a ```list of sample IDs``` in barcode order.

* Note that the IDs file must be in the same directory as the fastq_pass and must have two columns separated by commas. The IDs are in the first column, while the collection year is in the second.
#### Example:
```
cd CoronaAssembly 
nano ./data/id.txt
```

## Usage:
To know how to use it, just type 
```
python CoronaAssembly.py
```
#### Output 
* 1) conda activate artic  
* 2)	python CoronaAssembly.py -i input/file/fastq_pass/ -n ID.txt -c country  

1) First, you need to activate the artic environment by typing
```
conda activate artic
```
2) Then run the program.

#### Example
```
python CoronaAssembly.py –i ./data/fastq_pass/ -n id.txt –c Senegal
```

## Output
After assembly, the pipeline generates an ```output folder``` in the same folder as the fastq_pass. It contains two other folders. The first one ```final_consensus``` contains all consensus fasta formats of each sample which are concatenated into a file named ```final_consensus.fasta```. The second ```final_consensus_for_GISAID``` contains all the consensus fasta formats but with the header modified and concatenated into a file named ```final_consensus.fasta``` which is required for submission on GISAID. 

