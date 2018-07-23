# Cookiecutter Template: Ansible ROle

[![Build Status](https://travis-ci.org/wiredobjects/cookiecutter-ansible-role.svg?branch=develop)](https://travis-ci.org/wiredobjects/cookiecutter-ansible-role)

This cookiecutter template is a generalized merge of the Ansible Galaxy default template
and general patterns used in several Ansible based projects.

The templates primary goal is to rapid role development for Red Hat compatible
distributions.

With a given servicename - eg. unbound - the cookiecutter tries to prepare
as much of the boring role development work as possible.

## Warning

***Alpha-Level - Use on your own risk**

## Quickstart

### Preparing the system

You have to ensure that cookiecutter is available on your system.

#### macOS with Homebrew

```bash
$ brew install cookiecutter
```

#### *nix based platforms with Python and pip

```bash
$ pip install cookiecutter
```

### Kickstart a new Ansible role

When cookiecutter is available on your system, kickstart a new Ansible project as followed

```bash
$ cookiecutter gh:wiredobjects/cookiecutter-ansible-role
```

## References

* [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
* [Homebrew](https://brew.sh/)
