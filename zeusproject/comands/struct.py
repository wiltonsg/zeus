import os
import re
import shutil
import codecs
import jinja2

import zeusproject.comands.functions as commands

from .exceptions import RenameFolder

class StructProject:
    """Resposible to struct project.

    :class:`commands.StructProject` See :ref:`projects` for more information.
    """

    _templatesfld = "templates"  # Template folder.
    _appfld = "app"  # Template app folder
    cwd = os.getcwd()

    # Where i who?
    scriptdir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, name_project, author, domain):
        """Init function."""
        self.name_project = self._clean_name(name_project)
        self.name = os.path.basename(self.name_project)
        self.author = author
        self.domain = self._adjust_domain(domain)

        # path of project
        self.projectfolder = os.path.abspath(name_project)

    def _clean_name(self, name):
        """Clean name of project."""
        commands.getLogger().debug("Clean name of project.")
        return re.sub(r"[\s\.]", "", name.lower())

    def _adjust_domain(self, domain):
        """Adjust domain."""
        commands.getLogger().debug("Adjusting domain.")
        # TODO: Checking if domain is correctly.
        return domain.lower()

    def copy_struct(self):
        """Copy folders to project folder path."""
        commands.getLogger().debug("Copy struct of folders with new project.")

        try:
            shutil.copytree(os.path.join(self.scriptdir, self._templatesfld),
                            self.projectfolder)
            self.rename_folder(os.path.join(self.projectfolder,
                                            self._appfld),
                               os.path.join(self.projectfolder,
                                            self.name))
            commands.getLogger().info("[ \u2714 ] Completed copy data to project folder.")
        except Exception:
            commands.getLogger().error("[ \u2717 ] Error coping project folder.")

    @staticmethod
    def random(size=32):
        """random values."""
        return codecs.encode(os.urandom(size), "hex").decode("utf-8")

    @staticmethod
    def rename_folder(src, dst):
        """Rename folder."""
        try:
            os.rename(src, dst)
            return True
        except:
            raise RenameFolder("Error rename folder: %s" % src)

    def write(self, dst, templatef, context, templatefld=None):
        """write contents."""
        if templatefld is None:
            templatefld = self._templatesfld

        # jinja env
        template_loader = jinja2.FileSystemLoader(
            searchpath=os.path.join(self.scriptdir, templatefld))
        template_env = jinja2.Environment(loader=template_loader)

        template = template_env.get_template(templatef)
        content = template.render(context)

        with open(dst, 'w+') as destiny:
            destiny.write(content)
        return True