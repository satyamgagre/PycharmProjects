import PyPDF2

pdFiles = ['1.pdf', '22.pdf', '3.pdf']
merger = PyPDF2.PdfMerger()

for filename in pdFiles:
    with open(filename, 'rb') as pdFiles:
        merger.append(pdFiles)

merger.write('merged.pdf')
merger.close()