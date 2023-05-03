print('Multiparadigm programming languages, Lab № 2')
print('Yaremchenko Olexandr-221d')

TEMPLATE = 'Enter {}'

x = int(input(TEMPLATE.format('x')))
y = int(input('Enter y'))
z = int(input('Enter z'))

a = x - (x + (y / z)) / (78 + y)

print('Result is: ', a)
