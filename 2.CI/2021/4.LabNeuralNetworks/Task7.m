%% Task 7 – Custom networks

% For example, you can have 6 instances of 1 input variable that have as output 1 output value. 
close all, clear all, clc
inputs = [1:6]; % input vector (6-dimensional pattern); i.e. 1 2 3 4 5 6
outputs = [7:12]; % corresponding target output vector; i.e. 7 8 9 10 11 12

% Define and custom the network


% create the network: 1 input, 2 layer (1 hidden layer and 1 output layer), feed-forward network
net = network( ...
1, ... % numInputs (number of inputs)
2, ... % numLayers (number of layers)
[1; 0], ... % biasConnect (numLayers-by-1 Boolean vector)
[1; 0], ... % inputConnect (numLayers-by-numInputs Boolean matrix)
[0 0; 1 0], ... % layerConnect (numLayers-by-numLayers Boolean matrix); [a b; c d]
... % a: 1st-layer with itself, b: 2nd-layer with 1st-layer,
... % c: 1st-layer with 2nd-layer, d: 2nd-layer with itself
[0 1] ... % outputConnect (1-by-numLayers Boolean vector)
);
% View network structure
view(net);


% We can then see the properties of sub-objects as follows:
net.inputs{1}
net.layers{1}, net.layers{2}
net.biases{1}
net.inputWeights{1}, net.layerWeights{2}
net.outputs{2}

% Define topology and transfer function

% number of hidden layer neurons
net.layers{1}.size = 5;
% hidden layer transfer function
net.layers{1}.transferFcn = 'logsig';
view(net);


% Configure the network

net = configure(net,inputs,outputs);
view(net);

%Train net and calculate neuron output

% initial network response without training
initial_output = net(inputs)
%We can get the weight matrices and bias vector as follows:
net.IW{1}
net.LW{2}
net.b{1}

% network training
net.trainFcn = 'trainlm'; % trainlm: Levenberg-Marquardt backpropagation
% trainlm is often the fastest backpropagation algorithm in the toolbox, and is highly %recommended
%as a first choice supervised algorithm for regression, although it does %require more memory than
%other algorithms, as for example traingdm (Gradient descent %with momentum backpropagation) or
%traingdx (Gradient descent with momentum and %adaptive learning rate backpropagation).
net.performFcn = 'mse';



net = train(net,inputs,outputs);
% final weight matrices and bias vector:
net.IW{1}
net.LW{2}
net.b{1}


net(1) % For 1 as input the outputs should be close to 7
net(2) % For 1 as input the outputs should be close to 8
net(3) % For 1 as input the outputs should be close to 9
net(4) % For 1 as input the outputs should be close to 10
net(5) % For 1 as input the outputs should be close to 11
net(6) % For 1 as input the outputs should be close to 12


