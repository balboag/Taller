# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os

from conexion import bd
from fpdf import FPDF

def imprimir(fac,mat,dni):
    pdf = FPDF()
    pdf.add_page()
    header(pdf)
    pdf.output('prueba.pdf','F')
    os.system('/usr/bin/evince prueba.pdf')
    
        
def header(pdf):
    pdf.set_font('Arial','B',12)
    pdf.cell(80)
    pdf.cell(30,10,'TALLERAUTO',1,0,'C')
    pdf.set_font('Arial','',10)
    pdf.cell(30,25,'Calle Senra, 12',1,0,'C')
    pdf.ln(20)
    
    
