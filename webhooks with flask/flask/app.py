from flask import Flask,request #request for passing data when making requests
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource,reqparse,abort

app = Flask(__name__)
api = Api(app)

# using requstparser from restful to define arguments
artists_put_args = reqparse.RequestParser()
artists_put_args.add_argument("name",type=str,help = "Name of the artist is required",required= True)
artists_put_args.add_argument("views",type=int,help = "views of the artist is required",required= True)
artists_put_args.add_argument("likes",type=int,help = "likes of the artist is required",required= True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
# db = SQLALchemy(app)
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
        args = artists_put_args.parse_args()
        artists[name]= args
        return artists[name],201 # status code for created resources

    def delete(self,name):
        return artists[name]
    
api.add_resource(Artist,"/artists/<string:name>")
@app.route("/")
def index():
    return "Hello flask"

if __name__ == "__main__":
    app.run(debug = True)