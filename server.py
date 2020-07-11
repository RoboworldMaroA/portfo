# from flask import Flask, render_template
# app = Flask(__name__)



# @app.route('/')
# def main_web():
#     return render_template('./index.html')

# @app.route('/index.html')
# def index():
#     return render_template('./index.html')

# @app.route('/about_me.html')
# def about_me():
#     return render_template('./about_me.html')


# @app.route('/mobile_robots.html')
# def mobule_robots():
#     return render_template('./mobile_robots.html')

# @app.route('/web_design.html')
# def web_design():
#     return render_template('./web_design.html')






# # @app.route('/')
# # def hello_world():
# #     return 'maro a'

########## this above is work well #############

#
#
#
#
#

##### this below is action on wesbite #####

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


# enything what i put into the username going to function main_web


@app.route('/') 
def home(username=None, post_id=None):
    return render_template('index.html', name=username)

@app.route('/index.html') 
def index(username=None, post_id=None):
    return render_template('index.html', name=username)



#cos nie dokonca dziala css nie widzi ??? @app.route('//<username>/<int:post_id>') # enything what i put into the username going to function main_web
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

# @app.route('/<username> ') # enything what i put into the username going to function main_web
# def main_web(username=None):
#     return render_template('./index.html', name=username)

# @app.route('/index.html')
# def index():
#     return render_template('./index.html')

@app.route('/<string:page_name>') # when you use this then yhis is automaticki going to the page with this name you dont have to copy over and over new route
def html_page(page_name):
    return render_template(page_name)


#### this part is for write data to file as a list

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{name},{email},{subject},{message}')


#### this part is for write data to file as a CSV

def write_to_csv(data):
	with open('database.csv', mode='a', newline ='') as database2:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE) 
		csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data) # before was print(data) later was write_to file
			return redirect('/thank_you_contact.html')
		except:
			return 'did not save to database'
	else:
		return 'Something went wront Try again!'



# @app.route('/mobile_robots.html')
# def mobule_robots():
#     return render_template('./mobile_robots.html')

# @app.route('/web_design.html')
# def web_design():
#     return render_template('./web_design.html')	


# ##### to ponizsze dzial dodawanie pojedynczych wybranych nazw z dictionarry
####### ale powyzej jest inna wercja podana z video tutoriala
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	if request.method == 'POST':
# 		data = request.form.to_dict()
# 		print(data)
# 		get_name = data.get("name")
# 		get_email = data.get("email")
# 		f = open("database.txt", "a")
# 		f.write(get_name)
# 		f.write(get_email)
# 		f.close()
# 		return redirect('/thank_you_contact.html')
# 	else:
# 		return 'Something went wront Try again!'


