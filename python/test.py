def solution(players, callings):
    answer = []
    award={}  # 등수:이름
    names={}  # 이름:등수
    for i in range(len(players)):
        award[i]=players[i]
        names[players[i]]=i
    for i in callings:
        award[names[i]],award[names[i]-1],names[i],names[award[names[i]-1]]=award[names[i]-1],award[names[i]],names[award[names[i]-1]],names[i]
    for i in range(len(players)):
        answer.append(award[i])
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))