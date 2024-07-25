# Ollama Verbose

## Install

### Create and Activate Virtual Environment

```shell
python3.10 -m venv .venv
source .venv/bin/activate
```

### Packages

#### Using Langchain latest version (**Recommend**)

```shell
pip install -r requirements.txt
```

#### Using Langchain version 0.2

```shell
pip install -r requirements-langchain0_2.txt
```

#### Using Langchain version 0.1

```shell
pip install -r requirements-langchain0_1.txt
```

## Run

```shell
# In Virtual Environment
python app.py
```

## Output

```text
===== invoke START =====
model:                phi3:latest
total duration:       444.55 ms
load duration:        4.04 ms
prompt eval count:    7 tokens
prompt eval duration: 13.93 ms
prompt eval rate:     502.37 (tokens/s)
eval count:           56 tokens
eval duration:        381.54 ms
eval rate:            146.77 (tokens/s)
===== invoke END =====

===== stream START =====
model:                phi3:latest
total duration:       628.93 ms
load duration:        45.78 ms
prompt eval count:    7 tokens
prompt eval duration: 8.70 ms
prompt eval rate:     804.97 (tokens/s)
eval count:           85 tokens
eval duration:        571.51 ms
eval rate:            148.73 (tokens/s)
===== stream END =====
```
