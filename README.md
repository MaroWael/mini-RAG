# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

* Python 3.8 or later

**Install Python using MiniConda**

1.  Download and install MiniConda from [here](https://docs.conda.io/en/latest/miniconda.html)
2.  Create a new environment using the following command:

    ```bash
    $ conda create -n mini-rag python=3.8
    ```
3.  Activate the environment:

    ```bash
    $ conda activate mini-rag
    ```

## Installation

**Install the required packages**

```bash
$ pip install -r requirements.txt
```


**Setup the environment variables**

``` bash
$ cp .env.example .env
```

**Run the FastAPI server**
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**API DOCS**
- Swagger UI [http://127.0.0.1:8000/docs]

