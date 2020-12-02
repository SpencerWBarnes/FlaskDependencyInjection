from flask import Flask, render_template, Response
from DependencyContainer import DependencyContainer

import appRoutes

def buildApp():
  dependencyContainer = DependencyContainer()
  dependencyContainer.wire(modules=[appRoutes])
  appRoutes.app.container = dependencyContainer
  return appRoutes.app

if __name__ == "__main__":
  appRoutes.app = buildApp()
  appRoutes.app.run(host="0.0.0.0", debug=True)