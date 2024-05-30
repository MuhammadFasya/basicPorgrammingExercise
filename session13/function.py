# create a function 
def getAboutMe ():
  print("My name is petot")
getAboutMe()

#static
def getAboutMe ():
  return "My name is fasya"

about_me = getAboutMe ()
print(about_me)

#dynamic
def getAboutMe (name, class_name):
  return "My name is " + name + " my class is " + class_name

about_me = getAboutMe("udin","Sastra Mesin", "UDIN PETOT")
print(about_me)

#more function
def getAboutMe(name, class_name):
  course = getCourses(class_name)
  return "My name is " + name + " my course is " + course

def getCourses(class_name):
  if(class_name == "TI23T"):
    return "Basic Programming"
  else:
    return "Object Oriented Programming"

about_fasya = getAboutMe ("Fasya", "TI23T")
print(about_fasya)