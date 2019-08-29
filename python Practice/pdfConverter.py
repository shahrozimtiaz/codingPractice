from fpdf import FPDF

pdf = FPDF()
# imagelist is the list with all image filenames
imagelist = ['IMG-0113.JPG','IMG-0114.JPG']
for image in imagelist:
    pdf.add_page()
    pdf.image(image,w=150,h=200)
    pdf.rotate(angle=180)
pdf.output("newPDF.pdf", "F")