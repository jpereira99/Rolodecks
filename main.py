from flask import Flask, render_template, request
import backend

app = Flask(__name__)

#homepage
@app.route("/")
def home():
    return render_template("main.html")

##AUTH##
#login
@app.route("/login")
def login():
    return render_template("login.html")
#signup
@app.route("/signup")
def signup():
    return render_template("signup.html")

##PROFILE##
#Private Profile
@app.route("/profile")
def profilePrivate():
    return render_template("profilePrivate.html")

#Public Profile
@app.route("/profile_<user>")
def profilePublic(user):
    return render_template("profilePublic.html", user=user)


##EXPLORE##
@app.route("/explore")
def explore():
    return render_template("explore.html")


##PAYLOADS##
#UserPayload
@app.route("/userUpload", methods=['POST'])
def payloadUsername():
    req_data = request.get_json()

    userID = req_data['uid']
    username = req_data['username']

    backend.usernameDB(userID, username)

    return '''Successfully submitted into database'''

#UserPayload
@app.route("/projUpload", methods=['POST'])
def payloadProject():
    req_data = request.get_json()

    userID = req_data['uid']
    identifier = req_data['identifier']
    name = req_data['name']
    desc = req_data['desc']
    imgurl = req_data['imgurl']

    backend.projectDB(userID, identifier, name, desc, imgurl)

    return '''Successfully submitted into database'''

#run web service
app.run(debug=True)
