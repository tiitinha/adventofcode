import re

valid_count, valid_count2 = 0, 0

with open('inputpeq.txt', 'r') as f:
    passports = [p.strip('\n') for p in f.read().split('\n\n')]
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for p in passports:
        if all(field in p for field in req_fields):
            valid_count += 1

    for p in passports:
        if not all(field in p for field in req_fields):
            continue
        fields = re.split(r'\s', p)
        pass_dict = {}
        validity = []

        for f in fields:
            i = f.split(':')
            if (i[1].isdigit() and i[0] != 'pid'):
                pass_dict[i[0]] = int(i[1])
            else:
                pass_dict[i[0]] = i[1]

        if ('byr' in pass_dict):
            validity.append(1920 <= pass_dict.get('byr') <= 2002)
        if ('iyr' in pass_dict):
            validity.append(2010 <= pass_dict.get('iyr') <= 2020)
        if ('eyr' in pass_dict):
            validity.append(2020 <= pass_dict.get('eyr') <= 2030)
        if ('hgt' in pass_dict):
            if ('cm' in str(pass_dict.get('hgt'))):
                hgt = int(re.search('[\d]+', pass_dict.get('hgt')).group(0))
                validity.append(150 <= hgt <= 193)
            elif ('in' in str(pass_dict.get('hgt'))):
                hgt = int(re.search('[\d]+', pass_dict.get('hgt')).group(0))
                validity.append(59 <= hgt <= 76)
            else:
                validity.append(False)
        if ('hcl' in pass_dict):
            validity.append(re.match(r'#[\da-f]{6}$', str(pass_dict.get('hcl'))))
        if ('ecl' in pass_dict):
            validity.append(pass_dict.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        if ('pid' in pass_dict):
            validity.append(re.match(r'\d{9}$', pass_dict.get('pid')))

        if (all(validity)):
            valid_count2 += 1

print(valid_count, valid_count2)
