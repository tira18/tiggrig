import os
import sys
import pikepdf
import time

varo = input("Please input PDF file name:")
#path = os.path.dirname(os.path.abspath(__file__))
path = os.getcwd()
#print(path)
pdf = pikepdf.open(path+'\\'+varo)
pdf.save(path+'\patrast.pdf')
print("Patrasta")
time.sleep(20)    
