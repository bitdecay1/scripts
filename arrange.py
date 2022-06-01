import re

string = "auditor, backup, bin, daemon, games, gnats, irc, libuuid, list, lp, mail, man, mysql, news, nobody, proxy, root, sshd, sync, sys, sysadmin, syslog, uucp, www-data"
#The \s matches any whitespace character, and we just replace it with an empty string ''
string = re.sub(r'\s', '', string).split(',')

for data in string:
        if data != "null":
                print(data)
