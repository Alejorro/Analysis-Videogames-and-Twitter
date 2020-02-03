

def generate_pdf():

    import os
    import pdfkit

    options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
    }

    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(current_dir, "../Outputs/queryToPDF.html")


    pdfkit.from_file(filename,'Outputs/testcsv.pdf', options=options)

    os.remove(filename)
