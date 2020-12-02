from flask import Flask, render_template, Response
from DependencyContainer import DependencyContainer
import appRoutes
import config

from dependency_injector.wiring import inject, Provide
import sys

def buildApp():
  dependencyContainer = DependencyContainer()
  dependencyContainer.config.from_dict(config.config)

  dependencyContainer.wire(modules=[sys.modules[__name__], appRoutes])
  appRoutes.app.container = dependencyContainer
  return appRoutes.app

@inject
def runApp(app,
          appConfig = Provide[DependencyContainer.config.app]):
  debug = (appConfig["env"] == "dev")
  appRoutes.app.run(host=appConfig["host"], port=appConfig["port"], debug=debug)

if __name__ == "__main__":
  appRoutes.app = buildApp()
  runApp(appRoutes.app)