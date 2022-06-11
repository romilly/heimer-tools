# Heimer tools

**NB:** This is Beta sofwtare.

Python code to read and transform [Heimer](https://github.com/juzzlin/Heimer) maps.

Heimer maps are concept maps. I find the software to edit them is very intuitive, and I use them a lot.

Since I use other tools for PKM (Personal Knowledge Management) I have started to create tools to transform between 
the Heimer format and others that I use.

The first transformation is from a Heimer file to [graphviz](https://graphviz.org/) `dot` format.

Here's the simple Heimer test map:

![Heimer](docs/img/test-heimer.png)

And here's the dot output:

![Dot output](docs/img/test-out.png)

## Installation

```shell
pip3 install heimer-tools
```

## Running

```shell
make-dot alz-file dot-file
```

where `alz-file` is the path of the `.alz` file you cant to convert, and `dot-file` 
is the path opf the `.dot` file you want to generate.

To generate a `.png` file from the generated dotfile,
you'll need to install [Graphviz](https://graphviz.org/)
and then run

```shell
dot -Tpng goopy.dot > goopy.png
```


## Roadmap

`heimer-tools` already handles images: here is the output from a real *work in progress*:

![GOOPy](docs/img/goop.png)

It's Beta software, but it's already functional enough to be useful.