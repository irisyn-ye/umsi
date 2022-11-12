# START PROBLEM SET 2
print('Problem Set 2 \n')

wellbeing_resources = 'Counseling and Psychological Services (CAPS)|734-764-8312, '\
'SilverCloud|, '\
'Dean of Students Office|734-764-7420, '\
'Office of Student Conflict Resolution|734-936-6308, '\
'Services for Students with Disabilities (SSD)|734-763-3000, '\
'Maize and Blue Cupboard (MBC)|734-936-2794, '\
'Ginsberg Center for Community Service Learning|734-763-3548, '\
'Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771, '\
'Multi-ethnic Student Affairs (MESA)|734-763-9044, '\
'Spectrum Center|734-763-4186'
# PROBLEM 01 (30 points)
print('\nPROBLEM 01')
wellbeing = wellbeing_resources.split(", ")
health = wellbeing[0:2]
academic = wellbeing[2:5]
community = wellbeing[-5:-3]
marginalized_comm = wellbeing[-3:]

# PROBLEM 02 (40 points)
print('\nPROBLEM 02')
addl_health_resources = ['UMSI Embedded CAPS Psychologist|Ashley Evearitt',
'Wolverine Wellness|734-763-1320']
health.extend(addl_health_resources)

uhs = 'University Health Service (UHS)|734-764-8320'
health.append(uhs)

trotter = 'Trotter Multicultural Center|734-763-3670'
marginalized_comm.insert(1, trotter)

addl_academic_resources = ['Sweetland Center for Writing', 'Office of the Ombuds']
addl_academic_resource_numbers = ['|734-764-0429', '|734-763-3545']
addl_academic_resources_0 = addl_academic_resources[0] + addl_academic_resource_numbers[0]
addl_academic_resources_1 = addl_academic_resources[1] + addl_academic_resource_numbers[1]
addl_academic_resources = []
addl_academic_resources.append(addl_academic_resources_0)
addl_academic_resources.append(addl_academic_resources_1)

academic.extend(addl_academic_resources)
print(academic)

# PROBLEM 03 (20 points)
print('\nPROBLEM 03')
health.reverse()
academic.sort()
marginalized_comm.sort(reverse=True)
umsi_caps = health.index('UMSI Embedded CAPS Psychologist|Ashley Evearitt')
student_focused_health_resources = health[umsi_caps-1:umsi_caps+1]

# PROBLEM 04 (10 points)
print('\nPROBLEM 04')
uhs = tuple(health[0].split('|'))
caps = tuple(health[-1].split('|'))
marginalized_comm_str = ','.join(marginalized_comm)

# END PROBLEM SET