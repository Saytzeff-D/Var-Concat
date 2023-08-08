# Various ways to concatenate
my_name = 'David is a'
school = 'student of SQI'

# fulltext = ' '.join([my_name, school])
# fulltext = '%s %s' % (my_name, school)
fulltext = '{} {}'.format(my_name, school)
print(fulltext)

fullname = 'David Atanda'
level = '200L'
institution = 'Obafemi Awolowo University'
address = 'Ogbomoso, Oyo State'
passion = 'Health and Tech'
role = 'Fullstack web developer'
lang = 'Javascript'

print(
    f"My name is {fullname}. I'm currently a {level} student at {institution}. I live in {address}. My passion for {passion} keeps me going. A {role} with great expertise in {lang}"
)