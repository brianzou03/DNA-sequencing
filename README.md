# DNA-sequencing
(project synopsis here)

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

Text datasets with DNA for 3 species, used in the species classifier
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


### Filling the gaps
#### Author: Laura M. Zahn

https://www.science.org/doi/10.1126/science.abp8653


### Mechanisms of DNA damage, repair and mutagenesis
#### Authors: Nimrat Chatterjee Graham C. Walker

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5474181/


### Human DNA Repair Genes
#### Author: John Sgouros

https://d1wqtxts1xzle7.cloudfront.net/35295893/1284-with-cover-page-v2.pdf?Expires=1658702441&Signature=dQjl~kjMrgJrwmF1vcr2uFPZdkmy9Qj31hdKXivadJpVkKyrlU41tcFnH81XMYFLuKitGkRBg2O1Mw-6FcJUJzMFx9BI7a75zzrEo~cElbfRZ0Aori4aK2ygintricxETBM4m2eNTQkbPsAMHv7UjpIbX74KpJdDU4P6RGb05RAXwJajsAy9N7Z6BY3nOv2CXKtFo61zHNNtwzZtAiKyfA8m05eY3yrSKpHlt2xl~4x4ouhmjvf3xn47QG80qj1AKlYu5Se0c-G~01816yOpAlFTEE4qGdfA4NVbBzxcM4Z4BXnPtBaE57lMLDUqtT7Avu12CTWlbxGo6OCkPbSgMQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA