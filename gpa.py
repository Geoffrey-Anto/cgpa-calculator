import math

gradeMap = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "N": 0,
}

def read_csv_server(csvData) -> float:
    grades = []
    creditSum = 0
    csvData = [row.split(",") for row in csvData.split("\r\n")]
    for row in csvData:
        [credit, grade] = row
        credit = float(credit)
        grade = gradeMap[grade]
        grades.append(credit * grade)
        creditSum += credit
    gpa = float(sum(grades)) / float(creditSum)
    decimal = gpa - math.floor(gpa)
    return math.floor(gpa) + math.ceil(decimal*100)/100
