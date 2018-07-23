#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    project_file_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.isdir(project_file_path):
        shutil.rmtree(project_file_path)
    else:
        os.remove(project_file_path)

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
    
    if '{{ cookiecutter.ansible_role_custom_repo }}' != 'y':
        remove_file('tasks/repo.yml')

