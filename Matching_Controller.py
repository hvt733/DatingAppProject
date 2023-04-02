import random
from database_controller import show_seen, counts, update_seen, show_liked, update_liked, update_matched

class Randomize:
    def __init__(self, user_id):
        count = counts()
        array = []
        for i in range(count):
            array.append(str(i + 1))
        self.__IdArray = array
        self.__user_id = user_id
        
        seens = show_seen()
        seen = seens[user_id - 1]
        self.__seenArray = seen[0].split(" ")
        
        likess = show_liked(self.__user_id)
        likes = likess[0]
        like = likes[0]
        self.__likes = like.split(" ")
    def returnInfo(self):
        return self.__IdArray, self.__seenArray
    def getMultiRandom(self):
        a = []
        for i in self.__seenArray:
            try:
                self.__IdArray.remove(i)
            except ValueError:
                pass
        for j in self.__IdArray:
            a.append(j)
        
        if len(a) == 0:
            return self.__user_id    
        
        print(a)
        x = random.choice(a)
        self.__seenArray.append(x)
        update_seen((' '.join([str(elem) for elem in self.__seenArray])), self.__user_id)
        return x
    def setLike(self, i):
        self.__likes.append(i)
        print(self.__likes)
        update_liked(' '.join([str(elem) for elem in self.__likes]), self.__user_id)
        

class Match:
    def __init__(self, user_id):
        self.__user_id = user_id

        likess = show_liked(self.__user_id)
        likes = likess[0]
        like = likes[0]
        self.__likes = like.split(" ")
        self.__match = []
    def isMatch(self):
        for i in self.__likes:
            try:
                likess = show_liked(int(i))
                likes = likess[0]
                like = likes[0]
                liked = like.split(" ")
                if str(self.__user_id) in liked:
                    self.__match.append(i)
            except ValueError:
                pass
        update_matched(' '.join([str(elem) for elem in self.__match]), self.__user_id)