from flask import Flask, render_template, Response
from WrapperClass import WrapperClass

from DependencyContainer import DependencyContainer
from dependency_injector.wiring import inject, Provide

app = Flask(__name__,
            template_folder="")

@app.route("/")
def loadHomePage():
  return render_template("index.html")


# Reference: https://python-dependency-injector.ets-labs.org/introduction/index.html
#            https://pypi.org/project/dependency-injector/
@app.route("/api/tester")
@inject
def testDependencyInjection(wrapperObj = Provide[DependencyContainer.wrapperObj]):
   response = Response(wrapperObj.runTask())
   response.headers['Access-Control-Allow-Origin'] = "*"
   return response