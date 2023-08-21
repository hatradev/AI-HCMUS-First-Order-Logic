class KB:
    def __init__(self, name, objects, negative=False):
        self.name = name
        self.negative = negative
        self.objs = objects

    def xuat(self):
        print("KB: ", self.name, self.objs, self.negative)


class Fact(KB):
    def __init__(self, name, objects, negative=False):
        KB.__init__(self, name, objects, negative)

    def xuat(self):
        print(self.name, ": ", self.objs)
        print("\n")


class Rule(KB):
    def __init__(self, name, objects, kbs, operator, negative=False, isDistinct=False):
        KB.__init__(self, name, objects, negative)
        self.opr = operator
        self.kbs = kbs
        self.isDistinct = isDistinct

    def xuat(self):
        print(self.name, ": ", self.objs, self.opr)
        for kb in self.kbs:
            kb.xuat()
        print("\n")


class SingleQuestion:
    def __init__(self, name, objects, pos, canSolve=True, negative=False):
        self.name = name
        self.pos = pos  # -1 (True, False), 0, 1
        self.objs = objects
        self.canSolve = canSolve
        self.negative = negative

    def xuat(self):
        print(self.name, self.objs, self.pos, self.negative)


def splitFacts(line, isQ=False):
    first = line.split("(")
    if "" in first:
        first.remove("")
    if first[-1].endswith(")). "):
        first.extend(first[-1].split(")). "))
        first.pop(1)
        first.pop(-1)
    elif first[-1].endswith("))."):
        first.extend(first[-1].split("))."))
        first.pop(1)
        first.pop(-1)
    elif first[-1].endswith(")."):
        first.extend(first[-1].split(")."))
        first.pop(1)
        first.pop(-1)
    elif first[-1].endswith(") "):
        first.extend(first[-1].split(") "))
        first.pop(-1)
    elif first[-1].endswith(")) "):
        first.extend(first[-1].split(")) "))
        first.pop(1)
        first.pop(-1)
    elif first[-1].endswith("."):
        first.extend(first[-1].split("."))
        first.pop(1)
        first.pop(-1)
    if first[-1].endswith(")"):
        first.extend(first[-1].split(")"))
        first.pop(1)
        first.pop(-1)

    if not isQ and first[-1].endswith("'") and first[-1].find("', '") != -1:
        first[-1] = first[-1][1:-2] if first[-1].endswith(")'") else first[-1][1:-1]
        first[-1] = first[-1].replace("', '", "><")
    elif (not (first[-1].startswith("'") and first[-1].endswith("'"))) or isQ:
        first[-1] = first[-1].replace(", ", "><")

    first.extend(first[-1].split("><"))
    first.pop(1)
    return first


def splitRules(first, it, index):
    if first[index].find("), (") != -1:
        temp = first[index].split("), (")
        first.extend(temp)
        first.pop(index)
        it.extend([1] * (len(temp) - 1))
        first.reverse()
        return True

    if first[index].find("); (") != -1:
        temp = first[index].split("); (")
        first.extend(temp)
        first.pop(index)
        first.reverse()
        it.extend([1] * (len(temp) - 1))
        return True

    if first[index].find(")); ") != -1:
        temp = first[index].split("); ")
        first.extend(temp)
        first.pop(index)
        first.reverse()
        it.extend([0] * (len(temp) - 1))
        return True

    if first[index].find("), ") != -1:
        temp = first[index].split("), ")
        first.extend(temp)
        first.pop(index)
        if len(it) > 1:
            it.extend([1] * (len(temp) - 1))
            # print("ok")
            first.reverse()
            it.reverse()
        else:
            it.extend([1] * (len(temp) - 1))
        return True

    if first[index].find("); ") != -1:
        temp = first[index].split("); ")
        first.extend(temp)
        first.pop(index)
        it.extend([0] * (len(temp) - 1))
        if len(it) > 1:
            first.reverse()
            it.reverse()
        return True

    if first[index].find(" \\== ") != -1:
        tmp = first[index].split(" \\== ")
        app = "\\==" + "("
        for i in tmp:
            app = app + i + ", "
        app = app[:-2]
        first.append(app)
        first.pop(index)

    if first[index].find(" > ") != -1:
        tmp = first[index].split(" > ")
        app = ">" + "("
        for i in tmp:
            app = app + i + ", "
        app = app[:-2]
        first.append(app)
        first.pop(index)
    return False


def readFactsAndRules(filename):
    f = open(filename, "r")
    datalist = f.readlines()
    facts = []
    rules = []
    for line in datalist:
        if line.startswith("/*") or line == "" or line == "\n":
            continue
        if line.find(":-") == -1:
            # facts
            first = splitFacts(line[:-1])
            for i in range(len(first)):
                if first[i].startswith("'"):
                    first[i] = first[i][1:]
                if first[i].endswith("'"):
                    first[i] = first[i][:-1]
            facts.append(Fact(first[0], first[1:]))
        else:
            # rules
            first = line.split(":- ")
            head = splitFacts(first[0])
            head.pop(1)
            first.pop(0)
            first[-1] = first[-1][:-1]
            it = []

            flag = True
            while flag:
                for idx in range(len(first)):
                    if idx == 0:
                        flag = splitRules(first, it, idx)
                    else:
                        flag = flag or splitRules(first, it, idx)
            kbs = []
            for kb_item in first:
                item = splitFacts(kb_item)
                negative = False
                if "~" in item[0]:
                    negative = True
                    item[0] = item[0].replace("~", "")
                if ">" in item[0]:
                    if item[2] == "2":
                        kbs[-1].objs[1] = "3"
                        it.pop()
                        continue
                    elif item[2] == "1":
                        kbs[-1].objs[1] = "2"
                        item = [kbs[-1].name, kbs[-1].objs[0], "3"]
                        it.pop()
                        it.append(0)
                kbs.append(KB(item[0], item[1:], negative))
            rules.append(Rule(head[0], head[1:], kbs, it))
    return facts, rules


def readQuestions(filename):
    f = open(filename, "r")
    datalist = f.readlines()
    questions = []
    q = -1
    for line in datalist:
        if line.startswith("/*") or line == "" or line == "\n":
            continue
        if line.startswith("?- "):
            first = splitFacts(line[3:-1], True)
            for i in range(len(first)):
                if first[i].find("'") != -1:
                    first[i] = first[i][1:-1]
                else:
                    q = i - 1 if i != 0 else -1
            questions.append(SingleQuestion(first[0], first[1:], q))
    return questions


def writeAnswers(filename, answers):
    f = open(filename, "w")
    for ans in answers:
        if ans[1] == -1:
            f.write(str(ans[0][1]) + "\n")
        else:
            output = ans[0][0] + " = "
            for res in ans[0][1]:
                output += res + ", "
            output = output[:-2]
            output += "\n"
            f.write(output)
