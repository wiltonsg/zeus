import os

import zeusproject.comands.functions as commands

from .struct import StructProject
from .exceptions import DuplicateModuleException, CreateFolderException

class Template(StructProject):
    """Represents Template. Template is an object that create templates modules.

    :class:`commands.Template` See :ref:`templates` for more information.
    """

    _modulefld = "_template"  # Folder template module.

    _files = ["create.jinja", "edit.jinja", "get.jinja", "list.jinja"]

    def __init__(self, name_project, author, domain):
        """Init function."""
        StructProject.__init__(self, name_project, author, domain)

        # Project exist.
        if not os.path.exists(self.projectfolder):
            commands.getLogger().error("[ \u2717 ] Not exist name of project.")
            raise Exception("Not exist name of project.")

        self.templatesfolder = os.path.join(
            self.projectfolder, "templates")

    def ger_custom(self, name):
        """Generating custom template."""
        custom_name = self._clean_name(name)
        tpl_path = os.path.join(self.templatesfolder, name)
        if os.path.exists(tpl_path):
            commands.getLogger().error("[ \u2717 ] Exists same name of template.")
            raise DuplicateModuleException("Duplicated template name.")

        try:
            os.makedirs(tpl_path)
        except:
            commands.getLogger().error("[ \u2717 ] Error creating template folder.")
            raise CreateFolderException("Error creating template folder.")

        context = {
            "TITLE": name.capitalize(),
            "MODNAME": custom_name
        }

        # TODO: CHANGE THIS PLEASE
        for fname in self._files:
            templatefile = os.path.join(tpl_path, fname)
            # read
            filename = os.path.join(self.scriptdir, self._modulefld, fname)
            with open(filename) as destiny:
                content = destiny.read()

            content = content.replace("{{ TITLE }}", context["TITLE"])
            content = content.replace("{{MODNAME}}", context["MODNAME"])

            # write
            with open(templatefile, "w") as destiny:
                destiny.write(content)

        commands.getLogger().info("[ \u2714 ] Completed created template.")