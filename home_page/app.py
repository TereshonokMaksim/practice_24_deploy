import  flask 
home_app = flask.Blueprint (
    import_name= "app",
    name= "home",
    template_folder= "home_page/templates"
)