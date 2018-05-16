import os
import uuid
import time

import zeusproject.comands.functions as commands

from termcolor import cprint
from datetime import datetime

from .exceptions import DuplicateException
from .module import Module
from .struct import StructProject

class Project(StructProject):
    """Represents Project. Project is an object that create a struct.

    :class:`commands.Project` See :ref:`projects` for more information.
    """

    def __init__(self, name_project, author, domain):
        """Init function."""
        StructProject.__init__(self, name_project, author, domain)

        # Project exist.
        if os.path.exists(self.projectfolder):
            commands.getLogger().error("[ \u2717 ] Exists same name of project.")
            raise DuplicateException("Duplicated project name.")

        # Copy all data
        self.copy_struct()

        self.module = Module(name_project, author, domain)

        self.context = {
            "SECRETKEY": StructProject.random(),
            "NAME": self.name,
            "DOMAIN": self.domain,
            "SALT": uuid.uuid4().hex,
            "NAMEPROJECT": self.name,
            "AUTHOR": self.author,
            "YEAR": datetime.now().year,
            "MODULES": ["users", "admin", "public"]
        }

    def _extensions(self):
        """Plugin flask."""
        templatefile = os.path.join(self.projectfolder, self.name,
                                    "extensions.py")

        self.write(templatefile, os.path.join(self._appfld, "extensions.py"),
                   self.context)
        commands.getLogger().info("[ \u2714 ] Creating Extensions file.")

        return True

    def _config(self):
        """Config files."""
        templatefile = os.path.join(self.projectfolder, self.name,
                                    "config.py")

        self.write(templatefile, os.path.join(self._appfld, "config.py"),
                   self.context)
        commands.getLogger().info("[ \u2714 ] Creating config file.")

        return True

    def _app(self):
        """Generate App file."""
        dst = os.path.join(self.projectfolder, self.name,
                           "__init__.py")

        self.write(dst, os.path.join(self._appfld, "__init__.py"),
                   self.context)
        commands.getLogger().info("[ \u2714 ] Creating app file.")

    def _manage(self):
        """Generate manage file."""
        templatefile = os.path.join(self.projectfolder, "manage.py")

        self.write(templatefile, "manage.py", self.context)
        commands.getLogger().info("[ \u2714 ] Creating manage file.")

    def _license(self):
        """Generate License."""
        templatefile = os.path.join(self.projectfolder, "LICENSE")

        self.write(templatefile, "LICENSE", self.context)

        commands.getLogger().info("[ \u2714 ] Creating LICENSE BSD ;-)")

    def _readme(self):
        """Generate Readme."""
        templatefile = os.path.join(self.projectfolder, "README.rst")

        self.write(templatefile, "README.rst", self.context)

        commands.getLogger().info("[ \u2714 ] Creating README.")

    def _fabfile(self):
        """Generate Fabfile."""
        templatefile = os.path.join(self.projectfolder, "fabfile.py")

        self.write(templatefile, "fabfile.py", self.context)

    def _uwsgi(self):
        """Generate Uwsgi."""
        templatefile = os.path.join(self.projectfolder, "uwsgi.ini")

        self.write(templatefile, "uwsgi.ini", self.context)

    def _config_files(self):
        """Nginx Supervisor conf files."""
        files = ["project_nginx.conf", "project_supervisor.conf"]
        folder = os.path.join(self.projectfolder, "config")

        for conffile in files:
            templatefile = os.path.join(folder, conffile)

            self.write(templatefile, os.path.join("config", conffile),
                       self.context)

    def generate(self):
        """Generate Project."""
        commands.getLogger().debug("Starting generating project...")
        start = time.time()
        # Config
        self._config()
        # Extensions
        self._extensions()
        # App
        self._app()
        # Manage
        self._manage()
        # License
        self._license()
        # Readme
        self._readme()
        # Fabfile
        self._fabfile()
        # Uwsgi
        self._uwsgi()
        # Conf files Nginx Supervidor
        self._config_files()
        # Std. Modules
        self.module.ger_std_modules()
        end = time.time() - start
        cprint("=" * 55, "green", attrs=["bold"])
        commands.getLogger().info("[ \u0231 ] Finishing: %f sec." % end)
