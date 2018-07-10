#Create a "students" class

class Student(object):
	'''Each student needs to have an ID, a set of homework grades,
	a set of exam grades, and an attendance record.
	'''
	def __init__(self, idNumber, homeworkGrades, examGrades, attendanceRecord):
		self.idNumber = idNumber
		self.homeworkGrades = homeworkGrades
		self.examGrades = examGrades
		self.attendanceRecord = attendanceRecord
	
	def addHomeworkGrade(self, grade):
	    self.homeworkGrades.append(grade)

        def addExamGrade(self, grade):
            self.examGrades.append(grade)

        def inAttendance(self, present):
            if present == "yes":
                self.attendanceRecord.append(1)
            else:
                self.attendanceRecord.append(0)
                
        def checkAttendance(self):
            attendance = sum(self.attendanceRecord)
            print("Student " + str(self.idNumber) + " has attended " + str(attendance) + " classes.")
        
        def homeworkAverage(self):
            hwAvg = sum(self.homeworkGrades)/len(self.homeworkGrades)
            return hwAvg
            
        def examAverage(self):
            exAvg = sum(self.examGrades)/len(self.examGrades)
            return exAvg

Kat = Student("A37", [10,9,10], [92,97], [1,0,0,0,1,1,1,0,1,0,1])