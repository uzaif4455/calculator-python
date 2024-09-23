# READING A FILE

# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()
#
'''with open('myfile.txt', 'a') as f:
  f.write("Hey I a uzaif")
  f = open('myfile.txt', 'r')
  print(f)
  f.seek(6)  #ye isse 6 position index tak jo bhi rahenga us ko ye skip kar denga aur age ka jo bhi hai wo hame read() k through milenga
  text = f.read()
  print(text)
  f.close()'''

  ####
  """with open('myfile.txt', 'w') as f:
      f.write("Hey I a uzaif")
      f = open('myfile.txt', 'r')
      print(f)
      # f.seek(6)  #ye isse 6 position index tak jo bhi rahenga us ko ye skip kar denga aur age ka jo bhi hai wo hame read() k through milenga
      f.truncate(6)
      text = f.read()
      print(text)
      f.close()"""