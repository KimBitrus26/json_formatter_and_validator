from app import db, ma

#user model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    
    #constructor
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
       
 
class UserSchema(ma.Schema):
    class Meta:
        model = User

        sqla_session = db.session
    
        fields = ('id','username','email','password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
   

         
#programmatic creating database
db.create_all()
