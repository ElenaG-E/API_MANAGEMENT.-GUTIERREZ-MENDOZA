class Todo():
    def __init__(self, userId=0, id=0, title='', completed=True):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed