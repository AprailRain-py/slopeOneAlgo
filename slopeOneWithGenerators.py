import csv

class slopeOneRecommendation:
    def __init__(self):
        self.devData = self.loadRatingData('ratingsOld.csv')
        self.artist = self.loadMovieData2('moviesOld.csv')

    def getDeviation(self, b1, b2):
        band = [b1, b2]
        cardDnom, counter, nU, ratedUser = 0, 0, 0, []
        # print(self.devData[1])
        for user in self.devData:
            for key in self.devData[user].keys():
                if key in band:
                    counter += 1
            if counter == 2:
                #calculating number of users rated both bands and the user name
                cardDnom += 1
                ratedUser.append(user)
                counter = 0
                break
            else:
                counter = 0
        #subtracting every users rating of both band dvided by no. of users rated both bands and summing all of them
        for user in ratedUser:
            n1 = (self.devData[user][band[0]] - self.devData[user][band[1]])
            nU += n1 / cardDnom
        return (nU, cardDnom)

    def getAllDeviation(self):
        data = self.artist.keys()
        # print(data)
        devDict = {}
        for single in data:
            tempDict = {}
            for user in data:
                if single != user:
                    tempDict[user] = self.getDeviation(single, user)
                    # tempDict[user] = self.getDeviation(single[1],user[1])
            devDict[single] = tempDict
        return devDict

    def loadRatingData(self, path):
        f = open(path, newline='')
        ratings = csv.reader(f, delimiter=',')
        next(ratings)
        movieRating, tRating, userId = {}, {}, 0
        for i in ratings:
            if userId == 0:
                userId = i[0]
                movieRating[i[1]] = float(i[2])
            else:
                if userId == i[0]:
                    movieRating[i[1]] = float(i[2])
                else:
                    tRating[int(userId)] = movieRating
                    userId = i[0]
                    movieRating = {}
                    movieRating[i[1]] = float(i[2])
        return tRating

    def loadMovieData(self, path):
        f = open(path, newline='')
        movies = csv.reader(f, delimiter=',')
        moviesList = []
        for i in movies:
            if i[0] != 'movieId':
                moviesList.append(i[0])
                # moviesList.append((i[0],i[1]) )
        return moviesList

    def loadMovieData2(self, path):
        f = open(path, newline='', encoding='utf8')
        movies = csv.reader(f, delimiter=',')
        moviesList = {}
        for i in movies:
            if i[0] != 'movieId':
                moviesList[i[0]] = i[1]
                # moviesList.append((i[0],i[1]) )
        return moviesList

    def recommender(self, user):
        allDeviation = self.getAllDeviation()
        # print(allDeviation)
        # print(allDeviation)
        userBands = self.devData[user]
        recommend = {}
        n, d = 0, 0
        for artist in userBands:
            for diffArtis in allDeviation[artist]:
                if diffArtis not in userBands.keys():
                    rating = userBands[artist]
                    deviation = allDeviation[diffArtis]
                    # print(deviation)
                    artistDeviation = deviation[artist][0]
                    cRb = deviation[artist][1]
                    n1 = (rating + artistDeviation) * cRb
                    n += n1
                    d += cRb
                    recommend[diffArtis] = round(n / d, 2)

        recommend = list(recommend.items())

        recommend = [(self.artist[n], r) for (n, r) in recommend]

        recommend.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return recommend
