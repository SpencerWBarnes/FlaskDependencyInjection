from flask import Flask, render_template, Response
from WrapperClass import WrapperClass

app = Flask(__name__,
            template_folder="")

wrapperObj = WrapperClass()

@app.route("/")
def loadHomePage():
  return render_template("index.html")

@app.route("/api/tester")
def testDependencyInjection():
   response = Response(wrapperObj.runTask())
   return response

if __name__ == "__main__":
  app.run(debug=True)