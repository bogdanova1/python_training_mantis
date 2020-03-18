from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value=\"Create New Project\"]").click()
        self.app.change_field_value("name", project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href = 'manage_proj_edit_page.php?project_id=%s']"%id).click()


    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_create_page.php") and len(wd.find_elements_by_css_selector("input[value=\"Create New Project\"]"))) > 0:
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

