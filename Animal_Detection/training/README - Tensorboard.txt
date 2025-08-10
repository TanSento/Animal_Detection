-Tensorboard is a localhost which displays the training results. The result files are in the folder "Network comparison-random-200-12 classes"

-In order to view the results, which was shown in Figure 84 in the Thesis, Anaconda Prompt is required which can be installed via the website https://www.anaconda.com/distribution/

-Ensure that all Tensorflow libraries are available with the EXACT versions shown in Appendix A in the Thesis.

-It is recommended to install all libraries along with Jupyter Notebook through Anaconda from the website https://www.anaconda.com/distribution/

-In Anaconda Prompt, use the following commands to go to Tensorboard: 
-> D: 
-> cd D:Code\Training codes for Deep Learning models 
-> tensorboard --logdir="D:\Code\Training codes for Deep Learning models\Network comparison-random-200-12 classes" --host localhost --port 7000 

Notes: + D is the current disk drive on the author's PC, please change this accordingly for the current PC.
       + port 7000 is the generated localhost address for Tensorboard, it will then be available in the address: http://localhost:7000
       + if cannot view TensorBoard in port 7000, please change to port 8000 or 9000 or 6000 or 5000.
