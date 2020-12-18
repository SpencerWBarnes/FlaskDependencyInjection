from flask import Flask, render_template, Response
from DependencyContainer import DependencyContainer
import appRoutes
import config

from dependency_injector.wiring import inject, Provide
import sys

def buildApp():
  dependencyContainer = DependencyContainer()
  dependencyContainer.config.from_dict(config.config)

  # List all modules containing an @inject decorator
  dependencyContainer.wire(modules=[sys.modules[__name__], appRoutes])
  # Adding the container to the app gives the tests access to the container
  appRoutes.app.container = dependencyContainer
  return appRoutes.app

# Decorator to inject something from a provider
@inject
def runApp(app,
          appConfig = Provide[DependencyContainer.config.app]):
  debug = (appConfig["env"] == "dev") # Example use of using the dict from config["app"]
  appConfig["port"] = 8080 # Example of how easy it is to overwrite a config at runtime
  
  appRoutes.app.run(host=appConfig["host"], port=appConfig["port"], debug=debug)

if __name__ == "__main__":
  appRoutes.app = buildApp()
  runApp(appRoutes.app)