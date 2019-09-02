
############ Scope one algorithm
from data import deviatedData

class slopeOneAlgo:

  def __init__(self,devData):
    self.devData = deviatedData

  def getDeviation(self,b1,b2):
    band=[b1,b2]
    cardDnom,counter,nU,ratedUser=0,0,0,[]
    for user in self.devData:
      for key in self.devData[user].keys():
        if key in band:
          counter += 1
      if counter ==2 :
        cardDnom += 1
        ratedUser.append(user)
        counter=0
      else:
        counter=0
    
    for user in ratedUser:
      n1 = (self.devData[user][band[0]] - self.devData[user][band[1]])
      nU += n1/cardDnom
    return (nU,cardDnom)

  artist = ['Taylor Swift','PSY','Whitney Houston','Foo Fighter']

  def getAllDeviation(self):
    data = self.artist
    devDict={}
    for single in data:
      tempDict={}
      for user in data:
        if single != user :
          tempDict[user] = self.getDeviation(single,user)
      devDict[single]=tempDict
    return devDict

  # print(allDeviation)

  def recommendation(self,user):
    allDeviation = self.getAllDeviation()
    # print(allDeviation)
    userBands = self.devData[user]
    recommend={}
    n,d=0,0
    for artist in userBands:
      for diffArtis in allDeviation[artist]:
        if diffArtis not in  userBands.keys():
          rating = userBands[artist]
          deviation = allDeviation[diffArtis]
          # print(deviation)
          artistDeviation = deviation[artist][0]
          cRb = deviation[artist][1]
          n1 = (rating + artistDeviation) * cRb
          n += n1
          d += cRb
          recommend[diffArtis]=n/d
    
    recommend = list(recommend.items())
    recommend.sort(key=lambda artistTuple : artistTuple[1], reverse=True)
    return recommend

# print(slopeOne("Ben"))
# r = slopeOneAlgo(deviatedData)
# r.getAllDeviation()
# print(r.recommendation('Ben'))




