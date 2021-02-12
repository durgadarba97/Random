from printHTML import writeTable, deleteFile
import mysql.connector

class MemberClaim:
    def __init__(self):
        self.salariesdb = mysql.connector.connect(host="localhost", user="root", passwd="qwerty1234", database="SALARIES")
        self.cursor = self.salariesdb.cursor()

    def getMembers(self):
        self.cursor.execute("SELECT * FROM Member;")
        writeTable(self.cursor.fetchall(), "Member table")

    def getClaim(self):
        self.cursor.execute("SELECT * FROM Claim;")
        writeTable(self.cursor.fetchall(), "Claim table")

    def innerJoin(self):
        self.cursor.execute("SELECT C.ClaimAmt, M.FirstName, M.LastName FROM Claim C INNER JOIN Member M ON C.MemberID = M.MemberID;")
        writeTable(self.cursor.fetchall(), "inner join")

    def leftOuterJoin(self):
        self.cursor.execute("SELECT C.ClaimAmt, M.FirstName, M.LastName FROM Claim C LEFT OUTER JOIN Member M ON C.MemberID = M.MemberID;")
        writeTable(self.cursor.fetchall(), "left outer join")
    
    def rightInnerJoin(self):
        self.cursor.execute("SELECT M.MemberID, C.ClaimAmt, M.FirstName, M.LastName FROM Claim C RIGHT OUTER JOIN Member M ON C.MemberID = M.MemberID;")
        writeTable(self.cursor.fetchall(), "right outer join")

    def crossJoin(self):
        self.cursor.execute("SELECT * FROM Claim CROSS JOIN Member M;")
        writeTable(self.cursor.fetchall(), "cross join")

if __name__ == "__main__":
    memberclaim = MemberClaim()

    # memberclaim.getMembers()
    # memberclaim.getClaim()
    # deleteFile()
    # memberclaim.innerJoin()
    memberclaim.crossJoin()

