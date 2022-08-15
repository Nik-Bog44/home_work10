class Candidate:
    def __init__(self, pk, name, position, picture, skills):
        self.pk = pk
        self.name = name
        self.position = position
        self.picture = picture
        self.skills = skills

    def __repr__(self):
        return f"{self.name},\n {self.position},\n {self.skills}"
