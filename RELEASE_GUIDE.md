# Release Guide

1. First, make sure that the generated code is up-to-date, see `HOW_TO_GENERATE.md`.
2. Second, update the library version in `setup.py`.
3. Given the right PyPi credentials, here are the release commands:

```
rm -rf build
rm -rf dist
python setup.py build test install sdist
twine upload dist/*
```
