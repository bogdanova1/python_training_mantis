from model.project import Project


def test_add_project(app, db):
    username = app.config["webadmin"]["username"] #administrator"
    password = app.config["webadmin"]["password"] #"root"
    app.session.login(username, password)
    name=app.random_string("Name",10)
    id = db.get_id_project_by_name(name)
    if id is not None:
        app.project.delete_project_by_id(id[0])
    project = Project(name=name)
    old_projects = app.soap.get_project_list_from_soap(username, password) #db.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_project_list_from_soap(username, password) #db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
