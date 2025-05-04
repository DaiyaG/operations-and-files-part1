file1 = open('Codingal.txt',
                        'r')
file2 = open('CodingalUpdate.txt',
                              'w')

for lines in file1.readlines():

    if not (lines.startswith('Coding')):

        print(lines)

        file2.write(lines)

file2.close()
file1.close()        