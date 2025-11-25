#We are trying to learn about 
fastqc reads_1.fq reads_2.fq

bowtie2-build toyvirus_1kb.fa toyvirus_1kb.index
#Align the reads to the reference genome using bowtie2 
bowtie2 \
  -x toyvirus_1kb.index \
  -1 reads_1.fq \
  -2 reads_2.fq \
  -S virus.align.sam 
# Output files are sam files
"""Output turned out to be
500 reads; of these
  500 (100%.00) were paired; of these:
    0 (0.00%) aligned concordantly 0 times
    0 (0.00%) aligned concordantly exactly 1 time
    500 (100.00%) aligned concordantly >1 times
    ----
    0 pairs aligned concordantly 0 times; of these:
      0 (0.00%) aligned discordantly 1 time
    ----
    0 paired aligned 0 times concordantly or discordantly; of these 
      0 mates make up pairs; of these:
        0 (0.00%) aligned 0 times
        0 (0.00%) exactly 1 time
        0 (0.00%) >1 times
100.00% overall alignment rate """"


# Change this document to such a way that you can use any document to execute this code.
