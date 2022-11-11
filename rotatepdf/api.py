from ninja import Form, NinjaAPI, File, Schema
from ninja.files import UploadedFile
from PyPDF2 import PdfFileReader,PdfFileWriter
import os
api=NinjaAPI()

# class Inputfeild(Schema):
#     page: int
#     degree: int

# @api.post("/upload")
# def upload(request,details:Inputfeild = Form(...), file: UploadedFile = File(...)):
#     target_file=file.name
#     output_file=open('final.pdf','wb')
#     pdf= PdfFileReader(target_file)
#     writer=PdfFileWriter()
#     page= pdf.getPage(details.page)
#     page.rotateClockwise(details.degree) 
#     writer.addPage(page)
#     writer.write(output_file)
#     output_file.close()
#     # rotatepdf/pdf_rotation/rotatepdf/1.pdf
# # mimetype

#     return {'input':pdf}   





class Inputfeild(Schema):
  page: int
  degree: int

@api.post("/rotate_pdf")
def rotate_pdf(request,details:Inputfeild = Form(...), file: UploadedFile = File(...)):
  pdf = PdfFileReader(file)
  writer = PdfFileWriter()
  page = pdf.getPage(details.page)
  page.rotateClockwise(details.degree)
  writer.addPage(page)
  output_file = open('final.pdf', 'wb')
  writer.write(output_file)
  path = os.path.realpath(output_file.name)
  output_file.close()
  return {'response':'pdf rotation successful',"path": path} 