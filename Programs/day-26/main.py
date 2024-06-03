student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key)

import pandas

student_df = pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(row.student)

