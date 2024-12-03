# python-flask-application
Learning Python Flask Framework

Creating a Flask CRUD Application:

- CRUD Application 
	* The application that can perform CREATE/RETRIEVE/UPDATE/DELETE operations on the database

- PostgreSQL 
	* PostgreSQL is another Relational Database Management System similar to MySQL database Management System.
	* Like MySQL, in PostgreSQL also the data is stored in the form of tables and it uses SQL(Structured Query Language) queries to access and perform  various tasks on the database.

- Creating a basic flask application
	* Install Python 
		You can check if python is installed or not by opening command prompt and using the command python --version.
	* Install Visual Studio Code (We can use other IDEs such as PyCharm, Eclipse, etc)

	* Open Visual Studio Code and create a new project

	* Install flask
		Open terminal in Visual studio Code and use the command pip install flask
	
	* Basic flask application - filename -> app.py
	----------------------------------------------
		from flask import Flask 		# importing Flask class from flask module
		app = Flask(__name__)			# here flask is a constructor. With this we are creating an instance of flask class. 
							# This instance of flask is used to handle all the requests and responses
							# This flask constructor takes module name as the argument
							#__name__ is a special variable. It holds the name of the current python file
		
		@app.route('/')				# the route() function of a flask class is a decorator.
							# this decorator tells which url should call the associated function
		def home():				# here in this example - '/' url is associated with home() function
    			return "Welcome to Flask!" 	# this is returned as a response to the client

		if __name__=='__main__':
			app.run()			# run() method of the flask class runs the application
			# app.run("local host", 5000)	# here the application runs on the local host on the port 5000 
	----------------------------------------------
	
	* Running the flask application
		In the terminal of the visual studio code type the below command
			flask run  # the built in server runs on the localhost with the port no 5000
		
		Once this command is executed, an URL is given in the terminal
		Click on that URL or copy and paste that URL in the browser to see the output.

	* NOTE: The command "flask run" by default tries to find and execute code defined in app.py file. 
		In case if the file name is different, then the flask environment variable must be set with proper file name
			set FLAK_APP = <file_name.py>

	* Each function with a decorator is called microservice

- Connecting a Flask Application to PostgreSQL database
	* SQLAlchemy is used to connect PostgreSQL to a Flask application.
	* SQLAlchemy is an ORM - Objects Relational Mapper. It is written in Python.
	* It gives a way around to interact with PostgreSQL without using SQL statements.
	* It provides an extra layer on the top of SQL which allows us to use the database tables just like Python class Objects.
	* We have to just create a class object and SQLAlchemy will take care of the rest

- Install SQLAlchemy
	* pip install flask_sqlalchemy
		Execute this command in the VS Code terminal to install sqlalchemy
	* pip install psycopg2-binary
		pyscopg2 is a postgreSQL database adapter for python. So run this command also in the VS Code terminal

- Setting up PostgreSql:
	* Install postgreSQL.
	* In the windows search bar, search for SQL Shell
	* Terminal will be opened - I gave the details as below
		server - localhost (same as the one that are there in the brackets)
		database - postgres
		port - 5432
		username - postgres
		password - postgres 
	* Create a database called employee
		CREATE DATABASE employee;			
	* Some useful commands 					
		to see the list of databases - select datname from pg_database;
		to see list of tables in a database - \dt
		to drop a database - DROP database <database name>)
		to drop a table - DROP table <table name>
		to describe a table - \d <table name>
	* Change to employee database
		\c employee or \connect employee
	* Now we are in the new database that we created
	* connection details:
		Specify the below connection details in the app.py file as below (Configuring SQLAlchemy)

			app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/employee"										
			app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False											
			db.init_app(app)


			# SQLALCHEMY_DATABASE_URI: The database URI to specify the database you want to establish a connection with.
			# postgresql://username:password@host:port/database_name
			# A configuration to enable or disable tracking modifications of objects. 
			# You set it to False to disable tracking and use less memory.	


- Creating database tables in Flask Application
	* a model in a python class represents a table in the database. 
 	* It contains information regarding the table structure
	* In flask, all the database information and the models are stored in a separate file called model.py
	* A typical model file looks like this:
		
	-----------------------------------------------------------------------------------------------------		
		from flask_sqlalchemy import SQLAlchemy
 
		db = SQLAlchemy()
 
		class Model_name(db.Model):
   			 __tablename__ = 'table_name'
 
    			field1_name = db.Column(db.Field1Type, primary_key...)
    			field2_name = db.Column(db.Field2Type)
    			field3_name = db.Column(db.Field3Type)
 
    			def __init__(self, Field1_name,Field2_name,Field3_name):
      				self.field1_name = field1_name
        			self.field2_name = field2_name
        			self.field3_name = field3_name
 
    			def __repr__(self):
        			return f"<statement>"
	-----------------------------------------------------------------------------------------------------	
		from flask_sqlalchemy import SQLAlchemy

		db = SQLAlchemy()

		class EmployeeDetails(db.Model):
   		 __tablename__ = "emp_table"
    
    		employee_id = db.Column(db.Integer(), primary_key=True)
    		name = db.Column(db.String())
    		age = db.Column(db.Integer())
    		position = db.Column(db.String(80))

    		def __init__(self, employee_id, name, age, position):
        		self.employee_id = employee_id
        		self.name = name
        		self.age = age
        		self.position = position

    		def __repr__(self):
        		return f"{self.name}:{self.employee_id}"
	-----------------------------------------------------------------------------------------------------	
-Some Important Information:
	
	* By default, all the route decorators of flask application, accepts only the requests submitted in GET method.

	* All the URLs requested by - i. the browser
                                      ii. the query string and 	
						(A query string is the portion of a URL where data is passed to a web application and/or back-end database.
		                                 The query string is whatever follows the question mark sign ("?") Ex: example.com?arg1=value1&arg2=value2)
					         Ex: http://127.0.0.1:5000/retrieve?employee_id=123&name=Abc&age=30&position=Lead
				      iii. the form submitted without mentioning any method attribute always uses GET method

	* If we want the application to use other HTTP methods, we should explicitly mention them in 'methods' argument in the route decorator.
		@flask_object.route(URL, methods = ['GET', 'POST'] ) 
			-- Here, the provided URL, must handle all the requests submitted by GET and POST HTTP methods.
	
	* The HTTP method of the URL request, can be identified by the method attribute of request object.
		request.method - stores the request's HTTP method
		request.form - stores the data submitted by POST method, in the form of dictionary
		request.args - stores the data submitted by GET method, in the form of dictionary
	
	* The request object needs to be imported from flask module and it stores various details of the client request.
		from flask import request


 		(key->name attribute of the form input field, value->data submitted in the input field)



- Performing a CREATE Operation on database:
		
	In app.py file:
	---------------
	@app.route('/create', methods=['GET', 'POST'])
	def create():
    	if request.method == 'GET':
        	return render_template('createemp.html')		#for this render_template should be imported from flask module 

    	if request.method == 'POST':
       		employee_id = request.form['employeeid']		# here Keys used in the request.form attribute are the values of 'name' attribute 
        	name = request.form['name']				# in the associated html i.e., createemp.html form's input field.
        	age = request.form['age']
        	position = request.form['position']
        	employee = EmployeeDetails(employee_id=employee_id, name=name, age=age, position=position)
        	db.session.add(employee)
        	db.session.commit()
        return "Employee added successfully"
			
			Inside the view function, if the method is GET, then form is displayed and when the method is POST, if it is a POST request, then you will want to process the incoming data.

	createemp.html:
	---------------

	<body>
    		<b>Add New Employee</b>
    		<form action='' method = "POST">
        		<p><b>Employee ID</b> <input type = "integer" name = "employeeid" /></p>
        		<p><b>Name</b> <input type = "text" name = "name" /></p>
        		<p><b>Age </b><input type = "integer" name = "age" /></p>
        		<p><b>Position </b> <input type = "text" name = "position" /></p>
        		<p><input type = "submit" value = "Submit" /></p>
    		</form>
	</body>

- Performing a RETRIEVE Operation on database:
	
	* Retrieving all employee Information:

	In app.py file:
	---------------
	@app.route('/retrieve')
	
	def RetrieveEmployeeList():
    		employees = EmployeeDetails.query.all()
    	return render_template('showemplist.html',employees = employees)

	showemplist.html:
	-------------
	<body>
    		<h3> List of all the Employees </h3>
    		{% for employee in employees %}
    		<p> <b> Employee with <u>Id:{{employee.employee_id}} </u> is </b> </p>
    		<p><b>Name: </b> {{employee.name}} </p>
    		<p><b>Age: </b> {{employee.age}} </p>
    		<p><b>Position: </b>{{employee.position}}</p></br>
    		{% endfor %}
	</body>


	* Retrieving particular employee Details:
	
	In app.py file:
	---------------

	@app.route('/retrieve/<int:id>')
	def RetrieveSingleEmployee(id):
    	employee = EmployeeDetails.query.filter_by(employee_id=id).first()
    	
	if employee:
        	return render_template('showemp.html', employee = employee)
    	return f"Employee with id ={id} doesn't exist"


	showemp.html:
	---------------
	<body>
    		<p> <b> Information about the employee with  <u>Id:{{employee.employee_id}} </u> is </b> </p>
    		<p><b>Name: </b> {{employee.name}} </p>
    		<p><b>Age: </b> {{employee.age}} </p>
    		<p><b>Position: </b>{{employee.position}}</p>
	</body>

- Performing a UPDATE Operation on database:

	In app.py file:
	---------------
	
	@app.route('/update/<int:id>', methods=['GET', 'POST'])
	def update(id):
    		employee = EmployeeDetails.query.filter_by(employee_id=id).first()
    		if request.method == 'POST':
        		if employee:
            			db.session.delete(employee)
            			db.session.commit()

            			name = request.form['name']
            			age = request.form['age']
            			position = request.form['position']
            			employee = EmployeeDetails(employee_id=id, name=name, age=age, position=position)

            			db.session.add(employee)
            			db.session.commit()
            		return redirect(f'/retrieve/{id}')
        	return f"Employee with id = {id} Does nit exist"

    	return render_template('updateemp.html', employee=employee)
	
	updateemp.html:
	---------------
	<body>
    		<b>Update the Details of Employee</b>
    		<form action='' method = "POST">
    			<p><b>Name </b><input type = "text" name = "name" value="{{employee.name}}"/></p>
            		<p><b>Age </b><input type = "integer" name = "age"  value="{{employee.age}}"/></p>
            		<p><b>Position</b> <input type = "text" name = "position" value="{{employee.position}}"/></p>
            		<p><input type = "submit" value = "Submit" /></p>
		</form>
	</body>

- Performing a DELETE Operation on database:
	
	In app.py file:
	---------------
	@app.route('/delete/<int:id>', methods=['GET', 'POST'])
	def delete(id):
    		employee = EmployeeDetails.query.filter_by(employee_id=id).first()
    		if request.method == 'POST':
        		if employee:
            			db.session.delete(employee)
            			db.session.commit()
            			return "Employee Deleted successfully"
	
	
- Some Terminology:

	<form action="" method="post"> 
	
	here action -specifies the url where to send the form data when the form is submitted.
	
	methods - post/get - specifies the HTTP method to use when sending the form data.

	post method is used to send the data to the server to create or update a resource.	

	before request in flask - to run your code before each flask request, we can assign that function to before request method. 

	GET and POST method in a form:
	GET and POST are two efficient techniques that can send the data to the server.
	Difference between GET and POST are
		GET method adds the data to the URI while the POST methods appends the data to the body
		GET method is used for retrieving the data while the POST method is used for storing and updating the data.

	form tag is used for expressing the content of the form. The data filled in the forms is further processed.
	form tag has two attributes:
		i. Action: This attribute is used to specify the address of the program that handles the form content
		ii. Method: to specify GET or POST method
	
- Important Links that can be referred:
	https://www.askpython.com/python-modules/flask/flask-crud-application
	https://www.askpython.com/python-modules/flask/flask-postgresql -- Very useful
	https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask -- Very useful
	https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
