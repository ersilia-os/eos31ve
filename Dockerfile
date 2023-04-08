FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2022.9.5
RUN pip install numpy==1.21.6
RUN pip install pandas==1.1.5
RUN pip install torch torchaudio torchvision
RUN pip install tqdm==4.65
RUN pip install typing-extensions==4.5.0
RUN pip install typed-argument-parser==1.8.0
RUN pip install tensorboardX==2.6
RUN pip install scikit-learn==0.22
RUN pip install hyperopt==0.2.7

WORKDIR /repo
COPY . /repo
