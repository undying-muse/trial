# Bioinformatics notes

### RNA Types:
mRNA:    Messenger RNA, encodes proteins.  
tRNA:    Acts as adaptor between mRNA and amino acids. Transporter RNA, transports amino acids.  
rRNA:    Forms the ribosome.  
snRNA:   Functions in various nuclear processes. (example: splicing)  
snoRNA:  Facilitates the chemical modification of RNAs.    
miRNA:   Regulates gene expression.  
siRNA:   Silences gene expression.  
lncRNA:  Regulates gene expression.  

> New RNA type? Glyco-RNA  
Like Glycoprotein, Glycolipid etc., there are glycoRNAs 

## Discovery Analysis:

### mRNa Transcription unit:
> The DNA has a double helix structure.  
> Homework question: Does the cell use both strands or one single strand for mRNA transcription?

     #I just found out that I can add code here, nice.
     print("hello world")

- The mRNA is transcribed normally.
- If the mRNA contains useless regions with no protein coding.
- The mRNA goes through splicing to remove the introns.
- Mature mRNA codes proteins

> Another Homework question: The intronic slices of the mRNA gets thrown out of the sequence as the mRNA matures.   
> What happens to the intronic regions?

There are more proteins than there are genes in the cells.    
This is possible by alternative splicing[^1] of the mRNA. 

mRNA can...
- remove each intron,
- remove some exons as well as introns,
- remove part of exons,
- keep some introns,
- mutually exclude some exons etc.

Our goal is to determine transcriptional activities of every
single gene in the cell/tissue.
For this main steps are
1) Tissue collection,
2) Total RNA extraction and isolation,
3) cDNA preparation,
4) Quantification,
5) Comparative analysis 


QPCR (Quantitative PCR)
Transcriptome: 




Coding session:

     #!/bin/bash
     source /usr/local/anaconda3/etc/profile.d/conda.sh

     Fastq='SRR9641842.fastq'
     Reference='Bowtie2Index/NC_009334.fa'
     VirusName='EBV'

     conda activate bfblab
     #run fastqc
     fastqc $Fastq

     #uncompress fastq.gz file if needed
     if [[ -f ${Fastq}.gz ]]; then
         echo "Uncompressing ${Fastq}.gz file"
         gunzip ${Fastq}.gz
     fi

     #check if bowtie2 samtools bcftools and fastqc are available in the conda environment
     command -v bowtie2 >/dev/null 2>&1 || { echo >&2 "bowtie2 not found in PATH. Aborting."; exit 1; }
     command -v samtools >/dev/null 2>&1 || { echo >&2 "samtools not found in PATH. Aborting."; exit 1; }
     command -v bcftools >/dev/null 2>&1 || { echo >&2 "bcftools not found in PATH. Aborting."; exit 1; }
     command -v fastqc >/dev/null 2>&1 || { echo >&2 "fastqc not found in PATH. Aborting."; exit 1; }

     # Index already built for EBV reference genome
     # Align reads to reference genome
     bowtie2 -x ${Reference%.fa} -U $Fastq -S ${VirusName}.alignment.sam

     # Convert sam to bam
     samtools view -b ${VirusName}.alignment.sam > ${VirusName}.alignment.bam
     #sort the bam file
     samtools sort ${VirusName}.alignment.bam -o ${VirusName}.alignment.sorted.bam
     #index the sorted bam file
     samtools index ${VirusName}.alignment.sorted.bam

     #count number of reads aligned
     samtools view -c -F 4 ${VirusName}.alignment.sorted.bam

     #Visualize in IGV

     #Run bcfools to call variants
     bcftools mpileup -f Bowtie2Index/NC_009334.fa \
     ${VirusName}.alignment.sorted.bam | \
     bcftools call -mv -Ov -o ${VirusName}.variants.vcf

     #Summarize variants
     bcftools stats ${VirusName}.variants.vcf > ${VirusName}.variant.stats

     conda deactivate



Go to the file containing this and the files to be compared using the **cd** command


[^1]: Splicing: is the mRNA maturation by cutting the introns out of the mRNA





