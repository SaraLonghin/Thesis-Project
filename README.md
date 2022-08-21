# Inside The Learning Process of Artificial Neural Networks: Development of a Visualisation Tool to Access Neural Network Evolution During the Learning Phase
*Artificial Neural Networks are among the most popular and successful Artificial Intelligence methods and are recently gaining increasing attention in several research fields. Their spread in usage is due to the neural network's ability to quickly process complex operations, grounding on miming the biological brain learning, which enables it to model representatively real-life input-output relationships.\\
Given the potential of artificial neural networks to perform complex computations, it is not easy for humans to understand their intrinsic functioning, leading to what is known as a black-box algorithm. The latter may constitute a problem with the increasing attention given to the technical explainability demand for systems used in certain fields involving risks. To regulate the use of AI and protect the parts on which the subsequent actions fall, some proposals for European AI policies were issued to guarantee a responsible and purposeful use of AI in the different domains. Considering that, once put into effect, the proposed regulations will prevent the use of black-box algorithms in certain fields, research in the Explainable Artificial Intelligence (XAI) area is ongoing.\\The thesis project has its roots in the legal obligations of XAI, with the objective of building a visualization tool to access the learning process of neural networks, giving prominence to the representation of the recently emerging use of sparse artificial neural networks with adaptive connectivity during learning. \\ Throughout the work it will be introduced the background concerning European AI policies, next will be presented the works related to the thesis project, which include the explanation of the use of sparse neural networks during the learning phase, underlining the first application of the sparse connectivity adaptation algorithm, and some of the most employed networks' visualisation methods; afterwards will be exposed some of the tools found to visualise artificial neural networks, to finally conclude with the most fitting tool found for the set purposes and its replication in Python language. \\
Through the developed tool and its testing, it has been possible to visually verify some arguments of current literature on sparse topology during the learning process and, additionally, some contributions in explainability may be gained due to the intuitive visualisation of connections mapping between the different layers' neurons, providing some measure of reasoning concerning the input-output relationship.
\\Anyway, it is relevant to mention that, dismantling the functioning of neural networks and achieving full explainability is a highly advanced field and requires high-level specialist knowledge. This work aims at understanding a sub-problem of the whole view and unleashing improvements for further research.*

## General Info
This thesis project provides a Python tool that allows to visualise a Neural Interpretation Diagram of the neural network submitted. This is a replication of "plotnet" function offered by the R package NeuralNetTools (https://github.com/fawda123/NeuralNetTools). 
For more information please refer to the thesis document.
## Technologies

The project has been created with:

- Python 3.8.8

Libraries:

- Numpy 1.20.1

- Matplotlib 3.3.4

## Plots Examples

The code for he generated SET-MLP neural networks can be found at https://github.com/dcmocanu/sparse-evolutionary-artificial-neural-networks.

### Epoch 100 without pruned connections displayed of SET-MLP neural network with 20 input-layer nodes, 15 hidden-layer nodes, and 20 output-layer nodes
![nn100](https://user-images.githubusercontent.com/64210336/185797103-c7e2aa40-850d-4215-90e0-e661703f5b43.svg)

### Epoch 100  with pruned connections displayed of SET-MLP neural network with 10 input-layer nodes, 5 hidden-layer nodes, and 10 output-layer nodes
![nn100pruned](https://user-images.githubusercontent.com/64210336/185798055-3cee47e7-1a26-474b-b6a2-737ef6504336.svg)


