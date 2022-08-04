# DNA-sequencing
DNA Classifier:
The classifier portion of the project takes in data from humans, chimps, and dogs. The classifier
is trained on human DNA using k-mer counting and the Multinomial Naive Bayes classification algorithm.
The accuracy, precision, recall, and f1 statistics are outputted. 

DNA Sequence Gap Resolution:
Given k-mer strands of 6-letter length, we match our sequence of 5 letters + one unknown base with in-order
matching. This means that gcatgn will match with gcatga, gcatgc, gcatgg, gcatgt. We then count the occurrences
of each of the 4 bases to find which base occurs the most often, and is therefore the most likely to be the
missing base within the gap. We feed that information to the model, which then creates a prediction given a
6-letter strand with a missing base.

(Current limitation is resolving 1 missing base gaps, can be expanded but would require new models)

## Prerequisites
Some files within the data dir are too large, and therefore must be downloaded directly

GRCh38_latest_genomic.fna can be found under "Reference Genome Sequence" at NCBI, linked below

https://www.ncbi.nlm.nih.gov/genome/guide/human/

Test files are provided to demonstrate the functionality of the project

Set up the interpreter using Conda. Installation guide below

https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html


## Datasets used
* GRCh38_latest_genomic.fna - Human Genome Sequence (check prerequisites)
* GRCh38_genomic_test.fna - A subset (the initial sequence in GRCh38_latest_genomic.fna before artifacts)
 of the Human Genome Sequence without the ambiguous bases (N) for testing purposes


* GRCh38_latest_protein.faa - Human Protein Sequence
* GRCh38_protein_test.faa - A subset (first 200 protein entries from GRCh38_latest_protein.faa) 
 of the Human Protein Sequence for testing purposes


* orchid.fasta - Cypripedioideae, a subfamily of orchids for testing purposes

Text datasets with DNA for 3 species, used in the species DNA classifier
* human_data.txt
* chimp_data.txt
* dog_data.txt


## Machine Learning Model
Currently using Multinomial Naive Bayes, a variation of the Naive Bayes classifier.

## Sources/Research


### National Center for Biotechnology Information (NCBI)
NCBI: https://www.ncbi.nlm.nih.gov/
NCBI Human Genome Resources: https://www.ncbi.nlm.nih.gov/genome/guide/human/


### Closing gaps in the human genome using sequencing by synthesis
#### Authors: Manuel Garber, Michael C Zody, Harindra M Arachchi, Aaron Berlin, Sante Gnerre, Lisa M Green, Niall Lennon, and Chad Nusbaum

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2718494/

Garber M, Zody MC, Arachchi HM, Berlin A, Gnerre S, Green LM, Lennon N, Nusbaum C. Closing gaps in the human genome using sequencing by synthesis. Genome Biol. 2009;10(6):R60. doi: 10.1186/gb-2009-10-6-r60. Epub 2009 Jun 2. Erratum in: Genome Biol. 2011;12(4):403. PMID: 19490611; PMCID: PMC2718494.


### Filling the gaps
#### Author: Laura M. Zahn

https://www.science.org/doi/10.1126/science.abp8653

@article{
doi:10.1126/science.abp8653,
author = {Laura M. Zahn },
title = {Filling the gaps},
journal = {Science},
volume = {376},
number = {6588},
pages = {42-43},
year = {2022},
doi = {10.1126/science.abp8653},
URL = {https://www.science.org/doi/abs/10.1126/science.abp8653},
eprint = {https://www.science.org/doi/pdf/10.1126/science.abp8653}}


### Mechanisms of DNA damage, repair and mutagenesis
#### Authors: Nimrat Chatterjee Graham C. Walker

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5474181/

Chatterjee N, Walker GC. Mechanisms of DNA damage, repair, and mutagenesis. Environ Mol Mutagen. 2017 Jun;58(5):235-263. doi: 10.1002/em.22087. Epub 2017 May 9. PMID: 28485537; PMCID: PMC5474181.


### DNA Classification
#### Author: Nagesh Singh Chauhan

https://www.kaggle.com/code/nageshsingh/demystify-dna-sequencing-with-machine-learning/notebook

