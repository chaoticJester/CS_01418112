s1 = 345
s2 = 440
#--------------------------------------
s3 = int(s1 + s2)

hours = int(s3//3600)
minutes = int(s3/60) - (hours * 60)
seconds = int(s3%60)
#--------------------------------------
print("It is", hours, "hours", minutes, "minutes and", seconds, "seconds.")
