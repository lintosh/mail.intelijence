#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence ProtectiveRights please edit and use it with all the care you can give

#(@:App-Type): "Api (Restfull & RestLess)"

#(@:Language): "Python"

#(@:Language Compiler): "python 2.9"

#(@:Framework): "Flask"

#(@:Required-Modules): "Flask, Flask_restful, Flask_restless, Flask SQL Alchemy, Flask_MYSQL, Flask_Mail, Flask-WTF, Flask_Socket, Imaplib, python 2.9, email, html5lib, Jinja, Flask_Sijax, Flask_Admin, Flask_Login, **more to come**"

#wow if you are done with the above
#and
#you get it
#you are on the right track
#boom!!!!!!!! now lets start the job

#import the flask framework and all it's modules like the flask_restful and api's methods
#import all classes used in routing from the classes package/directory to access all api handlers



from flask import Flask,request,jsonify
from flask_restful import Resource, Api

# from classes import *
import classes


#Instantiate all classes and modules to start operation
#modules like flask and restful api
app=Flask(__name__)
api=Api(app)


#let the coding begin

class main(Resource):
	"""main class handles redirecting and all for main"""
	data=""
	def get(self,res):
		return {"response":res},201

	def put(self, res):
		self.data=request.form['name']
		return{res:self.data}
#add resources to the api and get routed
api.add_resource(main,'/<string:res>')#stack up the above class with this url and get bounded


#end of codes
#now start the engine and let the car start moving
#run flask here

if __name__ == '__main__':
	app.run(debug=True,port=9000)
		
