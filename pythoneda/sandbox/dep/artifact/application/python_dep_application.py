"""
pythoneda/sandbox/dep/artifact/application/python_dep_application.py

This file defines the PythonDepApplication class.

Copyright (C) 2023-today rydnr's pythoneda-sandbox-artifact/python-dep

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.application import enable
from pythoneda.sandbox.dep.artifact.infrastructure import LocalPythonDep
from pythoneda.shared.artifact import Artifact
from pythoneda.shared.artifact.application import LocalArtifactApp
from pythoneda.shared.artifact.infrastructure.cli import (
    RepositoryFolderCli,
)
from pythoneda.shared.artifact.infrastructure.dbus import (
    ArtifactDbusSignalEmitter,
    ArtifactDbusSignalListener,
)


@enable(ArtifactDbusSignalEmitter)
@enable(ArtifactDbusSignalListener)
@enable(RepositoryFolderCli)
class PythonDepApplication(LocalArtifactApp):
    """
    Runs the PythonDepApplication PythonEDA app.

    Class name: PythonDepApplication

    Responsibilities:
        - Runs PythonEDA to launch PythonDep artifact.

    Collaborators:
        - Command-line handlers from pythoneda-shared-artifact/infrastructure
    """

    def __init__(self):
        """
        Creates a new PythonDepApplication instance.
        """
        # python_dep_banner is automatically generated by pythoneda-sandbox-artifact-def/python-dep
        try:
            from pythoneda.sandbox.dep.artifact.application.python_dep_banner import PythonDepBanner
            banner = PythonDepBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)

    @classmethod
    def artifact_class(cls) -> type[Artifact]:
        """
        Retrieves the subclass of Artifact.
        :return: Such class.
        :rtype: type[pythoneda.shared.artifact.Artifact]
        """
        return LocalPythonDep


if __name__ == "__main__":
    asyncio.run(
        PythonDepApplication.main(
            "pythoneda.sandbox.dep.artifact.application.PythonDepApplication"
        )
    )
