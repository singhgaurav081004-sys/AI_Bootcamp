import numpy as np
subject =np.array(['Maths','Physics','Chemistry','English','Biology'])
exams=np.array(['Midterm','Final'])

np.random.seed(0)
marks= np.random.randint(10,101,size=(len(exams),len(subject)))
print("Subject",subject)
print("exams",exams)
print("Marks",marks)
print(np.mean(marks))
