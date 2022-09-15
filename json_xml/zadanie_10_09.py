import json
import pyconvert.pyconv
import xmltodict

class KinderGarden(object):
    def __init__(self, title, adress, contacts, info, capacity):
        self.title = title
        self.adress = adress
        self.contacts = contacts
        self.info = info
        self.capacity = capacity
    def __str__(self):
        return f'{self.title}, {self.adress}, {self.contacts}, {self.info}, {self.capacity}'

class Group(object):
    def __init__(self, educator, number, info):
        self.educator = educator
        self.number = number
        self.info = info
    def __str__(self):
        return f'{self.educator}, {self.number}, {self.info}'

class Child(object):
    def __init__(self, name, gender, birth_date, adress, parent_number, group):
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.adress = adress
        self.parent_number = parent_number
        self.group = group
    def __str__(self):
        return f'{self.name}, {self.gender}, {self.birth_date}, {self.adress}, {self.parent_number}, {self.group}'

class Educator(object):
    def __init__(self, name, gender, contacts, salary, kindergarden):
        self.name = name
        self.gender = gender
        self.contacts = contacts
        self.salary = salary
        self.kindergarden = kindergarden
    def __str__(self):
        return f'{self.name}, {self.gender}, {self.contacts}, {self.salary}, {self.kindergarden}'

class DataBase(object):
    def __init__(self, children):
        self.children = children

kindergarden1 = KinderGarden('Teddy Bear', 'Ostrovskiy 21/8', '+11111', 'state', 300)
educator1 = Educator('Marina', 'F', '+22222', 25000, kindergarden1)
group1 = Group(educator1, '1', 'little')
child1 = Child('Damir', 'M', '04.03.2020', 'Pushkina 5', '+33333', group1)

kindergarden2 = KinderGarden('MamiYami', 'Ostrovskiy 22/8', '+44444', 'private', 100)
educator2 = Educator('Sofi', 'F', '+55555', 90000, kindergarden2)
group2 = Group(educator2, '2', 'middle')
child2 = Child('Rahim', 'M', '04.03.2019', 'Chehova 7', '+66666', group2)

database = DataBase([child1, child2])

r = json.dumps(database, default=lambda x: x.__dict__, ensure_ascii=True, indent=True)
with open('file_json.json', 'w') as f:
    f.write(r)
with open('file_json.json', 'r') as file:
    stock = json.load(file)

def hehe(math):
    helper = [1, math]
    flag = 0
    while flag == 0:
        for elem in helper[1].items():
            if isinstance(elem[1], dict):
                helper = elem
                break
        else:
            flag = 1
    return helper

for matherial, num in zip(stock['children'], [0, 1]):
    kind_gard1 = KinderGarden(*list(hehe(matherial)[1].values()))
    matherial['group']['educator']['kindergarden'] = kind_gard1
    educ_1 = Educator(*list(hehe(matherial)[1].values()))
    matherial['group']['educator'] = educ_1
    group_1 = Group(*list(hehe(matherial)[1].values()))
    matherial['group'] = group_1
    child_1 = Child(*list(hehe(matherial)[1].values()))
    stock['children'][num] = child_1

xml_doc = pyconvert.pyconv.convert2XML(database)
with open('file_xml.xml', 'w') as f:
    f.write(xml_doc.toprettyxml())
with open('file_xml.xml', 'rb') as file:
    d = xmltodict.parse(file)

for matherial1, num in zip(d['DataBase']['childrens']['Child'], [0, 1]):
    kind_gard2 = KinderGarden(*list(hehe(matherial1)[1].values()))
    matherial1['Group']['Educator']['KinderGarden'] = kind_gard2
    educ_2 = Educator(*list(hehe(matherial1)[1].values()))
    matherial1['Group']['Educator'] = educ_2
    group_2 = Group(*list(hehe(matherial1)[1].values()))
    matherial1['Group'] = group_2
    child_2 = Child(*list(hehe(matherial1)[1].values()))
    d['DataBase']['childrens']['Child'][num] = child_2

if __name__ == '__main__':
    print('JSON')
    print(stock['children'][0],'\n', stock['children'][1])
    print('XML')
    print(d['DataBase']['childrens']['Child'][0], '\n', d['DataBase']['childrens']['Child'][1])