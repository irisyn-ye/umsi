# Lab Exercise 04
print('Lab Exercise 04 \n')

# Setup
employers = [
    ['Adobe Systems', 'California', '25000', ('Job', 'Internship'), 'software'],
    ['Advantage Health Centers', 'Michigan', '100', ('Job', 'Internship'), 'healthcare'],
    ['Amtrak', 'Various Locations', '25000', ('Job', 'Internship'), 'Transportation'],
    ['Blue Cross Blue Shield of Michigan', 'Michigan', '25000', ('Job', 'Internship'), 'Insurance'],
    ['Boston University', 'Massachusetts', '25000', ('Fellowship', 'Internship'), 'Education'],
    ['Elevance Health', 'Indiana', '25000', ('Internship', 'Fellowship'), 'healthcare'],
    ['Epic', 'Wisconsin', '20000', ('Internship', 'Job'), 'Software'],
    ['fairlife, LLC', 'Illinois', '1000', ('Job', 'Internship'), 'food'],
    ['Fan Duel', 'Florida', '1000', ('Internship', 'Job'), 'Software'],
    ['Gallagher', 'Illinois', '25000', ('Job',), 'Insurance'],
    ['GM Financial', 'Texas', '10000', ('Job', 'Internship'), 'automotive'],
    ['Mayo Clinic', 'Minnesota', '25000', ('Job', 'Internship'), 'Healthcare'],
    ['Northwestern Medicine', 'Illinois', '25000', ('Job', 'Fellowship'), 'Healthcare'],
    ['Optum', 'Minnesota', '25000', ('Job', 'Internship'), 'Healthcare'],
    ['Penske Truck Leasing', 'Pennsylvania', '10000', ('Job', 'Internship'), 'transportation'],
    ['Progressive', 'Wisconsin', '25000', ('Internship', 'Job'), 'insurance'],
    ['TikTok', 'California', '10000', ('Job', 'Internship'), 'Software'],
    ['Thomson Reuters', 'Minnesota', '25000', ('Internship', 'Job'), 'Software'],
    ['University of Michigan International Center', 'Michigan', '50', ('Internship', 'Fellowship'), 'Education'],
]


# Problem 01
for i in range(len(employers)):
    employers[i][2] = int(employers[i][2])

# print(f'Problem 1: Updated < employers > list:\n{employers}')

# Problem 02

large_fellowship = 0
for i in range(len(employers)):
    if 'Fellowship' in employers[i][-2] and employers[i][2] >= 20000:
        large_fellowship += 1

# print(f'Problem 2: There are {large_fellowship} large employer Fellowship positions.')

# Problem 03

mid_size_employers = []
for i in range(len(employers)):
    if int(employers[i][2]) >= 1000 and int(employers[i][2]) <= 5000:
        mid_size_employers.append(employers[i][0])

# print(f'Problem 3: Mid-size employers list:\n {mid_size_employers}')

# Problem 04

software_count = 0
health_count = 0
edu_count = 0
transport_count = 0
insurance_count = 0
other_count = 0

for i in range(len(employers)):
    if 'software' in employers[i][-1].lower():
        software_count += 1
    elif 'healthcare' in employers[i][-1].lower():
        health_count += 1
    elif 'education' in employers[i][-1].lower():
        edu_count += 1
    elif 'transportation' in employers[i][-1].lower():
        transport_count += 1
    elif 'insurance' in employers[i][-1].lower():
        insurance_count += 1
    else:
        other_count += 1

# print(f'Problem 4:\nSoftware employers: {software_count}\nHealthcare employers: {health_count}\nEducation employers: {edu_count}\n\
# Transportation employers: {transport_count}\nInsurance employers: {insurance_count}\nOther employers: {other_count}')


# Problem 05

idx = 0
num_employees = 0

avg_employee_num = 0

while idx in range(len(employers)):
    if employers[idx][-1].lower() == 'healthcare': 
        num_employees += employers[idx][2]
    idx += 1

avg_employee_num = int(num_employees / health_count)
print(f'Problem 5: Average number of employees among healthcare employers is {avg_employee_num}')
