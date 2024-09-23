from flask import Flask, jsonify, render_template

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}]
#we ca also use API and get the data from it and then pass it to the html page and we  can use json


@app.route("/jobs")
def list_jobs():
    return jsonify(
        JOBS
    )  #we send the data in json format and insted of using render_template we use jsonify and differenciate htmlpages and non html pages we often use api name infront of it. it bassically means url which  don't return html in the broweser but it return stuctured data in json format which can then ananlyzed and now we have made api route and now we wiil deploy it in render.com.


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
