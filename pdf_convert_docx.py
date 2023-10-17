from pdf2docx import Converter

pdf_file = 'C:\Users\PC\Downloads\\Q.pdf'
docx_file = 'D:\\OneDrive\\Desktop\\output.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
