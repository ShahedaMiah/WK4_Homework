# pelican = open('pelican.txt', 'a') - this creates and opens the .txt file in append mode
# pelican.write("A wonderful bird is the pelican") - this will append the string in the .txt file.
# pelican.close - this will close the file

pelican = open('pelican.txt', 'a')
pelican.write("\nextra stuff to test")
pelican.write("\nmore extra stuff without closing and re-opening file")
