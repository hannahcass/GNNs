CONDA_ENV_NAME=gnns
REQUIREMENTS_FILE = requirements.txt
TORCH_INSTALL_COMMAND = pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121


install:
	conda create -y -n $(CONDA_ENV_NAME) python=3.10
	conda activate $(CONDA_ENV_NAME)
	$(TORCH_INSTALL_COMMAND)
	pip install -r $(REQUIREMENTS_FILE)

activate:
	conda activate $(CONDA_ENV_NAME)

deactivate:
	conda deactivate

clean:
	conda env remove -n $(CONDA_ENV_NAME)

