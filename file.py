class kb:
  def __init__(self, name, objects, negative = False):
    self.name = name
    self.negative = negative
    self.objs = objects
  
  def xuat(self):
    print("OK")

class Fact(kb):
  def __init__(self, name, objects, negative= False):
    kb.__init__(self, name, objects, negative)
  
  def xuat(self):
    print(self.name, ": ", self.objs)
    print("OK")    
    
class Rule(kb):
  def __init__(self, name, objects, kbs, operator, negative = False, isDistinct = False):
    kb.__init__(self, name, objects, negative)
    self.opr = operator
    self.kbs = kbs
    self.isDistinct = isDistinct
    
  def xuat(self):
    print(self.name, ": ", self.objs)
    print("OK")    

def splitFacts(line):
  first = line.split("(")
  if "" in first:
    first.remove("")
  if first[-1].endswith(').'):
    first.extend(first[-1].split(")."))
    first.pop(1)
    first.pop(-1)
  elif first[-1].endswith(') '):
    first.extend(first[-1].split(") "))
    first.pop(1)
    first.pop(-1)
  elif first[-1].endswith(')). '):
    first.extend(first[-1].split(") "))
    first.pop(1)
    first.pop(-1)
  elif first[-1].endswith(')) '):
    first.extend(first[-1].split(") "))
    first.pop(1)
    first.pop(-1)

  if first[-1].endswith("'"):
    first[-1] = first[-1][1:-2]
    first[-1] = first[-1].replace("', '", '><')
  else:
    first[-1] = first[-1].replace(", ", '><')
  
  first.extend(first[-1].split("><"))
  first.pop(1)
  return first

def splitRules(first, it, index):
  if first[index].find('), (') != -1:
    first.extend(first[index].split('), ('))
    it.extend([1]*(len(first) - 1))
    return True
  
  if first[index].find('); (') != -1:
    first.extend(first[index].split('); ('))
    it.extend([0]*(len(first) - 1))
    return True
  
  if first[index].find('), ') != -1:
    first.extend(first[index].split('), '))
    it.extend([1]*(len(first) - 1))
    return True
  
  if first[index].find('); ') != -1:
    first.extend(first[index].split('); '))
    it.extend([0]*(len(first) - 1))
    return True
    
  for i in range(len(first)):
    idx = first[i].find("\\==")
    if (idx != -1):
      first.pop(i)
      it.pop(i-1 if i >= 1 else 0)
    return True
  return False

def readFactsAndRules(filename):
  f = open(filename, 'r')
  datalist = f.readlines()
  facts = []
  rules = []
  for line in datalist:
    if line.startswith('/*') or line == "" or line == "\n":
      continue
    if line.find(":-") == -1:
      #facts
      first = splitFacts(line[:-1])
      print(1, first)
      facts.append(Fact(first[0], first[1:]))
    else:
      #rules
      first = line.split(":- ")
      head = splitFacts(first[0])
      first.pop(0)
      first[-1] = first[-1][:-1]
      it = []
      
      # flag = True
      # while flag:
      #   for idx in range(len(first)):
      #     flag = splitRules(first, it, idx)
      
      splitRules(first, it, -1)
      
          
      
      print(2, first, it)
      # print(head)
  return 0

readFactsAndRules("BritishFamily.txt")


# print(splitFacts("(male(Person"))
# print(splitFacts("parent(Parent, Child"))
# print(splitFacts("divorced('Princess Diana', 'Prince Charles')."))
# print(splitFacts("male('James, Viscount Severn')."))