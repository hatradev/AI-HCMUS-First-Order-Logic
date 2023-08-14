class kb:
  def __init__(self, name, negative = False):
    self.name = name
    self.negative = negative
  
  def findIndex(self, kbs: list):
    return
  
  def check():
    return

class fact(kb):
  def __init__(self, name, objects, negative= False):
    kb.__init__(self, name, negative)
    self.objs = objects
  
  def findIndex(self, kbs: list):
    rt = []
    for i in range(len(kbs)):
      if self.name == kbs[i].name:
        rt.append(i)     
    return rt
  
  def check(self, kbs: list):
    length = len(self.objs) - 1
    rt = []
    for i in self.findIndex(kbs):
      if kbs[i].objs[length - q.pos] == q.objs[length - q.pos] or not length:
        rt.append(kbs[i].objs[q.pos])
    return rt
    
    
class rule(kb):
  def __init__(self, name, objects, facts, operator = 'and', negative = False):
    kb.__init__(self, name, negative)
    self.opr, self.objs = operator, objects
    self.facts = facts
    
  def findIndex(self, kbs: list):
    rt = []
    for i in range(len(kbs)):
      if self.name == kbs[i].name:
        rt.append(i)     
    return rt
  
  def check(self, kbs: list):
    main_var = [[]] * len(self.objs)
    temp_var = []
    length = len(self.objs) - 1
    rt = []
    for i in self.findIndex(kbs):
      if kbs[i].objs[length - q.pos] == q.objs[length - q.pos] or not length:
        rt.append(kbs[i].objs[q.pos])
    return rt

Facts = []

Facts.extend((fact("Male", ["Tra"]), fact("Female", ["Giang"]), fact("Female", ["Trinh"])))
Facts.extend((fact("Male", ["L"]), fact("Female", ["Huong"]), fact("Male", ["Tu"]), fact("Male", ["Tac"]), fact("Female", ["Xanh"])))

Facts.append(fact("Parent", ["L", "Tra"]))
Facts.append(fact("Parent", ["L", "Giang"]))
Facts.append(fact("Parent", ["L", "Trinh"]))

Facts.append(fact("Parent", ["Huong", "Tra"]))
Facts.append(fact("Parent", ["Huong", "Giang"]))
Facts.append(fact("Parent", ["Huong", "Trinh"]))

Facts.append(fact("Parent", ["Tac", "L"]))
Facts.append(fact("Parent", ["Xanh", "L"]))

Facts.append(fact("Parent", ["Tac", "Tu"]))
Facts.append(fact("Parent", ["Xanh", "Tu"]))

Facts.append(fact("Married", ["L", "Huong"]))
Facts.append(fact("Divorced", ["L", "Huong"]))

Facts.append(fact("Married", ["Tac", "Xanh"]))


Rules = []

Rules.append(rule("GrandFather", ["GF", "GC"], [fact("Male", ["GF"]), fact("Parent", ["GF", "X"]), fact("Parent", ["X", "GC"])]))
Rules.append(rule("GrandMother", ["GM", "GC"], [fact("Female", ["GM"]), fact("Parent", ["GM", "X"]), fact("Parent", ["X", "GC"])]))

Rules.append(rule("Father", ["F", "C"], [fact("Male", ["F"]), fact("Parent", ["F", "C"])]))
Rules.append(rule("Mother", ["M", "C"], [fact("Female", ["M"]), fact("Parent", ["M", "C"])]))


class SingleQuestion:
  def __init__(self, name, objects, pos):
    self.name = name;
    self.var = lambda x: f"{x}"
    self.pos = pos #-1 (True, False), 0, 1
    self.objs = objects
    
class DoubleQuestion:
  def __init__(self, name, objects, pos, operator = 'and'):
    for i in range(2):
      self.question[i] = SingleQuestion(name[i], objects[i], pos[i])
    self.opr = operator

q = SingleQuestion("Parent", ["X", "Tra"], 0)
q1 = SingleQuestion("Male", ["X"], 0)
q2 = SingleQuestion("Female", ["X"], 0)
q3 = SingleQuestion("Female", ["Giang"], -1)
q4 = SingleQuestion("Parent", ["Giang", "Tra"], -1)

def findinRules(rules, q: SingleQuestion):
  rt = []
  for i in range(len(rules)):
    if q.name == rules[i].name:
      rt.append(i)     
  return rt

def findinFacts(facts, q: SingleQuestion):
  rt = []
  for i in range(len(facts)):
    if q.name == facts[i].name:
      rt.append(i)
  return rt

def checkinFacts(listFacts, facts, q: SingleQuestion):
  if q.pos == -1:
    for i in listFacts:
      if q.objs == facts[i].objs:
        return True
    return False
  else:
    res = []
    k = len(q.objs) - 1
    for i in listFacts:
      if facts[i].objs[k - q.pos] == q.objs[k - q.pos] or not k:
        res.append(facts[i].objs[q.pos])
    return res

def solveSingleQuestion(rules, facts, q: SingleQuestion):
  result = []
  tmp = findinRules(rules, q)
  if len(tmp) == 0:
    tmp = findinFacts(facts, q)
    return checkinFacts(tmp, facts, q)
  for i in tmp:
    result.append(checkinFacts(findinFacts(facts, SingleQuestion(Rules[i].name, Rules[i].objs, ))))
  
  return 0

print(solveSingleQuestion(Rules, Facts, q4))