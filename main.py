from flask import Flask,render_template,jsonify
app = Flask(__name__)
app.debug=True

@app.route('/',methods=['POST','GET'])
def main():
	return render_template('index.html')

@app.route('/test',methods=['POST','GET'])
def test():
		response={"name":"zya"}
		return jsonify(response),200


if __name__ == '__main__' :
	app.run(debug=True)