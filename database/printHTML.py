import os

def writeTable(table, title):
    file = open("output.html", "a")
    
    file.write("<html><h3> " + title + ": </h3><table>")

    for i in table:
        file.write("<tr>")
        
        for j in i:
            file.write("<th>" + str(j) + "<th>")

        file.write("</tr>")
    
    file.write("</table></html>")

    file.close()

def deleteFile():
    if os.path.exists("output.html"):
        os.remove("output.html")
    

