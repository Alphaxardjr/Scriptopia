from flask import Flask,request #request for passing data when making requests
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource,reqparse,abort

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
    # db.create_all()


# using requstparser from restful to define arguments
artists_put_args = reqparse.RequestParser()
artists_put_args.add_argument("name",type=str,help = "Name of the artist is required",required= True)
artists_put_args.add_argument("views",type=int,help = "views of the artist is required",required= True)
artists_put_args.add_argument("likes",type=int,help = "likes of the artist is required",required= True)
artists = {
    "kiba":{"gender":"male","music":"utu"},
    "diamondi":{"gender":"male","music":"nesanesa"},
    "zuchi":{"gender":"female","music":"siji"}
}

def abort_if_name_not_found(name):
    if name not in artists:
        # abort function aborts the request and return the specified message
        abort(404,message="The name is not valid")

def abort_if_name_already_exists(name):
    if name in artists:
        abort(409,message= "The name is already exist")
  
class Artist(Resource):
    def get(self,name):
        # abort if before returning
        abort_if_name_not_found(name)
        # make sure the response is json serioulizable
        return artists[name]
    def put(self,name):
        # print(request.form) #there is a better way of using reqparse
        abort_if_name_already_exists(name)
        args = artists_put_args.parse_args()
        artists[name]= args
        return artists[name],201 # status code for created resources

    def delete(self,name):
        abort_if_name_not_found(name)
        del artists[name]
        return '',204
    
api.add_resource(Artist,"/artists/<string:name>")
@app.route("/")
def index():
    return "Hello flask"

if __name__ == "__main__":
    app.run(debug = True)