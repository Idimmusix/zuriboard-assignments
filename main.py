class Student:
    # [assignmient] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
      self.name=name
      self.age=age
      self.tracks=tracks
      self.score=score

    def change_name(self, name):
      self.name = name

    #debug method
    def getName(self):
       return self.name

    def change_age(self, age):
      self.age=age

    #debug method
    def getAge(self):
      return self.age

    def get_score(self):
      return self.score

    def add_track(self, track):
      self.tracks.append(track)

    def getTracks(self):
      return self.tracks


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print('My name is ',Bob.getName(), ', I am ',Bob.getAge(),' years old, I scored ',Bob.get_score(), ' in my ',Bob.getTracks(),' tracks\n')
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print('My name is ',Bob.getName(), ', I am ',Bob.getAge(),' years old, I scored ',Bob.get_score(), ' in my ',Bob.getTracks(),' tracks\n')
#
