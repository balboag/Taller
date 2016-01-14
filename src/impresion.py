# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os
import time

from conexion import bd
from fpdf import FPDF

def imprimir(fac,mat,dni):
    pdf = FPDF()
    pdf.add_page()
    header(pdf,fac,mat,dni)
    body(pdf,fac)
    pdf.output('prueba.pdf','F')
    os.system('/usr/bin/evince prueba.pdf')
 
def header(pdf,fac,mat,dni):
    pdf.set_font('Arial','B',12)
    pdf.cell(60,10,'TALLERAUTO',0,1,'C')
    pdf.set_font('Arial','',10)
    pdf.cell(60,10,'Calle Senra, 12  Marin (Pontevedra)',0,1,'L')
    pdf.cell(60,10,'36911 Tlfo: 986 882 211-656 565 918',0,1,'L')
    pdf.image('car.png',170,10,25,25,'png','')
    pdf.line(5,40,200,40)
    pdf.set_font('Times','B',12)
    pdf.cell(180,10,'Factura numero: %s ' % fac,0,1,'R')
    pdf.cell(60,10,'DATOS CLIENTE:',0,1,'L')
    cursor = bd.cursor()
    cursor.execute(""" SELECT dnicli, apelcli, nomcli, dircli, poblic, procli, cpcli FROM clientes WHERE dnicli=?""", (dni,))
    datos = cursor.fetchall()
    for fila in datos:
        pdf.cell(30,10,'%s' % fila[1],0,0,'L')
        pdf.cell(30,10,'%s' % fila[2],0,1,'L')
        pdf.cell(20,10,'%s' % fila[3],0,0,'L')
        pdf.cell(50,10,'%s' % fila[4],0,0,'R')
        pdf.cell(90,10,'Matricula Vehiculo: %s' %mat,0,1,'R')
        pdf.cell(30,10,'%s' % fila[6],0,0,'L')
        pdf.cell(60,10,'%s' % fila[5],0,1,'L')
    pdf.line(5,90,200,90)

def body(pdf, fac):  
    pdf.set_font('Times','B',12)
    pdf.cell(180,10,'Fecha factura: ' + time.strftime('%d %b %y'),0,1,'R')
    pdf.cell(120,10,'DATOS FACTURA:',0,1,'L')
    pdf.cell(60,10,'ID',1,0,'L')
    pdf.cell(60,10,'Concepto',1,0,'C')
    pdf.cell(60,10,'Precio unidad',1,1,'R')

    cursor = bd.cursor()
    cursor.execute(""" SELECT idv, idfac, conceptov, preciov FROM ventas WHERE idfac=?""", (fac,))
    datos = cursor.fetchall()
    suma = 0
    for fila in datos:
        pdf.cell(60,10,'%s' % fila[0],1,0,'L')
        pdf.cell(60,10,'%s' % fila[2],1,0,'C')
        pdf.cell(60,10,'%s' % fila[3],1,1,'R')
        suma = suma + int(fila[3])
        
    pdf.cell(60,10,'',0,1,'C')  
    pdf.cell(180,10,'IVA: 21%',0,1,'R')
    pdf.cell(180,10,'Total sin IVA: ' + str(suma) + ' E',0,1,'R')
    pdf.cell(180,10,'Total con IVA: ' + str(suma+(suma*0.21)) + ' E',0,1,'R')

