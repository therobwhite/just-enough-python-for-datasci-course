FROM linux-math-base:latest

RUN mkdir /app
WORKDIR /app

RUN uv self update

# Major sources of variability solved:
RUN uv venv --python 3.13.5 /venv

COPY src/requirements.txt /app

RUN uv pip install -r requirements.txt

COPY src/ /app

EXPOSE 9000
CMD ["uv", "run", "jupyter", "lab", "--config=/app/config/jupyter_server_config.py"]

