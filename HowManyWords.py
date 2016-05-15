def HowManyWords(s):
    answer = 0
    string = 'word'
    target = 0
    for i in xrange(0, len(s)):
        if s[i].lower() == string[target]:
            target += 1
            if target == 4:
                answer += 1
                target = 0

    return answer


print HowManyWords("awosdrd")
