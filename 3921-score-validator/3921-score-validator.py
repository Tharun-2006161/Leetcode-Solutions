class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        
        score = 0
        counter = 0
        for i in range(len(events)):
            if events[i].isdigit():
                score += int(events[i])
            elif events[i] == "W":
                counter += 1
                if counter == 10:
                    break
            elif events[i] == "NB":
                score += 1
            elif events[i] == "WD":
                score += 1
        return [score,counter]