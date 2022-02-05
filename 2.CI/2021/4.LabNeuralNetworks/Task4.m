%Task 4 - Clasification of linearly separable data with a Rosenblatt's
%perceptron

close all, clear all, clc

% Number of samples of each class
N= 20;
% Define inputs and outputs
offset = 5; % offset for second class
x = [randn(2,N) randn(2,N)+ offset]; %inputs
y = [zeros(1,N) ones(1,N)]; %outputs
%Plot input samples with plotpv (Plot perceptron input/vectors)
figure(1)
plotpv(x,y);

% Now we going to create and train the perceptron

net = perceptron;

% Take a look to the default parameters of this perceptron. Notice that the performance/cost
%function used is mae (mean absolute error), the training function is trainc (trains a network %with
%weight and bias learning rules with incremental updates) and the transfer function %used is hardlim
%(Hard-limit). 


net = train(net, x, y);
view(net)


%Plot decision boundary
figure(1)
plotpc(net.IW{1},net.b{1});




