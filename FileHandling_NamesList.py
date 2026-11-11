student_names = [
	"Aarav Patel",
	"Mia Chen",
	"Noah Johnson",
	"Anuj",
	"Ethan Williams",
	"Isabella Brown",
	"Liam Davis",
	"Ava Wilson",
	"Lucas Martinez",
	"Amira Khan",
]
file_path = "D:\DIPAK_AI_TRAINING\GIFTABLED_AI_LEARN\Programs\student_names.txt"

with open(file_path, "w+", encoding="utf-8") as file:
	for name in student_names:
		file.write(name + "\n")

with open(file_path, "r", encoding="utf-8") as file:
	saved_names = file.readlines()

print("Student names read from the file:")
for name in saved_names:
	print(name.strip())

file_path_csv = "D:\DIPAK_AI_TRAINING\GIFTABLED_AI_LEARN\Programs\students.csv"
import csv
students=[
     {"name": "Dipak","marks": 80},
      {"name": "Abhee","marks": 85}, ]

with open(file_path_csv,"w",newline="", encoding="utf-8") as file:
     writer= csv.DictWriter(file, fieldnames=["name","marks"])
     writer.writeheader()
     writer.writerows(students)


# #input/output int string
with open(file_path_csv,"r",newline="", encoding="utf-8") as file:
     reader = csv.DictReader(file)

for row in reader:
         print(row["name"], row["marks"])
         marks = int(row["marks"])
         print(marks + 5)


import json
file_path_json = "D:\DIPAK_AI_TRAINING\GIFTABLED_AI_LEARN\Programs\student_subject_2.json"
subject ={"course":"python", "passing_marks": 40, "Topics": ["txt", "csv","json"]}

with open(file_path_json,"w", encoding="utf-8") as file:
	json.dump(subject, file, indent=4)