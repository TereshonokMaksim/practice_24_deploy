from project.settings import DB

class Product(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String,nullable = False)
    
    def __repr__(self) -> str:
        return f'product - {self.id}'