"""""
The Class Grade Program is to display the number of grade, ist average,
and the percentage of grades that are above the average grade in a final exam
create a list to store 24 numbers (float) from the text file final.txt
capture user's input 24 times for their grades
we apprend the number/grade to the list 

Then define a function that calculate the number of grades
then calculate the average which takes the total/ number of grades
We convert the output of the percentage of grades that are above the average to a percentage


output calculated value to the user

end

""""""""
PSEUDO CODE

import final.txt
main():
    infile = open ("final.txt")
    num_grades = formListofGrades (dictionary)
    avg_grade = createAverageGrade (num_grades)
    calculate_percent_above_average = createPercentAboveAverage (avg_grade)

def creat_dictionary("final.txt")
read in final.txt
creat list =each line form the text file
close the file
create dict off the list

"""""
infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades) 
num = 0 
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:2f}%".format(100*num /len(grades)))




# grades = []

# for i in range(24):
#     grades.append(float(input("Enter the grade: ")))

# grades.sort()
# avgGrades = sum(grades[:]) / 24
# avg = "Average Grade {0:.2f}%".format(avgGrades)
# print("Average Grade {0:.2f}%".format(avgGrades))