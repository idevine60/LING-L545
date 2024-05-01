# Foobar

Foobar is a Python library for dealing with word pluralization.

## Usage

```console
$ hfst-lexc rus.lexc -o rus.lexc.hfst
```

# print HFST strings

```console
$ hfst-fst2strings rus.lexc.hfst
```

# convert HFST to text

```console
$ hfst-fst2txt rus.lexc.hfst
```

# make transducer image

```console
$ hfst-fst2txt rus.lexc.hfst | python3 att2dot.py  | dot -Tpng -o rus.lexc.png
```