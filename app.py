# 1.  opens a file, reads its contents, and prints them
with open("story.txt" , "r") as file:  # we open a file story.txt and name it as file
  story = file.read() # 2. we store the file read into the variable story
  print(story) # 3. we print the file content finally
  
# 2. writes data to a file
# Create a program that writes your name and profession to a file called my_info.txt

with open("my_info.txt" , "w") as file:
  file.write("my name is sadaf and i m front end developer.")
  