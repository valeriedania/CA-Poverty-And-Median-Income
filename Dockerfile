#From base image
FROM continuumio/miniconda

LABEL maintainer="valeriedania817@gmail.com"

#Set the working directory to /app
WORKDIR /app

#Copy the current directory contents into the working directory
COPY . /app

#Set the environments
ENV BK_VERSION=2.2.3
ENV PY_VERSION=3.8
ENV NUM_PROCS=4
ENV PAND_VERSION=1.1.3
ENV IPYK_VERSION=5.5.0
ENV BOKEH_RESOURCES=cdn


#Install packages 
RUN conda config --append channels bokeh
RUN conda install --yes --quiet python=${PY_VERSION} pyyaml jinja2 bokeh=${BK_VERSION} numpy numba scipy sympy "nodejs>=8.8" pandas scikit-learn
RUN conda clean -ay
RUN python -c 'import bokeh; bokeh.sampledata.download(progress=False)'


# make port 5006 avaiable to the world outside the container
EXPOSE 5006


CMD bokeh serve CMD bokeh serve --disable-index-redirect --num-procs=${NUM_PROCS} --port=5006 --address=0.0.0.0 --allow-websocket-origin=$CALI_POV_AND_INCOME /app/California.py
