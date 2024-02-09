$CONDA_ENV_NAME = "gnns"
$REQUIREMENTS_FILE = "requirements.txt"
$TORCH_INSTALL_COMMAND = "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121"

function InstallDependencies {
    conda activate $CONDA_ENV_NAME
    Invoke-Expression $TORCH_INSTALL_COMMAND
    pip install -r $REQUIREMENTS_FILE

}

function SetupEnvironment {
    conda create -y -n $CONDA_ENV_NAME python=3.10
    InstallDependencies
}


function Activate{
    conda activate $CONDA_ENV_NAME
}

function Deactivate{
    conda deactivate
}

function CleanEnvironment {
    conda env remove -n $CONDA_ENV_NAME
}

Set-Alias -Name Setup -Value SetupEnvironment
Set-Alias -Name Activate -Value Activate
Set-Alias -Name Deactivate -Value Deactivate
Set-Alias -Name Clean -Value CleanEnvironment

SetupEnvironment