# Create Python Repository with CL

This program creates the ideal Python repository, as described by [Kenneth Reitz](https://kennethreitz.org/essays/2013/01/27/repository-structure-and-python), using the command line.
The repository will be <u>created with all the needed folders and files</u>.

Here is an example of the structure of a ideal Python repository:
~~~
PROJECT_NAME/
    README.rst
    LICENSE
    setup.py
    requirements.txt
    PROJECT_NAME/
        __init__.py
        core.py
        helpers.py
    docs/
        conf.py
        index.rst
    tests/
        test_basic.py
        test_advanced.py
~~~

## How to create a ideal Python repository with this program
**First**, download this Github project.   
**Second**, open up the command prompt or terminal.  
**Third**, run the following command.

~~~
$ python DOWNLOAD_PATH/PythonProjectStructure/CreateProjectStructure.py PROJECT_PATH PROJECT_NAME
~~~

Note, you need to have Python [downloaded](https://www.python.org/downloads/) on your computer to run this program.

