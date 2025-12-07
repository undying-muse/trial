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
> DNA uses both strands for mRNA transcription. Same gene is not coded in the same place. Different genes are coded in different parts of the DNA, and can be on either strand.

     #I just found out that I can add code here, nice.
     print("hello world")

- The mRNA is transcribed normally.
- If the mRNA contains useless regions with no protein coding.
- The mRNA goes through splicing to remove the introns.
- Mature mRNA codes proteins

> Another Homework question: The intronic slices of the mRNA gets thrown out of the sequence as the mRNA matures.   
> What happens to the intronic regions?
> Introns are removed from precursor mRNA (pre-mRNA) by the spliceosome and follow several defined fates depending on organism, intron type, and cellular context. Key outcomes:
> Immediate degradation
> - Most excised introns are rapidly degraded by cellular exonucleases:
> In the nucleus, debranching enzyme DBR1 (in yeasts and metazoans) cleaves the 2′–5′ phosphodiester bond at the lariat branchpoint,
> converting the lariat to a linear RNA that 5′→3′ and 3′→5′ exonucleases (e.g., XRN family, the exosome) degrade.
Rapid turnover prevents accumulation of intronic RNA and recycles nucleotides.
Circular intronic RNAs (stable lariats/ciRNAs)
> - Some intron lariats escape debranching and remain circular (ciRNAs). Features:
Resistance to exonucleases because they lack free ends.
Can be relatively stable in the nucleus and modulate transcription of their parent genes by interacting with RNA polymerase II or splicing factors.
Observed in metazoans; formation depends on specific sequence motifs near the branchpoint and splice sites.
Exon-derived circular RNAs via back-splicing (circRNAs) and intron retention contributing to circRNA biogenesis
> - Intronic sequences can promote back-splicing between exons, producing exon-containing circRNAs; intronic complementary sequences or inverted repeats (e.g., Alu elements in humans) often mediate this.
> - Some circRNAs retain intronic fragments (exon–intron circRNAs, EIciRNAs) and act in transcriptional regulation.
Functional noncoding RNAs processed from introns
> - Many introns contain functional RNAs that are processed into stable small RNAs:
Small nucleolar RNAs (snoRNAs) and small Cajal body RNAs (scaRNAs) are commonly encoded within introns; after splicing and debranching, host intron fragments are trimmed to mature sno/scaRNAs.
Some microRNAs (miRNAs) are produced from intronic regions (mirtrons): the splicing and debranching pathway can bypass Drosha cleavage, with the debranched intron folded and processed by Dicer to yield miRNAs.
Other regulatory RNAs (piRNAs in some organisms) can originate from intronic sequences.
Nuclear retention and regulatory roles
> - Some excised introns or partially processed intron-containing RNAs are retained in the nucleus and serve regulatory functions:
Modulate splicing decisions, nucleate nuclear bodies, or influence chromatin states.
Intron retention in pre-mRNA can create transcripts targeted for nonsense-mediated decay or store transcripts for later processing.
Export and cytoplasmic roles
> - Rarely, intron-derived RNAs are exported and act in the cytoplasm: functioning as regulatory RNAs, competing endogenous RNAs, or contributing to viral mimicry and immune signaling in particular contexts.
Evolutionary and genomic consequences
> - Excised introns can serve as raw material for new genes, regulatory elements, or mobile elements; intronic sequences contribute to exon shuffling and regulatory motif evolution.
Summary flow after splicing

> Spliceosome releases intron lariat.
> Debranching (DBR1) converts lariat → linear intron (often).
> Linear intron is degraded by exonucleases, or
> Intron is processed into stable products (snoRNAs, mirtrons, ciRNAs), or
> Lariat persists as a circular intronic RNA with regulatory roles, or
> Intronic sequences facilitate circRNA production or other regulatory outcomes.
> Collectively, introns are not passive waste: most are degraded quickly, but a significant subset is repurposed into stable RNAs or regulatory elements that impact gene expression and genome evolution. (Information reflects literature through May 2024.)

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





