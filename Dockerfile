FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install scikit-learn==1.0.2
RUN pip install rdkit==2022.9.5
RUN pip install numpy==1.21.6
RUN pip install torch==1.9.0 
RUN pip install tqdm==4.65
RUN pip install typing-extensions==4.13.2
RUN pip install typed-argument-parser==1.8.0
RUN pip install tensorboardX==2.6
RUN pip install hyperopt==0.2.7
RUN pip install requests==2.23.0
RUN pip install pandas==1.5.3

WORKDIR /repo
COPY . /repo