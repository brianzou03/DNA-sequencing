# DNA-sequencing
DNA Classifier:
The classifier portion of the project takes in data from humans, chimps, and dogs. The classifier
is trained on human DNA using k-mer counting and the Multinomial Naive Bayes classification algorithm.
The accuracy, precision, recall, and f1 statistics are outputted. 

DNA Sequence Gap Resolution:
(DNA gap prediction Synposis here)
(Current limitation is resolving 1 missing base gaps, can be expanded but would require new models)

## Prerequisites
Some files within the data dir are too large, and therefore must be downloaded directly

GRCh38_latest_genomic.fna can be found under "Reference Genome Sequence" at NCBI, linked below

https://www.ncbi.nlm.nih.gov/genome/guide/human/

Test files are provided to demonstrate the functionality of the project



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


## FASTA File Extensions 

* fasta, fa	generic FASTA	Any generic fasta file. See below for other common FASTA file extensions
* fna - FASTA nucleic acid	(Used generically to specify nucleic acids.)
* ffn - FASTA nucleotide of gene regions (Contains coding regions for a genome.)
* faa - FASTA amino acid (Contains amino acid sequences. A multiple protein fasta file can have the more specific extension mpfa.)
* frn - FASTA non-coding RNA (Contains non-coding RNA regions for a genome, in DNA alphabet e.g. tRNA, rRNA)


## DNA Bases + 1 letter code
* Adenine (A) : pairs with Thymine (T)
* Cytosine (C) : pairs with Guanine (G)
* Guanine (G)
* Thymine (T)

## Protein amino acids + 3 letter code + 1 letter code

* alanine - ala - (A)
* arginine - arg - (R)
* asparagine - asn - (N)
* aspartic acid - asp - (D)
* cysteine - cys - (C)
* glutamine - gln - (Q)
* glutamic acid - glu - (E)
* glycine - gly - (G)
* histidine - his - (H) 
* isoleucine - ile - (I)
* leucine - leu - (L)
* lysine - lys - (K)
* methionine - met - (M)
* phenylalanine - phe - (F)
* proline - pro - (P)
* serine - ser - (S)
* threonine - thr - (T)
* tryptophan - trp - (W)
* tyrosine - tyr - (Y)
* valine - val - (V)


## DNA Encoding Approaches
1. **Ordinal encoding DNA sequence data**
We need to encode each nitrogen base as an ordinal value. 
“ATGC” becomes [0.25, 0.5, 0.75, 1.0]. Ambiguous bases become 0.


2. **One-hot encoding DNA Sequence**
One-hot encoding is often used in deep learning methods and works with CNN. 
“ATGC” becomes [0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]. 
One-hot encoded vectors can be concatenated or transformed into matrices


3. **k-mer counting (DNA sequences as a "language")**
The problem with ordinal and one-hot is that the results are not uniform length, necessary for classification
and regression. With k-mer counting we take a sequence and break it down into k-mer length "words". 
We determine the length of the words - for example "words" of length 5 (hexamers), 
“ATGCATGCA” becomes: 'ATGCA', 'TGCAT', ‘GCATG’, 'CATGC', 'ATGCA' . 
This forms 5 hexamer words, with 5 (letters) ^ 5 (length) = 3125 potential words 


## Machine Learning Model
(ML Model here)


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

