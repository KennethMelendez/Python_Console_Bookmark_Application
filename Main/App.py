from Controller.Controller import Controller
from View.View import View
from View.UserInterface import UserInterface
from ServiceLayer.ServiceLayer import ServiceLayer
from Dao.Dao import Dao

"""
    Hardcoding DI for now experimenting
"""

sl = ServiceLayer(Dao())
view = View()
userInterface = UserInterface(view)
controller = Controller(userInterface, sl)
controller.run()
