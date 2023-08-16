class kb:
    def __init__(self, name, objects, negative=False):
        self.name = name
        self.negative = negative
        self.objs = objects

    def xuat(self):
        print("kb: ", self.name, self.objs)


class Fact(kb):
    def __init__(self, name, objects, negative=False):
        kb.__init__(self, name, objects, negative)

    def xuat(self):
        print(self.name, ": ", self.objs)
        print("\n")


class Rule(kb):
    def __init__(self, name, objects, kbs, operator, negative=False, isDistinct=False):
        kb.__init__(self, name, objects, negative)
        self.opr = operator
        self.kbs = kbs
        self.isDistinct = isDistinct

    def xuat(self):
        print(self.name, ": ", self.objs, self.opr)
        for kb in self.kbs:
            kb.xuat()
        print("\n")


def splitFacts(line):
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

    if first[-1].endswith("'"):
        first[-1] = first[-1][1:-2]
        first[-1] = first[-1].replace("', '", "><")
    else:
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

    if first[index].find("), ") != -1:
        temp = first[index].split("), ")
        first.extend(temp)
        first.pop(index)
        if len(it) == 1:
            it.extend([1] * (len(temp) - 1))
            # print("ok")
            first.reverse()
            it.reverse()
        else:
            it.extend([1] * (len(temp) - 1))
        return True

    if first[index].find("); ") != -1:
        first.extend(first[index].split("); "))
        first.pop(index)
        it.extend([0])
        if len(it) == 2:
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
    return False


def readFactsAndRules(filename):
    f = open(filename, "r")
    datalist = f.readlines()
    facts = []
    rules = []
    cnt = 0
    for line in datalist:
        if line.startswith("/*") or line == "" or line == "\n":
            continue
        if line.find(":-") == -1:
            # facts
            first = splitFacts(line[:-1])
            facts.append(Fact(first[0], first[1:]))
            facts[-1].xuat()
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
                kbs.append(kb(item[0], item[1:]))
            rules.append(Rule(head[0], head[1:], kbs, it))
            rules[-1].xuat()
    return facts, rules


readFactsAndRules("BritishFamily.txt")
# print(splitFacts("(male(Person"))
# print(splitFacts("parent(Parent, Child"))
# print(splitFacts("divorced('Princess Diana', 'Prince Charles')."))
# print(splitFacts("male('James, Viscount Severn')."))
