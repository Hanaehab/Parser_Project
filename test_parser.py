import re

oneRuleFlag = False


def remove_non_ascii(s):
    return "".join(c for c in s if ord(c) < 128)


results = []
linesCounter = 0
infile = open('dimensions_rules.txt', 'r').readlines()
dimensions = {}

for index, line in enumerate(infile):

    if (line.startswith("//") and line.find('VIA') != -1 and line.find('.L') != -1 and line.find('.W') != -1):
        linesCounter += 1

    elif (line.startswith("//") == False and linesCounter != 0):

        i = infile.index(line)
        viaName = ""

        for times in range(1, linesCounter):
            ruleString = remove_non_ascii(infile[i + times]).strip()
            splitOnSpace = ruleString.split()
            viaName = [i for i in splitOnSpace if i.startswith('VIA')][0]
            results.append(ruleString)

        dimensions[viaName] = {}

        squareCounter = 0
        barCounter = 1
        for rule in results:
            newString = rule.replace('{',' ')
            newString = newString.replace('}',' ')
            print(newString.split())
            print((newString.split()).index('width'))
            # print(((rule.split('width'))[1].split('='))[2].split(','))



            # print((rule.split('=')).index('{width'))


        linesCounter = 0
        index = linesCounter + 1
    # print(results)

# with open('dimensions_rules.txt', 'r') as file:

# via = {}
# results = []
# linesCounter = 0
# index = 0
# for line in file:
#     if(line.startswith("/")):
#         linesCounter += 1
#     else:
#         linesCounter = 0
#         index = file.index(line)
#         for times in range(0, 3):
#             results.append(file[index + times])

# print(results)

# if (re.search("^/.*", line) and oneRuleFlag == False):
#     print("ignore")
#     continue

# elif(oneRuleFlag):
#     print((remove_non_ascii(line).strip()).split('='))

# elif (line.find('VIA') != -1 and line.find('.L') != -1 and line.find('.W') != -1):

#     oneRuleFlag = True
#     splittedString = (
#         (remove_non_ascii(line).strip()).split('='))[-1].strip()

#     getWidth = splittedString.split(',')
#     for width in getWidth:
#         via[width.strip()] = []
