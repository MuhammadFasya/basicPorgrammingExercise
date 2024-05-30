# Module adalah kumpulan function
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