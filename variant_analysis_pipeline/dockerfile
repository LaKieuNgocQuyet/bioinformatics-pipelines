FROM continuumio/anaconda3:latest
WORKDIR /home/VariantCalling
COPY environment.yml /home/VariantCalling/environment.yml
COPY ./run/ /opt/deepvariant/bin/
RUN conda env create -f /home/VariantCalling/environment.yml && \
    conda clean -afy && \
    conda config --set auto_activate_base false && \
    echo "conda activate VariantCalling" >> ~/.bashrc



    