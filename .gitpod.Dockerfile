FROM pypy:3.7
RUN apt update -y && apt upgrade -y
RUN pyenv install 3.9.1
