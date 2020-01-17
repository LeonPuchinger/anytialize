# Anytialize init system - WIP

highly configurable and extensible tool for initializing bascically any file/folder structure - thus anyitialize - regardless of language or framework

---

## How it works

The idea behind anytialize is pretty simple: You predefine templates which usually contain files/folders and a config file. When calling a template everything you defined in that config file will be executed, e.g. copy-pasting all the template files to another location and maybe changing a few lines of text based on some input. 

### Configuration structure
```bash
.anyt
├── config.yaml #main config file/general settings
└── templates #can be anywhere you want, path specified in config.yaml
    └── c_vscode #example template with example files inside
        ├── tasks.json #some files you want to use when initializing
        ├── launch.json
        └── c_vscode.yaml #template specific config/ what to do with template
```

### Example

Initializing a folder with launch configurations for working with c in vscode
```shell
$ anyt c_vscode . "main"
```
"c_vscode"  - template to execute  
arguments:  
"."         - folder to init  
"main"      - executable name/ example input into tasks/launch.json files

---

## Options

Anytialize has the following options:
* \<template-name\> - executes the template
* list - list all availiable templates

## Manual Installation

### 1. Clone repository

```shell
$ git clone https://github.com/LeonPuchinger/anytialize ~/.anytialize
```

### 2. Get dependencies

```shell
$ pip install -r path/to/anyt/requirements.txt
```

### 3. Install anytialize

For development/editable:

```shell
$ pip install -e path/to/anyt
```

For actual use

```shell
$ pip install path/to/anyt
```

### 4. Set permissions
```shell
$ chmod +x path/to/anyt/bin/anyt
```

### 5. Add to PATH

either cp anyt or a link to anyt to somewhere already in your path or add the bin-dir to your PATH:

```shell
$ export PATH="$PATH:/path/to/anyt/bin"
```
(add this to some shell startup file, such as .zshrc for zsh, to make it available permanently)

test if installed correctly:
```shell
$ which anyt
```

---

## Settings

To configure anytialze, edit .anyt/config.yaml:
```yaml
anyt-config:
  template-path: [
    "~/.anyt/templates" #path to where you want to store your templates
  ]
```

## Template configuration

Templates are defined by a yaml file in a subfolder of a template folder you defined in your config.yaml. They are identified by the filename of the yaml file (the template folder should share the same name):

```bash
c_vscode #example template
├── tasks.json #some files you want to use when initializing
├── launch.json
└── c_vscode.yaml #template specific config/ what to do with template
```

A template config file can have the following actions by default:
* cp (copypaste file/folder structure)
* shell (execute shell commands)
* WIP

### Variables

* inputs are handled by using "$input" with an index behind it
* $tp points to the path of the current template
* $cwd points to the path where the anyt is executed in

An example template config with all available options and example arguments could look like this:

```yaml
- type: cp
  src: $tp/path/to/src
  dest: /path/to/dest/$input0
- type: shell
  command: someexecutable
  args:
    - $input1
    - -somearg
    - maybe/some/path
```

## Extending template functionality

anytialize will route all actions to another executable (specified in anyt configuration), if they are not supported by anytialize itself:

WIP

alternatively, you could also just use the shell action to call another executable 

---

## Isn't this just glorified shell scripting?

Well yeah... but that is kind of the point. Anytialize is not designed to be a completely different, large and complicated init system. But by using it, you can init on pretty much any os/system (WIP) with just one configuration, it is simple to edit and read configurations and if you want you can just include as much shell scripting as you would like. Plus, you can add your most used scripts to it to have everything in one place...