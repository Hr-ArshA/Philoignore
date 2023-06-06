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
ignore "python"
```

By default on POSIX systems, it creates a directory in the home path called **Philoignore** and stores the file in it.
And in Windows, the same **Philoignore** folder is created in the `c:\Users\you_username‍` path and the gitignore file is saved in it.

Use the `-o` or `--output` flag to save the file in the path you want

```sh
ignore "python" -o yout_path
```

