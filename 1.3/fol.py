from file import *


def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


def allObjects(facts):
    rt = []
    for i in range(len(facts)):
        for obj in facts[i].objs:
            if obj not in rt and not containsNumber(obj):
                rt.append(obj)
    return rt


def findinRules(rules, q: SingleQuestion):
    rt = []
    for i in range(len(rules)):
        if q.name == rules[i].name:
            rt.append(i)
    return rt


def findinFacts(facts, q: SingleQuestion):
    rt = []
    if q.name == "\\==":
        rt.append(-1)
        return rt
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
            if i == -1:
                for f in facts:
                    if (
                        len(f.objs) == 1
                        and f.objs[0] != q.objs[k - q.pos]
                        and f.objs[0] not in res
                    ):
                        res.append(f.objs[0])
            elif facts[i].objs[k - q.pos] == q.objs[k - q.pos] or not k:
                res.append(facts[i].objs[q.pos])
        return res


def solveFactNegative(kbsIndex, facts, q: SingleQuestion):
    if q.pos == -1:
        for i in kbsIndex:
            if q.objs == facts[i].objs:
                return False
        return True
    else:
        object_list = allObjects(facts)
        k = len(q.objs) - 1
        for i in kbsIndex:
            if facts[i].objs[k - q.pos] == q.objs[k - q.pos] or not k:
                object_list.remove(facts[i].objs[k - q.pos])
        return object_list


def common_member(a, b):
    result = [i for i in a if i in b]
    return result


def newQuestion(kbInRule, ruleObjs, varPos, qObjs):
    idx = -1

    newVar = []  # 0 là hằng, 1 là biến
    newObjs = []

    for i in range(len(kbInRule.objs)):
        # Tìm vị trí tương ứng của obj đó trong kb lớn
        try:
            idx = ruleObjs.index(kbInRule.objs[i])
        except ValueError:
            idx = -1

        if idx != -1:  # Nếu tìm được thì lưu vào newObjs
            newObjs.append(qObjs[idx])
            newVar.append(2 if varPos == idx else 0)
        else:  # Nếu k tìm được thì đó là biến trung gian
            newObjs.append(kbInRule.objs[i])
            newVar.append(1)

    canSolve = True
    pos = -2
    if sum(newVar) == 1:
        pos = newVar.index(1)
    elif sum(newVar) == 0:
        pos = -1
    else:
        pos = newVar.index(2)
        if sum(newVar) > 2:
            canSolve = False
    return SingleQuestion(kbInRule.name, newObjs, pos, canSolve, kbInRule.negative)


def solveStackQuestions(
    rules, facts, result, questions: [SingleQuestion], qIndex, operator
):
    idx = -1
    rt = []

    for a in range(len(result)):
        ans = result[a]
        if (
            ans != None
            and ans[0] != "T/F"
            and ans[0] == questions[qIndex].objs[1 - questions[qIndex].pos]
        ):
            if len(ans[1]) <= 0:
                if operator[a - 1 if a >= len(result) - 1 else a] == 1:
                    return questions[qIndex].objs[questions[qIndex].pos], ans[1]
            else:
                # Tìm xem question qIndex có giải được không
                try:
                    idx = questions[qIndex].objs.index(ans[0])
                except ValueError:
                    idx = -1

                if idx != -1:
                    oldQ = questions[qIndex]
                    for value in ans[1]:
                        oldQ.objs[idx] = value
                        oldQ.canSolve = True
                        rt.append((solveSingleQuestion(rules, facts, oldQ, [])))
                    break

    if idx == -1:
        return None

    rt = combineResult(
        rt, [0] * (len(rt) - 1), questions[qIndex].objs[questions[qIndex].pos]
    )

    return rt[0][0], rt[0][1]


def combineOne(op, ans, expect):
    if ans[0][0] == expect:
        idx = 0
    else:
        idx = 1

    convertTF = []
    convertList = []

    for a in ans:
        if (a[0] == "T/F" and a[1] == False) or (a[0] != "T/F" and len(a[1]) == 0):
            convertTF.append(False)
            convertList.append([])
        else:
            convertTF.append(True)
            convertList.append(ans[idx][1] if a[0] == "T/F" else a[1])

    if op == 1:  # and
        if ans[idx][0] == "T/F":
            return (
                "T/F",
                ans[idx][1]
                and (
                    ans[1 - idx][1] if ans[1 - idx][0] == "T/F" else convertTF[1 - idx]
                ),
            )
        elif ans[1 - idx][0] != "T/F" and ans[1 - idx][0] != ans[idx][0]:
            return ans[idx]
        else:
            return (
                ans[idx][0],
                common_member(
                    ans[idx][1],
                    ans[1 - idx][1]
                    if ans[1 - idx][0] != "T/F"
                    else convertList[1 - idx],
                ),
            )
    else:  # or
        if ans[idx][0] == "T/F":
            return (
                "T/F",
                ans[idx][1]
                or (
                    ans[1 - idx][1] if ans[1 - idx][0] == "T/F" else convertTF[1 - idx]
                ),
            )
        elif ans[1 - idx][0] == "T/F":
            return ans[idx]
        else:
            tmp = []
            tmp.extend(ans[0][1])
            tmp.extend(ans[1][1])
            return (
                ans[idx][0],
                list(dict.fromkeys(tmp)) if ans[0][0] == ans[1][0] else ans[idx][1],
            )


def combineResult(result, operator, expect):
    rt = []
    rt.append(result[0])
    for j in range(1, len(result)):
        if result[j] == None:
            continue
        rt[0] = combineOne(operator[j - 1], [rt[0], result[j]], expect)

    if expect == "T/F" and type(rt[0][1]) == list:
        if len(rt[0][1]) == 0:
            return [(expect, False)]
        else:
            return [(expect, True)]
    return rt


def solveSingleQuestion(
    rules, facts, q: SingleQuestion, questions: [SingleQuestion] = []
):
    kbsIndex = findinRules(rules, q)
    if len(kbsIndex) == 0:  # Facts
        kbsIndex = findinFacts(facts, q)
        if q.negative == False:
            return q.objs[q.pos] if q.pos != -1 else "T/F", solveFact(
                kbsIndex, facts, q
            )
        else:
            return q.objs[q.pos] if q.pos != -1 else "T/F", solveFactNegative(
                kbsIndex, facts, q
            )

    # Rules
    final_result = [None] * len(kbsIndex)

    for kbI in kbsIndex:  # duyệt trong rules
        result = [None] * len(rules[kbI].kbs)
        questions = [None] * len(rules[kbI].kbs)
        # Duyệt qua từng kb nhỏ trong kbs lớn
        for k in range(len(rules[kbI].kbs)):
            kb = rules[kbI].kbs[k]

            # tạo câu hỏi mới
            newQ = newQuestion(kb, rules[kbI].objs, q.pos, q.objs)

            if newQ.canSolve == False:  # Không giải được ngay
                questions[k] = newQ
                continue
            else:
                key, res = solveSingleQuestion(rules, facts, newQ, questions)
                if newQ.pos != -1:
                    result[k] = (key, res)
                else:
                    result[k] = (key, res)
        i = 0
        while None in result:
            if questions[i] != None:
                result[i] = solveStackQuestions(
                    rules, facts, result, questions, i, rules[kbI].opr
                )
            i = (i + 1) % len(result)

        result = combineResult(
            result, rules[kbI].opr, q.objs[q.pos] if q.pos != -1 else "T/F"
        )

        return result[0][0], result[0][1]


# Đọc input file
choice = int(input("Choose input file (1. british-family.txt, 2. company.txt): "))
if choice == 1:
    facts, rules = readFactsAndRules("british-family.txt")
    questions = readQuestions("british-family-queries.txt")
elif choice == 2:
    facts, rules = readFactsAndRules("company.txt")
    questions = readQuestions("company-queries.txt")

# Trả lời
answers = []
for i in range(len(questions)):
    answers.append([solveSingleQuestion(rules, facts, questions[i]), questions[i].pos])
writeAnswers("answer.txt", answers)
print("All questions are answered in answer.txt")
