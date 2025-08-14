from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")#is a decorator
def my_home():
     return render_template("index.html")

@app.route("/<string:page_name>")#is a decorator
def html_page(page_name):
     return render_template(page_name)


# @app.route("/about.html")#is a decorator
# def about():
#      return render_template("about.html")

# @app.route("/contact.html")#is a decorator
# def contact():
#      return render_template("contact.html")

# @app.route("/works.html")#is a decorator
# def work():
#      return render_template("works.html")

def write_to_file(data):
     with open("./Web_development/database.txt", mode="a") as database:
          email = data["email"]
          subject = data["subject"]
          message = data["message"]
          file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
     with open("./Web_development/database.csv",newline='', mode="a") as database2:
          email = data["email"]
          subject = data["subject"]
          message = data["message"]
          csv_writer = csv.writer(database2, delimiter= ",", quotechar="|", quoting = csv.QUOTE_MINIMAL)
          csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     if request.method == "POST":
          try:
               data = request.form.to_dict()
               write_to_csv(data)
               return redirect("/thankyou.html")
          except:
               return "did not save to database"
     else:
         print("something went wrong")
     

if __name__ == "__main__":
    app.run(debug=True)


   #To enter in venv:
#    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#    .\venv\Scripts\Activate.ps1


#mirar esta pagina para templates buenos: https://html5up.net/