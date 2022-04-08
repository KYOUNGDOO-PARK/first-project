from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "NodoSheet"
wb.save("sample.xlsx")
wb.close()