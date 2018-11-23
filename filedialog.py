from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

file=askopenfilename()

if(file!=None):
    infile=open(file,"r")

for line in infile.readlines():
    line=line.strip()
    print(line)

infile.close()

file=asksaveasfilename()

if(file!=None):
    infile=open(file,"a")

infile.write("안녕하세요")

infile.close()


    
