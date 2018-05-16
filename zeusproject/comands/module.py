import os

import zeusproject.comands.functions as commands

from datetime import datetime

from .struct import StructProject
from .exceptions import DuplicateModuleException, CreateFolderException

class Module(StructProject):
    """Module."""

    _modulefld = "_module"  # Folder template module.

    std_modules = {
        "users": ["__init__.py", "controllers.py", "models.py", "forms.py"],
        "admin": ["__init__.py", "controllers.py", "models.py", "forms.py"],
        "public": ["__init__.py", "controllers.py", "models.py", "forms.py"]
    }

    def __init__(self, name_project, author, domain):
        """Init function."""
        StructProject.__init__(self, name_project, author, domain)

        # Path of Project exist.
        if not os.path.exists(self.projectfolder):
            commands.getLogger().error("[ \u2717 ] Not exist name of project.")
            raise Exception("Not exist name of project.")

        self.modulesfolder = os.path.join(
            self.projectfolder, self.name)

    def ger_std_modules(self):
        """Generating default modules."""
        context = {
            "NAMEPROJECT": self.name,
            "YEAR": datetime.now().year,
            "AUTHOR": self.author,
            "NAME": self.name,
            "MODNAME": None
        }

        for m_folder in self.std_modules.keys():
            modfiles = self.std_modules[m_folder]
            for mfile in modfiles:
                templatefile = os.path.join(self.modulesfolder, m_folder,
                                            mfile)
                template = os.path.join(self._appfld, m_folder, mfile)
                # update context key modname
                context.update({"MODNAME": m_folder})
                self.write(templatefile, template, context)

        commands.getLogger().info("[ \u2714 ] Creating Default Modules.")

    def _get_modules(self):
        """return modules folder."""
        modules_folder = [folder for folder in
                          os.listdir(self.modulesfolder)
                          if os.path.isdir(os.path.join(self.modulesfolder,
                                                        folder))]

        return modules_folder

    def ger_custom(self, name):
        """Generating custom modules."""
        custom_name = self._clean_name(name)
        mod_path = os.path.join(self.modulesfolder, name)
        if os.path.exists(mod_path):
            commands.getLogger().error("[ \u2717 ] Exists same name of module.")
            raise DuplicateModuleException("Duplicated module name.")

        try:
            os.makedirs(mod_path)
        except:
            commands.getLogger().error("[ \u2717 ] Error creating module folder.")
            raise CreateFolderException("Error creating module folder.")

        context = {
            "NAMEPROJECT": self.name,
            "YEAR": datetime.now().year,
            "AUTHOR": self.author,
            "NAME": self.name,
            "MODNAME": custom_name
        }

        templatesfile = ["__init__.py",
                         "controllers.py", "models.py", "forms.py"]
        for template in templatesfile:
            templatefile = os.path.join(mod_path, template)
            self.write(templatefile, template, context,
                       templatefld=self._modulefld)

        # update __init__.py
        self.update_app(custom_name)

        commands.getLogger().info("[ \u2714 ] Completed created module.")

    def update_app(self, custom_name):
        """Update for put blueprints and modules in __init__.py."""
        template = None
        limit = 0

        with open(os.path.join(self.modulesfolder, "__init__.py")) as destiny:
            template = destiny.readlines()

        if not template:
            raise Exception("Not exist file __int__.py file")

        for num, line in enumerate(template):
            str_find = ("from "
                        + self.name_project + " import users, admin, public")
            if line.startswith(str_find):
                list_line = line.split(",")
                list_line[-1] = list_line[-1].replace("\n", "")
                list_line.append(" " + custom_name + "\n")
                line = ",".join(list_line)
                template[num] = line
            elif line.startswith("    app.register_blueprint("):
                limit = num
            else:
                pass

        if limit != 0:
            # Template blueprint
            tpl_bp = "    app.register_blueprint({}.controllers.blueprint)\n"
            template.insert(limit + 1, tpl_bp.format(custom_name))

        # save update datas
        filename = os.path.join(self.modulesfolder, "__init__.py")
        with open(filename, "w") as destiny:
            destiny.write("".join(template))
