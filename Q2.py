import xlsxwriter

def populateSheet(workbook,worksheet):
 # start entering data from next row
 row=1
 col=0
 
 # data will have a right and bottom border
 dataFormat = workbook.add_format({'num_format': 'dd/mm/yy', 'bottom':True, 'right':True}) 

 for i in range(0,3): # data to be taken for 10 users
  fname = raw_input("Enter First Name: ")
  lname = raw_input("Enter Last Name: ")
  dob = raw_input("Enter D.O.B in (dd/mm/yy): ")
  city = raw_input("Enter City: ")
  
  worksheet.write(row, col, fname, dataFormat)
  worksheet.write(row, col+1, lname, dataFormat)
  worksheet.write(row, col+2, dob, dataFormat)
  worksheet.write(row, col+3, city, dataFormat)

  row+=1
 return workbook

def main():
 workbook = xlsxwriter.Workbook('Ans2.xlsx') # creating a workbook named "Ans2"
 worksheet = workbook.add_worksheet("work") # adding a worksheet named "work"
 
 col=0
 row=0
 
 # adding header in EXCEL file with right, bottom border and bold format
 headerFormat = workbook.add_format({'bold': True, 'bottom':True, 'right':True})
 
 worksheet.write(row, col, "First Name", headerFormat)
 worksheet.write(row, col+1, "Last Name", headerFormat)
 worksheet.write(row, col+2, "D.O.B.", headerFormat)
 worksheet.write(row, col+3, "City",headerFormat)
 
 workbook=populateSheet(workbook,worksheet)  # sending created workbook for adding 10 data values 
 
 workbook.close()


main()


