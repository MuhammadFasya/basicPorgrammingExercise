username = "admin"
password = "admin"
if username !="admin":
  if password !="admin":
    print("A")
  elif password == "admin":
    print("B")
  else:
    print("C")
else:
  if password != "admin":
    print("D")