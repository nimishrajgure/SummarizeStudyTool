from fpdf import FPDF

def generate_pdf(text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Summary", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=text)
    pdf.output(output_path)
