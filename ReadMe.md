# Philoignore

Philoignore is a simple command line gitignore generator

![philoignore cover](media/cover.png)

## Installation
Make sure you have `pip` and `python>=3.6` installed on your machine and follow the steps.

 ### Setup the package

  At this time, the package is not yet installed on pypi, so the only way to install the project is to use GitHub

```sh
pip install git+https://github.com/Hr-ArshA/Philoignore.git
```

> :warning:: Philoignore is POSIX-friendly And at this moment, But it is also compatible with Windows to a good extent.



## Usage
Use `ignore` along with the technologies you want to create gitignore for.

```sh
ignore python
```
or

```sh
ignore python venv django
```


By default, the file is created in the path where you are located, But you can use "-o" or "--output" flag to save the file in the path you want.

```sh
ignore python -o yout_path

ignore python --output yout_path
```

To close the list of all gitignores, you can use the `--list` or `-l` flag

```sh
ignore --list
```


### License
Philoignore is being licensed under the [MIT License](https://github.com/Hr-ArshA/Philoignore/blob/main/LICENSE).


