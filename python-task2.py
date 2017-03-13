print("####################################")
print("TASK 1")
#My function task1
def task1():
    keys = ['1', '2', '3', '4', '5', '6']
    values = [100, 40, 0, 74, 77]
#I compare the quantity of lists KEYS and VALUES
    if (len(keys) > len(values)):
        while(len(keys) > len(values)):
#Add a value NONE to the list VALUES
             values.append(None)
    else:
#Shortens the list VALUES with the size of list KEYS
        values = values[0:len(keys)]
#Creates new dictionary which has both keys nad values
    app = dict(zip(keys, values))
#Shows the dictionary
    print(app)
task1()

print ("####################################")
print ("TASK 2")
#Includes regular expression module
import re
#Regexp which looks at all special symbols
change = re.compile(u'\W+?', re.UNICODE)
word = input("What is your string? ")
#Turns into lower case
word_new = word.lower()
#Removes all special symbols from the string
word_new = change.sub('', word_new)
#Original string and the string vice versa should coincide!!!
rev_word = word_new[::-1]
if word_new == rev_word:
    print("%s IS a palyndrome" % (word))
else:
    print("%s IS NOT a palyndrome" % (word))


print ("####################################")
print ("TASK 3")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(b)
#Function SET creates a unique aggregate A and B
#Then function LIST combines two aggregates A and B into list C
c = list(set(a) | set(b))
print(c)


print("####################################")
print("TASK 4")
import re
import collections
#variable PATH which contains the path to access_log
path = '/home/student/apache_logs/access_log'
access_log = open(path, 'r')
#variable ip_mask is a pattern which looks only for IP addresses
ip_mask = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
#variable ip_list will contain values which matched the pattern
ip_list = re.findall(ip_mask, access_log.read())
#variable output returns a list of the 10 most common elements and their counts from the most common to the least.
output = collections.Counter(ip_list).most_common(10)
#variable ip goes through the list and prints the IP address and their count in access_log
for ip in output:
    print('IP address %s  meets \n %d times' % (ip[0], ip[1]))
    print('===================================')







