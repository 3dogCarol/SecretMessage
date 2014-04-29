import os
import string
import webbrowser
import sys
import random

dir = "/Users/carollawrence/Documents/Udacity/ObjectOrientedProgramming/"
alpha = dir+"alphabet/"

def read_files(file_list):
    file_list = os.listdir(alpha)
    del file_list[0]
    return file_list

def code_msg(msg,file_list):
    msg = string.upper(msg)
    file_msg = []
    for c in msg:
        file_index = ord(c)-65
        #print(ord(c),file_index)
        if ord(c) >= 65:
            if file_index <26:
                file_msg.append(file_list[file_index])
        else:
            if ord(c) == 32:
                file_msg.append(file_list[27])
            if ord(c) == 46:
                file_msg.append(file_list[26])
    return file_msg

def create_webpage(msg,page1,page2,click):
	webpage = open(page1,"w")
	webpage.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
	webpage.write('<html xmlns="http://www.w3.org/1999/xhtml">\n')
	webpage.write('<head>\n')
	webpage.write('</head>\n')
	webpage.write('<body>\n')
	webpage.write('<div>\n')
	
	for file in msg:
		input = '<img src="'+alpha+file+'" width="100" height="100"/>'
		webpage.write(input)
	webpage.write('\n')
	webpage.write('</div>\n')
	if click == 0:
		webpage.write('<a href='+page2+'> Click to unscramble message </a>')  
	else:
		webpage.write('<a href='+page2+'> Click to rescramble message </a>')  		 
	webpage.write('</body>\n')
	webpage.write('</html>\n')
	
def scramble(msg):
	scrambled = []
	while msg:
		#print(len(msg),len(scrambled))
		ele = random.choice(msg)
		msg.remove(ele)
		scrambled.append(ele)		
	return scrambled

file_list = []
file_list = read_files(file_list)
msg = sys.argv[1]


file_msg = code_msg(msg,file_list)
tmp = []
for file in file_msg:
	tmp.append(file)
scrambled_msg = scramble(tmp)

webpage = dir+"SecretMessage.html"
unscrambled = dir+"Message.html"

create_webpage(scrambled_msg,webpage,unscrambled,0)
create_webpage(file_msg,unscrambled,webpage,1)

page = "file://" + dir + "SecretMessage.html"
webbrowser.open(page)
