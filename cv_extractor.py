import pdfplumber
from docx import Document
import re
from unidecode import unidecode


class CV_Extrctor:

    def extract_text_from_pdf(self, pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages)

        return text

    def extract_text_from_docx(self, docx_path):
        doc = Document(docx_path)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
        cleaned = self.clean_text(text)
        return text

    def clean_text(self, text):
        text = unidecode(text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

cv = CV_Extrctor()
#df_text = cv.extract_text_from_pdf("C:/Users/ManalQatab/PycharmProjects/Salary-Index/CVs/ManalQatab_Resume.pdf")
df_text = cv.extract_text_from_docx("C:/Users/ManalQatab/PycharmProjects/Salary-Index/CVs/AI Training - BI Weekly Feedback - {1-2-2025}.docx")