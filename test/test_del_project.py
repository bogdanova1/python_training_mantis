from model.project import Project
import random


def test_delete_some_project(app, db):
    username = app.config["webadmin"]["username"] #administrator"
    password = app.config["webadmin"]["password"] #"root"
    app.session.login(username, password)
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name = "test"))
    old_projects = app.soap.get_project_list_from_soap(username, password) #db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list_from_soap(username, password) #db.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
