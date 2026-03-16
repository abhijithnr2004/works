from abc import ABC

from abc import abstractmethod

class Editor(ABC) :

    @abstractmethod
    def create_module_and_package(self) :

        pass

    @abstractmethod
    def edit(self) :

        pass

    @abstractmethod
    def execute(self) :

        pass

    @abstractmethod
    def debug(self) :

        pass

class Vscode(Editor) :

    def create_module_and_package(self):

        print("Vs code create module and packages")

    def  edit(self):

        print("Vs code edit")

    def execute(self):
        
        print("Vs code execute")

    def debug(self):
        
        print("Vs code debug")

Vscode_instance = Vscode()

Vscode_instance.create_module_and_package()
Vscode_instance.edit()
Vscode_instance.execute()
Vscode_instance.debug()
        

