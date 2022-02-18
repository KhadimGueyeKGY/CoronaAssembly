#!/usr/bin/python

#This pipeline has been set up to facilitate the genomic assembly of SARS-COV-2 data from the Oxford nanoport platforme.
#source : https://artic.readthedocs.io/en/latest/tests/?badge=latest
#auteur : kgy

import os
import sys


s = sys.argv
if len(s) < 7:
	print("Autor : KhadimGueyeKGY \n\nUsage:\n\n1) conda activate artic  \n2) python CoronaAssembly.py -i input/file/fastq_pass/ -n ID.txt -c country\n\n")
	sys.exit()

#-----------------------------------Genome Assembly

os.system("mkdir -p "+s[2]+"/../output/final_consensus")

a = os.popen("cd "+s[2]+" ; ls ").read().split("\n")
print ("Number of process : "+str(len(a)-1))

for i in range(len(a)) : 
	if a[i]=="":
		break
	c= s[2]+"/../output"+"/"+a[i]+"/"
	b = s[2]+"/"+a[i]+"/"
	os.system("mkdir -p "+c)
	print("Assembly of "+a[i]+" : "+str(i+1)+"/"+str(len(a)-1)+"\n")
	os.system("artic guppyplex --min-length 350 --max-length 700 --prefix "+a[i]+" --directory "+b+" --output "+c+"/"+a[i]+"_guppyplex_fastq_pass.fastq")
	os.system("artic minion --normalise 200  --threads 34 --scheme-directory primer-schemes --read-file "+c+"/"+a[i]+"_guppyplex_fastq_pass.fastq --medaka nCoV-2019/V3/ --medaka-model r941_min_high_g351 "+c)
	print ("\n\nDONE ...\n\n\n\n")
	os.system("cd "+c + " ; mv .consensus.fasta ../final_consensus/"+a[i]+"_consensus.fasta")
	os.system("cd "+s[2]+"/../output/"+"/ ; rm -r "+a[i]+"/")


#-------------------------------Rename header

os.system("mkdir -p "+s[2]+"/../output/final_consensus_for_GISAID")

id = open(s[2]+"/../"+s[4],"r").read().split("\n")
del id[0]
input = os.popen("cd "+s[2]+"/../output/final_consensus/ ; ls").read().split("\n")

for i in range(len(input)):
	if input[i]=="":
		pass
	else:
		t = str(i+1)
		if i < 9 :
			t= "0"+str(i+1)
		int= open(s[2]+"/../output/final_consensus/"+input[i],"r").read().split("\n")
		out = open(s[2]+"/../output/final_consensus_for_GISAID/"+t+"_"+id[i].split(",")[0]+".fasta","w")
		for j in range(len(int)):
			if int[j]=="":
				break
			if int[j].find(">") != -1 :
				id_l = id[i].split(",")
				out.write(">hCoV-19/"+s[6]+"/"+id_l[0]+"/"+id_l[1]+"\n")
			else :
				out.write(int[j]+"\n")


os.system("cd "+s[2]+"/../output/final_consensus_for_GISAID/ ; cat *fasta > final_consensus.fasta")
os.system("cd "+s[2] + "/../output/final_consensus/ ; cat * > final_consensus.fasta")




