class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # make hashMap
        hashMap = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                hashMap[pattern].append(word)
        
        # BFS
        # 처음 Pop하고 시작하니까 1부터시작
        res = 1
        q = collections.deque([beginWord])
        visit = set(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                # base case
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in hashMap[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
                
                
        return 0
                