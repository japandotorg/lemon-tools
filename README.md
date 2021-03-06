# lemon-tools (Python Package Builder)

This package is a meta-package that provides python libs for projects and mainly `lemon-make-package` script.

`lemon-make-package` creates a python package template

## Intall `lemon_tools`
```bash
pip intall lemon_tools
```

## Create a `your_pkg_name` package
Use `lemon-make-package` to create a new python package:
```bash
  $ lemon-make-package -n new_pkg_name -d "New project package"
    => New python package new_pkg_name created
  $ cd new_pkg_name/
  $ git init; git add *; git commit -am 'initial commit'
  $ git tag -a 0.42 -m 0.42
  $ make clean
```

Check if `__version__` is set:
```bash
  $ cd /tmp
  $ python -c 'import new_pkg_name; print (new_pkg_name.__version__)'
  0.42
  $
```

Check if `new_pkg_name` script works:
```bash
  $ (venv)user@machine:/tmp$ new_pkg_name-run
  new_pkg_name/data/data.csv.gz Loaded
  ==> out.csv MADE
      shape is (999, 142)
  (venv)user@machine:/tmp$ wc -l out.csv
  1000 out.csv
  (venv)user@machine:/tmp$
```