# Bioinformatics_notes_2
> Slides are not mine. Only the notes are my doing.


RNAseq library preparation tricks
95% of RNA in the transcriptome comes from ribosomal RNA
- Cytoplasmic rRNAs (5S rRNA, 5.8S rRNA, 18S rRNA and 28S rRNA)
- Mitochondrial rRNAs (12S rRNA and 16S rRNA)

Poly-A Transcrips: 
- mRNA
- immature miRNA
- snoRNA

Poly-A Transcrips + Other mRNA's: 
- tRNA
- mature miRNA
- piRNA

RNA seq library prep:
- Fragment the RNA

## Isoforms:

With RNAseq date isoform specific expression differences can be detected

Filter out the genes with <1.0 FPKM

Sample Metadata:

| Sample | strain | date | cage | treatment | replicate | sex |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| B1 | BALB/cJ | 20180515 | 1 | yes | 1 | M | 
| B2 | C57BL/6J | 20180515 | 2 | yes | 1 | M |
| B3 | BALB/cJ | 20180515 | 3 | no | 1 | M |
| B4 | C57BL/6J | 20180515 | 1 | no | 1 | F |
| B5 | BALB/cJ | 20180515 | 2 | yes | 2 | F |
| B6 | C57BL/6J | 20180515 | 3 | yes | 2 | M |
| B7 | BALB/cJ | 20180515 | 1 | no | 2 | M |
| B8 | C57BL/6J | 20180515 | 2 | no | 2 | M |
| B9 | BALB/cJ | 20180515 | 3 | yes | 3 | F |
| B10 | C57BL/6J | 20180307 | 1 | yes | 3 | F |
| B11 | BALB/cJ | 201805307 | 2 | no | 3 | M |
| B12 | C57BL/6J | 201805307 | 3 | no | 3 | M |

^Source: https://hbctraining.github.io/


| ---- | Patient sick | Patient healthy | 
| :---: | :---: | :---: | 
| signal positive | :---: | :---: | 




























































