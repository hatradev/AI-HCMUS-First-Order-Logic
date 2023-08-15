class kb:
  def __init__(self, name, objects, negative = False):
    self.name = name
    self.negative = negative
    self.objs = objects

class Fact(kb):
  def __init__(self, name, objects, negative= False):
    kb.__init__(self, name, objects, negative)    
    
class Rule(kb):
  def __init__(self, name, objects, kbs, operator, negative = False):
    kb.__init__(self, name, objects, negative)
    self.opr = operator
    self.kbs = kbs

facts = []
# Gender
facts.append(Fact("Male", ["Tra"]))
facts.append(Fact("Female", ["Giang"]))
facts.append(Fact("Female", ["Trinh"]))
facts.append(Fact("Male", ["L"]))
facts.append(Fact("Female", ["Huong"]))
facts.append(Fact("Male", ["Tu"]))
facts.append(Fact("Male", ["Tac"]))
facts.append(Fact("Female", ["Xanh"]))

# Parent
facts.append(Fact("Parent", ["Tac", "L"]))
facts.append(Fact("Parent", ["Xanh", "L"]))
facts.append(Fact("Parent", ["Tac", "Tu"]))
facts.append(Fact("Parent", ["Xanh", "Tu"]))
facts.append(Fact("Parent", ["L", "Tra"]))
facts.append(Fact("Parent", ["L", "Giang"]))
facts.append(Fact("Parent", ["L", "Trinh"]))
facts.append(Fact("Parent", ["Huong", "Tra"]))
facts.append(Fact("Parent", ["Huong", "Giang"]))
facts.append(Fact("Parent", ["Huong", "Trinh"]))

# Marriage
facts.append(Fact("Married", ["L", "Huong"]))
facts.append(Fact("Divorced", ["L", "Huong"]))
facts.append(Fact("Married", ["Tac", "Xanh"]))

# ? - parent(X, "Tra") 
# parent("L", "Tra") => TRUE

rules = []
rules.append(Rule("Father", ["F", "C"], [kb("Male", ["F"]), kb("Parent", ["F", "C"])], [1]))
rules.append(Rule("Mother", ["M", "C"], [kb("Female", ["M"]), kb("Parent", ["M", "C"])], [1]))
rules.append(Rule("GrandFather", ["GF", "GC"], [kb("Father", ["GF", "X"]), kb("Parent", ["X", "GC"])], [1]))
rules.append(Rule("GrandMother", ["GM", "GC"], [kb("Mother", ["GM", "X"]), kb("Parent", ["X", "GC"])], [1]))
# SingleQuestion("GrandFather", ["X", "Tra"]) ==> Tac
# ? - Father(X, "Tra") => "L"
# SingleQuestion("Father", ["X", "Tra"], 0)


class SingleQuestion:
  def __init__(self, name, objects, pos):
    self.name = name
    self.var = lambda x: f"{x}"
    self.pos = pos #-1 (True, False), 0, 1
    self.objs = objects
    
class DoubleQuestion:
  def __init__(self, name, objects, pos, operator = 'and'):
    for i in range(2):
      self.question[i] = SingleQuestion(name[i], objects[i], pos[i])
    self.opr = operator

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

def solveFact(kbsIndex, facts, q: SingleQuestion):
  if q.pos == -1:
    for i in kbsIndex:
      if q.objs == facts[i].objs:
        return True
    return False
  else:
    res = []
    k = len(q.objs) - 1
    for i in kbsIndex:
      if facts[i].objs[k - q.pos] == q.objs[k - q.pos] or not k:
        res.append(facts[i].objs[q.pos])
    return res 
  
def printSingleQuestion(q: SingleQuestion):
  print("== Câu hỏi mới==")
  print(q.name)
  print("Objs: ", q.objs)
  print(q.pos)
  print("================")


def common_member(a, b):
    result = [i for i in a if i in b]
    return result

def solveSingleQuestion(rules, facts, q: SingleQuestion, questions: [SingleQuestion]):
  kbsIndex = findinRules(rules, q)
  if len(kbsIndex) == 0:
    kbsIndex = findinFacts(facts, q)
    return solveFact(kbsIndex, facts, q)
  # Kiểm tra câu hỏi là YES-NO hay WHO?
  if(q.pos == -1):
    result = True
  else: result = []
  for kbI in kbsIndex:
    # Duyệt qua từng kb nhỏ trong kb lớn
    for k in range(len(rules[kbI].kbs)):
      kb = rules[kbI].kbs[k]
      print(rules[kbI].name, rules[kbI].objs)
      # Tạo một mảng obj mới để lưu các giá trị cụ thể cho câu hỏi mới
      newObjs = []
      varIdx = q.pos
      # Duyệt qua từng obj trong kb nhỏ
      idx = -1
      for i in range(len(kb.objs)):
        flag = True
        # Tìm vị trí tương ứng của obj đó trong kb lớn 
        try: 
          print(rules[kbI].objs, kb.objs[i])
          idx = rules[kbI].objs.index(kb.objs[i])
        except ValueError:
          idx = -1      
        print("Tìm được ở ", idx)
        if(idx != -1): # Nếu tìm được thì lưu vào newObjs
          newObjs.append(q.objs[idx])
          if(idx == q.pos): # Vị trí tìm được là vị trí của biến 
            varIdx = i # Cập nhật vị trí biến mới trong newQ        
        else: # Nếu k tìm được thì đó là biến trung gian
          if(q.pos == -1):
            newObjs.append(kb.objs[i])
            if(len(questions) == 0): varIdx = i
            # break
          elif(i == q.pos): # Vị trí biến trung gian trùng vị trí biến => Giải 
            newObjs.append(kb.objs[i])
          else: # Vị trí biến trung gian k trùng vị trí biến => K giải
            questions.append(SingleQuestion(kb.name, kb.objs, q.pos))
            flag = False
        print(i, flag, newObjs)
        print("=====================")
      if(flag):
        newQ = SingleQuestion(kb.name, newObjs, varIdx)
        printSingleQuestion(newQ)
        res = solveSingleQuestion(rules, facts, newQ, questions)
        # print(res)
        if(k == 0):
          result = res
        elif(rules[kbI].opr[k - 1] == 1): # AND
          if(q.pos == -1): # Câu hỏi YES-NO
            result = result and res
          else: # Câu hỏi WHO
            # printSingleQuestion(newQ)
            for quesIdx in range(len(questions)):
              ques = questions[quesIdx]
              # printSingleQuestion(ques)
              print(newQ.objs[newQ.pos], ques.objs[1 - ques.pos])
              if(newQ.objs[newQ.pos] == ques.objs[1 - ques.pos]):
                questions.pop(quesIdx)
                for person in res:
                  ques.objs[1 - ques.pos] = person
                  printSingleQuestion(ques)
                  # ques.pos = newQ.pos
                  subRes = solveSingleQuestion(rules, facts, ques, questions)
                  if(len(subRes) > 0):
                    return subRes
            result = common_member(result, res)
        elif(rules[kbI].opr[k - 1] == 0): # OR
          if(q.pos == -1): # Câu hỏi YES-NO
            result = result or res
          else: # Câu hỏi WHO
              result.extend(res)
  return result

# Câu hỏi liên quan đến Facts
# YES - NO
fq1 = SingleQuestion("Male", ["Tac"], -1) # True
fq3 = SingleQuestion("Female", ["Huong"], -1) # True
# WHO?
fq2 = SingleQuestion("Female", ["X"], 0) # ['Giang', 'Trinh', 'Huong', 'Xanh']
fq4 = SingleQuestion("Male", ["X"], 0) #['Tra', 'L', 'Tu', 'Tac']
fq5 = SingleQuestion("Parent", ["Huong", "X"], 1) # ['Tra', 'Giang', 'Trinh']
fq6 = SingleQuestion("Parent", ["X", "Tra"], 0) # ['L', 'Huong']

# Câu hỏi liên quan đến Rules
# YES - NO
rq = SingleQuestion("Father", ["L", "Tra"], -1) # True
rq1 = SingleQuestion("Mother", ["Huong", "Tra"], -1) # True
rq2 = SingleQuestion("Married", ["L", "Huong"], -1) # True
rq3 = SingleQuestion("GrandFather", ["Tac", "Tra"], -1) # True
# WHO?
rq5 = SingleQuestion("GrandMother", ["Xanh", "Tra"], -1) # Huong
# rq6 = SingleQuestion("GrandMother", ["X", "Tra"], 1) # L
# rq6 = SingleQuestion("GrandFather", ["L", "Tra"], -1) # L

print(solveSingleQuestion(rules, facts, rq5, []))
# print(solveSingleQuestion(rules, facts, rq6, []))