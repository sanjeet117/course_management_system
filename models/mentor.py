from models.user import User


class Mentor(User):

    def __init__(self, user_id, name, email, mentor_id, expertise):
        super().__init__(user_id, name, email)

        self.mentor_id = mentor_id
        self.expertise = expertise

    def display_profile(self):
        print("\n------ Mentor Profile ------")
        print(f"Mentor ID  : {self.mentor_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Expertise  : {self.expertise}")

        