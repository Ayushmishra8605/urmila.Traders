from fpdf import FPDF
from datetime import datetime
import streamlit as st


def download_button_logic(items_list: object, customer_name: object) -> None:
        # 1. PDF Setup
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)

        # Header
        pdf.cell(200, 10, txt="INVOICE / BILL", ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True, align='L')
        now = datetime.now()
        fomatted_time=now.strftime("%d/%m/%Y %H:%M:%S")
        pdf.cell(w=200,h=10,txt=f"now:{fomatted_time}", ln=True, align='L')
        pdf.cell(200, 10, txt="--------------------------------------------------", ln=True)

        # 2. Table Header
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(80, 10, "Product", 1)
        pdf.cell(30, 10, "Price", 1)
        pdf.cell(30, 10, "Qty", 1)
        pdf.cell(40, 10, "Total", 1)
        pdf.ln()

        # 3. Items Add Karna aur Total Calculate Karna
        pdf.set_font("Arial", size=12)
        grand_total = 0
        for item in items_list:
            line_total = item['amount'] * item['quantity']
            grand_total += line_total

            pdf.cell(80, 10, str(item['name']), 1)
            pdf.cell(30, 10, str(item['amount']), 1)
            pdf.cell(30, 10, str(item['quantity']), 1)
            pdf.cell(40, 10, str(line_total), 1)
            pdf.ln()

        # 4. Final Total in PDF
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(140, 10, "Grand Total", 1)
        pdf.cell(40, 10, f"Rs. {grand_total}", 1)
        # 5. PDF ko button ke liye taiyar karna
        pdf_output = pdf.output(dest='S').encode('latin-1')

        st.download_button(
            label="📥 Download PDF Bill",
            data=pdf_output,
            file_name=f"Bill_{customer_name}.pdf",
            )