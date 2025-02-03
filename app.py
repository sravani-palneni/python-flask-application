from flask import Flask, request, redirect, flash		# importing Flask class from flask module
from flask import render_template
import secrets
import os
from dotenv import load_dotenv
from model import db, EmployeeDetails
app = Flask(__name__)							# here flask is a constructor. With this we are creating an instance of flask class. 
												# This instance of flask is used to handle all the requests and responses
												# This flask constructor takes module name as the argument
												#__name__ is a special variable. It holds the name of the current python file


# Load environment variables from .env file
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")	# SQLALCHEMY_DATABASE_URI: The database URI to specify the database you want to establish a connection with.
																				# postgresql://username:password@host:port/database_name									
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False											    # A configuration to enable or disable tracking modifications of objects. 
																									# You set it to False to disable tracking and use less memory
db.init_app(app)

app.secret_key = os.getenv('SECRET_KEY')

@app.before_request
def create_table():
	db.create_all()

# Landing Page    
@app.route('/', methods=['GET', 'POST'])					# the route() function of a flask class is a decorator.
															# this decorator tells which url should call the associated function
def home():				    								# here in this example - '/' url is associated with home() function
    if request.method == 'GET':								
        return render_template('homepage.html') 			# this is returned as a response to the client							

# Performing a CREATE Operation on database
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createemp.html')  
    if request.method == 'POST':
        employee_id = request.form['employeeid']		# here Keys used in the request.form attribute are the values of 'name' attribute 
        name = request.form['name']						# in the associated html i.e., createemp.html form's input field.
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeDetails(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        #return "Employee added successfully"
        flash("Employee added successfully", 'success')
        return redirect(f'/retrieve/{employee_id}')
    
# Performing a RETRIEVE Operation on database
	# Retrieving all employee Information
@app.route('/retrieve')
def RetrieveEmployeeList():
    employees = EmployeeDetails.query.all()
    return render_template('showemplist.html',employees = employees)

# Retrieving particular employee Details
@app.route('/retrieve/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeDetails.query.filter_by(employee_id=id).first()
    if employee:
         return render_template('showemp.html', employee=employee)
    #return f"Employee with ID = {id} does not exist"
    flash(f"Employee with ID {id} does not exist", 'danger')
    return redirect(f'/empid')
	
# Performing a UPDATE Operation on database
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    employee = EmployeeDetails.query.filter_by(employee_id=id).first()
    if employee:
        if request.method == 'POST':
            db.session.delete(employee)
            db.session.commit()

            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeDetails(employee_id=id, name=name, age=age, position=position)

            db.session.add(employee)
            db.session.commit()
            flash("Employee Updated successfully", 'success')
            return redirect(f'/retrieve/{id}')
        return render_template('updateemp.html', employee=employee)  
    #return f"Employee with id = {id} Does not exist"
    flash(f"Employee with ID {id} does not exist", 'danger')
    return redirect(f'/empid')

# Performing a DELETE Operation on database
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    employee = EmployeeDetails.query.filter_by(employee_id=id).first()
    if request.method == 'GET':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            #return "Employee Deleted successfully"
            flash("Employee Deleted successfully", 'success')
            return redirect(f'/retrieve')
        flash(f"Employee with ID {id} does not exist", 'danger')
        return redirect(f'/empid')

# Getting the Emp Id from the User
@app.route('/empid', methods=['GET', 'POST'])																				
def employee():				    								
    if request.method == 'GET':								
        return render_template('employeeid.html')
    
if __name__=='__main__':
	app.run()					      # run() method of the flask class runs the application
	# app.run("local host", 5000)	  # here the application runs on the local host on the port 5000 