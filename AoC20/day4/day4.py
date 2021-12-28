import re

def passportControl():

    count = 0
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open('inputpeq.txt') as f:
        passports = [p.strip('\n') for p in f.read().split('\n\n')]
        for passport in passports:
            cleanstuff = [None, None, None, None, None, None, None]

            if not all(field in passport for field in requiredFields):
                continue

            passportFields = re.split('\s', passport)
            legitCount = 0

            for field in passportFields:
                fieldName, fieldValue = field.split(':')
                if fieldName == 'byr' and 1920 <= int(fieldValue) <= 2002:
                    legitCount += 1
                    cleanstuff[0] = int(fieldValue)
                elif fieldName == 'iyr' and 2010 <= int(fieldValue) <= 2020:
                    legitCount += 1
                    cleanstuff[1] = int(fieldValue)
                elif fieldName == 'eyr' and 2020 <= int(fieldValue) <= 2030:
                    legitCount += 1
                    cleanstuff[2] = int(fieldValue)
                elif fieldName == 'hgt':
                    regex  = re.findall(r'(\d{2,3})(\w{2})$', fieldValue)
                    if len(regex) == 1:
                        height = int(regex[0][0])
                        unit = regex[0][1]
                        if unit == 'in' and 59 <= height <= 76:
                            legitCount += 1
                            cleanstuff[3] = fieldValue
                        elif unit == 'cm' and 150 <= height <= 193:
                            legitCount += 1
                            cleanstuff[3] = (fieldValue)
                elif fieldName == 'ecl' and fieldValue in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    legitCount += 1
                    cleanstuff[4] = fieldValue
                elif fieldName == 'hcl' and re.match(r'(#[\da-f]{6}$)', fieldValue):
                    legitCount += 1
                    cleanstuff[5] = fieldValue
                elif fieldName == 'pid' and re.match(r'\d{9}$', fieldValue):
                    legitCount += 1
                    cleanstuff[6] = fieldValue

            if (legitCount == 7):
                count += 1
                print(cleanstuff)

        return count

print(passportControl())
