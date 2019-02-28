from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")


name = "hello"
default_task = "publish"


@init
def initailize(project):
    project.build_depends_on('mockito')
