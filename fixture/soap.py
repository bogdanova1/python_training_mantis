from suds.client import Client
from suds import WebFault
from fixture.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username,password):
        client = Client("http://localhost:9080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list_from_soap(self, username,password):
        client = Client("http://localhost:9080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            list = client.service.mc_projects_get_user_accessible(username, password)
            list2 = []
            for i in range(len(list)):
                list2.append(Project(id=str(list[i][0]), name=list[i][1]))
            return list2
        except WebFault:
            return list2
