try:
  f = open("demofile.txt")  # Open in write mode
  try:
    f.write("I Am Asik")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
else:
    print("Code Executed Successfully")



# -------------------------------------->Right Version<---------------------------------------
# try:
#   f = open("demofile.txt","w")  # Open in write mode
#   try:
#     f.write("I Am Asik")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
# else:
#     print("Code Executed Successfully")
