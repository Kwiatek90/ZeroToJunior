#challenge

#Write a program that contains the following lists of lists:
#universities = [
#['California Institute of Technology', 2175, 37704],
#['Harvard', 19627, 39849],
#['Massachusetts Institute of Technology', 10566, 40732],
#['Princeton', 7802, 37000],
#['Rice', 5879, 35551],
#['Stanford', 19535, 40569],
#['Yale', 11701, 40500]
#]
#Define a function, enrollment_stats(), that takes, as an input, a list of
#lists where each individual list contains three elements: (a) the name
#of a university, (b) the total number of enrolled students, and (c) the
#annual tuition fees.
#enrollment_stats() should return two lists: the first containing all of
#the student enrollment values and the second containing all of the
#tuition fees.
#Next, define a mean() and a median() function. Both functions should
#take a single list as an argument and return the mean and median of
#the values in each list.
#Using universities, enrollment_stats(), mean(), and median(), calculate
#the total number of students, the total tuition, the mean and median
#of the number of students, and the mean and median tuition values.
#Finally, output all values, and format the output so that it looks like
#this:
#******************************
#Total students: 77,285
#Total tuition: $ 271,905
#Student mean: 11,040.71
#Student median: 10,566
#Tuition mean: $ 38,843.57
#Tuition median: $ 39,849
#******************************

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

enroll_students = []
enroll_tuition_fees = []

def enrollment_stats(list_universities):
    for university in list_universities:
        enroll_students.append(university[1])
        enroll_tuition_fees.append(university[2])
        
def mean(list_to_mean):
    lenght = len(list_to_mean)
    sum_list = sum(list_to_mean)
    mean = sum_list / lenght
    return mean

def median(list_to_median):
    list_to_median.sort()
    length = len(list_to_median)
    result = int((length - 1) / 2)
    
    return list_to_median[result]
    
    

enrollment_stats(universities)
mean_students = mean(enroll_students)
mean_tuition = mean(enroll_tuition_fees)
median_students = median(enroll_students)
median_tuition = median(enroll_tuition_fees)

print("******************************")
print(f"Total students: {sum(enroll_students):,.2f}")
print(f"Total tuition: $ {sum(enroll_tuition_fees):,}\n" )
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,.2f}\n")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: {median_tuition:,.2f}")