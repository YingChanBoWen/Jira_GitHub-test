import os

f = open("log.txt", "w")  

files = os.popen("git log --graph --pretty=format:\'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset\' --abbrev-commit --date=relative --since=\"2019.07.26\" --until=\"2019.07.30\"").readlines() 
for file_item in files:
	print >> f, file_item
f.close()
