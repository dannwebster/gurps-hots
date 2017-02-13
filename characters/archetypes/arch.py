#!/usr/local/bin/python
import re

f = open('../Archetypes.md', 'r')

regex = re.compile('.*\[(.*)\].*')
architypes = list()
for line in f:
    match = regex.match(line)
    if match:
        architypes.append(match.group(1))

print architypes

arch_regexes = [ re.compile('^\s*#?#?\s*' + l + '\s*$') for l in architypes ]

a = open('./Architect.md', 'r')

for i, line in enumerate(a):
        buffer = ""
    for arch_regex in arch_regexes:
        matching = False
        match = arch_regex.match(line)
        if match:
            print "here"
            if matching:
                print
                print "***"
                print buffer
                print "***"
                print
            matching = True
            buffer = ""
        if matching:
            print "also here"
            buffer += line



