from flask import Flask, render_template, Response
from WrapperClass import WrapperClass

from DependencyContainer import DependencyContainer
from dependency_injector.wiring import inject, Provide
import sys

app = Flask(__name__,
            template_folder="")

@app.route("/")
def loadHomePage():
  return render_template("index.html")

@inject
@app.route("/api/tester")
def testDependencyInjection(wrapperObj = Provide[DependencyContainer.wrapperObj].provider()):
   response = Response(wrapperObj.runTask())
   response.headers['Access-Control-Allow-Origin'] = "*"
   return response

if __name__ == "__main__":
  # dependencyContainer = DependencyContainer()
  # dependencyContainer.wire(modules=[sys.modules[__name__]])
  app.run(host="0.0.0.0", debug=True)