from flask import Flask 			# importing Flask class from flask module
app = Flask(__name__)				# here flask is a constructor. With this we are creating an instance of flask class. 
									# This instance of flask is used to handle all the requests and responses
									# This flask constructor takes module name as the argument
									#__name__ is a special variable. It holds the name of the current python file
		
@app.route('/')						# the route() function of a flask class is a decorator.
									# this decorator tells which url should call the associated function
def home():				    		# here in this example - '/' url is associated with home() function
    return "Welcome to Flask!" 	    # this is returned as a response to the client

if __name__=='__main__':
	app.run()					    # run() method of the flask class runs the application
	# app.run("local host", 5000)	# here the application runs on the local host on the port 5000 