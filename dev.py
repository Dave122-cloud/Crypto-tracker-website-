 students_score =[12,45,68,87,23,55,62,75,90,60,41,56.]
#total_exam_score = sum(students_score)
#print(total_exam_score)
#(password)

password_list = []
for char in range(1, n_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, n_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, n_symbols +1):
    password_list.append(random.choice(symbols))

    print(password_list)
    random.shuffle(password_list)
    print(password_list)