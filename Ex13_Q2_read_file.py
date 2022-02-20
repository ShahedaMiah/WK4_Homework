#Q2, P2
pelican = open("pelican.txt", 'r')
print(pelican.read(), '\n')

#Q2, P3 - using '.seek' to go back to the beggining of the file, so keeping the file open
with open("pelican.txt", 'r') as pelican:
    data_type = (type(pelican.read()))
    print(data_type)
    pelican.seek(0)
    print(pelican.read())

#Q2, P3 - opening file each time you want to read again
with open("pelican.txt", 'r') as pelican:
    data_type = (type(pelican.read()))
    print(data_type)
with open("pelican.txt", 'r') as pelican:
    print(pelican.read())

#Q2, P5 - read file into list (list of words) and output number of items in the list
with open("pelican.txt", 'r') as pelican:
    pelican_data = pelican.read()
    pelican_list_line = pelican_data.replace('\n', ' ').split(" ")
    print('\n', pelican_list_line)
    print(len(pelican_list_line))

#Q2, P5 - read file into list (list of lines) and output number of items in the list
with open("pelican.txt", 'r') as pelican:
    pelican_list1 = pelican.readlines()
    print('\n', pelican_list1)
    print(len(pelican_list1))

#Q2, P5 - read file into list (list of lines, with list of words in lines) and output number of items in the list
with open("pelican.txt", 'r') as pelican:
    for pelican_list_line in pelican:
        print((pelican_list_line.split(' ')))
        print(len(pelican_list_line.split(' ')))

#Q2, P6 - use loop to iterate over and print contents of the file
with open("pelican.txt", 'r') as pelican:
    print('\n', pelican.readline(), end = " ")
    print(pelican.readline(), end = " ")
    print(pelican.readline(), end = " ")
    print(pelican.readline(), end = " ")
    print(pelican.readline())