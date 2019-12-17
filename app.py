from flask import Flask, url_for, render_template, request
from tensorflow import keras
import numpy as np

app = Flask(__name__)
data = keras.datasets.reuters
word_index = data.get_word_index()
model = keras.models.load_model('/users/programming/Desktop/student-grade.h5')
data = keras.datasets.reuters

def review_encode(s):
	encoded = [1]

	for word in s:
		if word.lower() in word_index:
			encoded.append(word_index[word.lower()])
		else:
			encoded.append(2)

	return encoded


@app.route("/")
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')

def review_encode(s):
    encoded = [1]

    for word in s:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)

    return encoded

    # print(review_encode(["Enjoyed"]))
@app.route('/', methods = ["POST"])
def predict():
    namequery = request.form['namequery']
    namequery2 = request.form['namequery2']
    namequery3 = request.form['namequery3']
    namequery4 = request.form['namequery4']
    namequery5 = request.form['namequery5']
    namequery6 = request.form['namequery6']
    namequery7 = request.form['namequery7']
    namequery8 = request.form['namequery8']
    namequery9 = request.form['namequery9']
    namequery10 = request.form['namequery10']
    if namequery.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery2.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery3.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery4.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery5.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery6.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery7.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery8.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery9.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if namequery10.isdigit() == False:
        return render_template('index.html', message='Please input a number.')
    if int(namequery) > 20:
        return render_template('index.html', message='Previous grades must be under 20.')
    if int(namequery2) > 20:
        return render_template('index.html', message='Previous grades must be under 20.')
    if int(namequery3) > 4:
        return render_template('index.html', message='Studytime must be under 4.')
    if int(namequery4) > 4:
        return render_template('index.html', message='Failures must be under 4.')
    if int(namequery5) > 93:
        return render_template('index.html', message='Absences must be under 93')
    if int(namequery6) > 1:
        return render_template('index.html', message='Must input 0 or 1')
    if int(namequery7) > 1:
        return render_template('index.html', message='Must input 0 or 1')
    if int(namequery8) > 1:
        return render_template('index.html', message='Must input 0 or 1')
    if int(namequery9) > 1:
        return render_template('index.html', message='Must input 0 or 1')
    if int(namequery6) > 1:
        return render_template('index.html', message='Must input 0 or 1')
    dataset = [int(namequery), int(namequery2), int(namequery3), int(namequery4), int(namequery5), int(namequery6), int(namequery7), int(namequery8), int(namequery9), int(namequery10)]
    dataset = np.asarray(dataset)
    prediction = model.predict([[dataset]])
    prediction = np.argmax(prediction)
    letter_grade = None
    if prediction >= 15:
        prediction = prediction + 1
    else:
        prediction = prediction + 2
    if prediction > 20:
        prediction = 20
    if prediction == 20:
        letter_grade = "Around A+ Range"
    elif prediction >= 18:
        letter_grade = "Around A Range"
    elif prediction >= 14:
        letter_grade = "Around B Range"
    elif prediction >= 10:
        letter_grade = "Around C Range"
    else:
        letter_grade = "C or lower"
    return render_template('result.html', variable=prediction, letter_pred=letter_grade)

if __name__ == "__main__":
    app.run(debug='true')