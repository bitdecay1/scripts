import re
#print a vertical list into a line-by-line list
string = "gnats, irc, libuuid, list, lp, mail, www-data"
#The \s matches any whitespace character, and we just replace it with an empty string ''
string = re.sub(r'\s', '', string).split(',')

for data in string:
        if data != "null":
                print(data)
