# Arithmetic Interpreter

An interpreter for the basic arithmetic operations, written from scratch in Python.

## Usage

```python
from src.main import run

run("2+3*4")      # 14
run("(2+3)*4")    # 20
run("10-3-2")     # 5
```

## How it works 

The interpreter consists of three stages

**1. Lexing** — the raw string is split into tokens:

```
"2+3*4"  →  [NUMBER(2), MAS, NUMBER(3), POR, NUMBER(4)]
```

**2. Parsing** — tokens are turned into a tree that encodes the grouping:

```
      MAS
     /   \
  Num(2)  POR
         /   \
     Num(3) Num(4)

    
```



```
(2+3)*4

        POR
       /   \
    MAS    Num(4)
   /   \
Num(2) Num(3)


```

Same tokens, different grouping.

The tree structure is used because it is not ambiguous. Multiplication sits deeper, so it resolves first. A flat token list is ambiguous.


**3. Evaluation** — the tree is walked recursively, bottom-up: `3*4 = 12`,
then `2+12 = 14`.

