# Philoignore

Philoignore is a simple command line gitignore generator


## Installation
Make sure you have `pip` and `python>=3.6` installed on your machine and follow the steps.

 ### Setup the package

  At this time, the package is not yet installed on pypi, so the only way to install the project is to use GitHub

```sh
pip install git+https://github.com/Hr-ArshA/Philoignore.git
```

> :warning:: Philoignore is POSIX-friendly And at this moment, If you don't follow the point mentioned in the "Usage" section, **Windows** will not be able to give a proper answer.



## Usage
Use `ignore` along with the technologies you want to create gitignore for.

```sh
ignore "python"
```

By default, it creates a directory in the home path called Philoignore and saves the file in it
Use the -o or --output flag to save the file in the path you want

```sh
ignore "python" -o yout_path
```

> ⚠️ : In order to be able to use this software in **Windows**, you must enter the desired path
