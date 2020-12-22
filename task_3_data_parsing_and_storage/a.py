import tabula
import camelot
# "./Rec_Task/1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf" yes.
# path = "./Rec_Task/1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf"
# dfs = tabula.read_pdf(path, stream=True)
# tabula.convert_into("./Rec_Task/1c1edeee-a13e-4b2e-90be-eb1dd03c3384.pdf", "output.csv", output_format="csv", pages='all')


path = "./Rec_Task/a6b29367-f3b7-4fb1-a2d0-077477eac1d9.pdf"
tables = camelot.read_pdf(path)
tables.export("o.csv", f="csv", compress=True)

for i in tables:
    print(i.parsing_report)

# tabula.convert_into("./Rec_Task/d9f8e6d9-660b-4505-86f9-952e45ca6da0.pdf", "output.csv", output_format="csv", pages='all')
# print(dfs[0])
