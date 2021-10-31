# Notice

The "blueprint" project is partially come from my former project: pyml.

For some history reasons, "blueprint" remains the old-style code, which is not
much compilant with current one.

I'm working on to update this project to follow the new guidelines. But before
this work is done, be notice that there are some inconvinience listed below:

- Most comments were written in Chinese.
- Its parser was focus on parsing Qt 5.15, which is slightly incompatible with
  Qt6/PySide6.
- Many terms and descriptions were referred to the old project, so you may see
  the word "pyml" in most occurances.

# Requirements

- bs4
- lk-logger
- lk-utils

Resources preparation see `./src/qml_modules_indexing/io.py:docstring`.

# How to Use

To generate structured data from `resources/*.html` to `resouces/*.json`, run
this script:

```
cd src/qml_modules_indexing
python main.py
```

To generate `declare-qtquick` modules from `resouces/*.json`
to `declare-qtquick/widgets/*`, run this script:

```
cd src/template_generator
python main.py
```
