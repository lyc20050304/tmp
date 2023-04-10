import pdfplumber
import csv

with pdfplumber.open("111_result_school_data.pdf") as pdf, open(
    "score.csv", "a"
) as csvfile:
    write = csv.writer(csvfile)

    for page in pdf.pages:
        for row in page.extract_tables()[0][1:]:
            write.writerow(row)
