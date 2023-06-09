# importing Flask. Flask framework is used for developing web app using python.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("Home.html")

@app.route('/about/')
def About():
    return render_template("About.html")

@app.route('/asu/')
def ASU():
    return render_template("ASU.html")

@app.route('/food/')
def Food():
    return render_template("Food.html")

@app.route('/shopping/')
def Shopping():
    return render_template("Shopping.html")

@app.route('/housing/')
def Housing():
    return render_template("Housing.html")

@app.route('/transportation/')
def Transportation():
    return render_template("Transportation.html")

@app.route('/buycar/')
def BuyACar():
    return render_template("BuyACar.html")

@app.route('/insurance/')
def Insurance():
    return render_template("Insurance.html")

@app.route('/license/')
def License():
    return render_template("License.html")

@app.route('/finance/')
def Finance():
    return render_template("Finance.html")

@app.route('/tax/')
def Tax():
    return render_template("Tax.html")

@app.route('/creditcards/')
def Credit():
    return render_template("CreditCards.html")

@app.route('/contact/')
def Contact():
    return render_template("Contact.html")

@app.route("/thanks", methods=['POST'])
def Thanks():
    if request.method=='POST':
        email = request.form["email_name"]
        text = request.form["text_name"]
        print(email, text)
        return render_template("Thanks.html")


if __name__ == "__main__":
    app.run(debug = True)