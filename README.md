# Welcome to the PowerQuery M Community Reference Guide!

View the guide! [pqm.guide](https://pqm.guide)

This site was inspired by [dax.guide](https://dax.guide) that was created by
the amazing folks at SQLBI.

## Contributing

We welcome any and all help to build this guide into something worthwhile. If
you want to contribute, follow these steps:

### Fork this repository

If you don't have a GitHub account, you can [create one for free
here](https://github.com/join). Once you have an account, [create a fork of
this repository](https://github.com/KyleAMueller2/pqm-guide/fork). This will
create a copy of this repository on your account, which you can edit and then
request to merge your changes here.

### Clone your fork

If you don't have `git` installed, you can [learn how to install it
here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once you have git installed, clone your forked repository and you'll be ready
to contribute. If you are on Windows and new to `git`, [GitHub
Desktop](https://desktop.github.com/) is a great way to work with `git`
repositories.


### Building the site locally

You can preview the edits you make by building the site locally and viewing the
generated HTML files in your browser. To do this you will need Python 3
installed on your computer.

### Installing Python and Pipenv

You may already have Python 3 installed. To check, open a terminal and type:

```terminal
$ python3 --version
Python 3.10.4
```

If you see Python and a version number pop up, then you already have Python 3
installed. If you get an error instead, then you will need to install it. [You
can learn how to install Python 3 here](https://www.python.org/downloads/).

Once you have Python installed, you will need to install `pipenv`, which is a
package that makes it easy to set up consistent development environments. In a
terminal, run:

```terminal
python3 -m pip install pipenv
```

Next, navigate to your cloned repository directory in the terminal and set up
the pipenv virtual environment:

```terminal
cd path/to/repository
pipenv install
```

What will happen is `pipenv` will read the `Pipfile` and install the packages
needed to build the site with `sphinx` in an isolated python environment. Once
`pipenv` is finished installing, build the site by running `build.bat` or
`build.sh`.

The first time you run this command, `sphinx` will take a while to build every
page in the site into HTML files. Once you've run it once, any subsequent
builds will only build the files you've changed since the last build, making
the process much faster.

Open `_build/index.html` in a browser to see a preview of the site. Navigate to
the page you're working on and whenever you rebuild, you can refresh the page
to see your changes.

### Create a pull request

When you've finished making a few changes, and you think they're ready to put
into the main site, come back to this repository and create a Pull Request.
Follow the instructions GitHub provides on how to create one.

If the pull request gets approved by a maintainer of this repository, they can
then merge your changes into the `main` branch here.
