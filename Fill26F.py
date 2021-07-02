#!/usr/bin/env python
# Jacob Salmela edited by Miguel Lopez Rivera
# 2016-06-02
# edited 7/1/2021
# Writes text to a PDF at coordinates.  Use for quickly filling out forms that you use regularly.
# This takes some manual setup, but saves a ton of time once done

#Currently this script will only be used to fill out form 26F for MFD

# http://stackoverflow.com/a/17538003
# Make sure to install the two utilities below first
# pip install PyPDF2
# pip install reportlab

######## IMPORTS #########
import sys
import os
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime

####### VARIABLES ########
# Get the filename and extension so we can use it for renaming the newly-created file
filename, file_extension = os.path.splitext(sys.argv[1])

# Append "-filled" to the filename and save it in the same place
# This retains the original file so it can be used again with the script
# It also saves the file in the same folder so it's easy to find
filled_out_file = filename + "-filled" + file_extension

#Static information for form 26F
#user will be prompted to enter variable data in main()
#A datetime object is created to call functions that will create the date,
#these are converted into strings and then joined by slashes
dt = datetime.datetime.now()
todays_date = "/".join([str(dt.month), str(dt.day), str(dt.year)])

####### FUNCTIONS ########
def main():
    packet = BytesIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    
    can.drawString(447, 610, todays_date)
    can.drawString(452, 231, todays_date)
    
    units = input("How many units? (If more than one, they must have certification from Building Dept.): ")
    
    reinspect = input("Is this a reinspection? Enter \"y\" or \"n\": ")
    while reinspect != "y" and reinspect != "n":
        reinspect = input("input not valid, please enter \"y\" or \"n\": ")
        
    scheduled_for = input("Enter date of inspection: ")
    scheduled_time = input("Enter time of inspection: ")
    if reinspect == "n":
        can.drawString(138, 754, scheduled_for)
        can.drawString(220, 754, scheduled_time)
    else:
        fee = "$50.00"
        can.drawString(377, 754, scheduled_for)
        can.drawString(431, 754, scheduled_time)
        
    can.drawString(65, 457, fee)
    can.drawString(90, 105, fee)
    location = input("Enter location of property: ")
    can.drawString(132, 544, location)
    can.drawString(231, 194, location)
    built = input("Enter year property was built: ")
    can.drawString(366, 547, built)
    owner = input("Enter property owner's last name: ")
    can.drawString(123, 524, owner)
    
    # Apply the changes
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # Read the existing PDF (the first argument passed to this script)
    existing_pdf = PdfFileReader(open(filename + file_extension, "rb"))
    output = PdfFileWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # Finally, write "output" to a real file
    outputStream = open(filled_out_file, "wb")
    output.write(outputStream)
    outputStream.close()
    
    os.system("start " + filled_out_file)


######### SCRIPT #########
if __name__ == "__main__":
    main()
