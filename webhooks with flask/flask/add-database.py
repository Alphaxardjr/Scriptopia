from flask import Flask,request #request for passing data when making requests
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with

app = Flask(__name__)
api = Api(app)
# config the database url
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) # initalize db in the app

# define the models
class NameModel(db.Model):
    name = db.Column(db.String,primary_key = True)
    gender = db.Column(db.String(10),nullable= False)
    views = db.Column(db.Integer,nullable= False)
    likes = db.Column(db.Integer,nullable= False)

    def __repr__(self):
        return f" The artist {name} with vies {views} and {likes} likes"
# create a database
# with app.app_context():
#     db.create_all()


# using requstparser from restful to define arguments
artists_put_args = reqparse.RequestParser()
artists_put_args.add_argument("name",type=str,help = "Name of the artist is required",required= True)
artists_put_args.add_argument("views",type=int,help = "views of the artist is required",required= True)
artists_put_args.add_argument("likes",type=int,help = "likes of the artist is required",required= True)
artists_put_args.add_argument("gender",type=str,help = "Gender of the artist is required",required=True)

# creating a resource field so that it can be seriolized as json

resource_fieds = {
    "gender":fields.String,
    "name":fields.String,
    "views":fields.Integer,
    "likes":fields.Integer
}
 
class Artist(Resource):
    @marshal_with(resource_fieds)
    def get(self,name):
        result = NameModel.query.get(name= name)
        return result
    @marshal_with(resource_fieds)
    def put(self,name):
        args = artists_put_args.parse_args()
        artist = NameModel(name=args['name'],views = args['views'],likes = args['likes'],gender =args['gender'])

        # add and commit to db
        db.session.add(artist)
        db.session.commit()
        return artist,201 # status code for created resou

    # def delete(self,name):
    #     abort_if_name_not_found(name)
    #     del artists[name]
    #     return '',204
    
api.add_resource(Artist,"/artists/<string:name>")
@app.route("/")
def index():
    return "Hello flask"

if __name__ == "__main__":
    app.run(debug = True)