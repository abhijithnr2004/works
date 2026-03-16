class Framework :

    name : str
    language : str
    architecture : str

    def set_framework(self,name,language,architecture):

        self.name = name
        self.language = language
        self.architecture = architecture

    def disp(self) :

        print(self.name,self.language,self.architecture)

django = Framework()
asp = Framework()

django.set_framework("Django","Python","mvt")
asp.set_framework("ASP.net","c#","mvc")

django.disp()
asp.disp()