net.divideFcn = 'dividerand';% divideFCN allow to change the way the data is
% divided into training, validation and test
% data sets.
net.divideParam.trainRatio = 0.1; % Ratio of data used as training set
net.divideParam.valRatio = 0.1;
% Ratio of data used as validation set
net.divideParam.testRatio = 0.8; % Ratio of data used as test set
net.trainParam.max_fail = 6; % validation check parameter
net.trainParam.epochs=2000; % number of epochs parameter
net.trainParam.min_grad = 1e-5 % minimum performance gradient
% you can define different transfer functions for each layer (layer{1} and
% layer{2}). You can take a look to this parameter in Matlab to see all
% functions available
net.layers{1}.transferFcn = 'logsig';
net.layers{1}.transferFcn = 'tansig';
net.layers{2}.transferFcn = 'softmax';
net.layers{2}.transferFcn = 'logsig';
% you can define different cost/performance functions. You can take a look to
% this parameter in Matlab to see all functions available
net.performFcn='crossentropy';
net.performFcn='mse';






%you can use different Training functions. You can take a look to this
%parameter in Matlab to see all functions available.
%Notice that trainlm is often the fastest backpropagation algorithm in the
%toolbox, and is highly recommended as a first choice supervised algorithm
%for regression, although it does require more memory than other
%algorithms, as for example traingdm or traingdx.
net.trainFcn= 'trainlm';
net.trainFcn= 'traingdm';
net.trainFcn= 'traingdx';




%Levenberg-Marquardt
%Gradient Descent with momentum
%Gradient descent with momentum and adaptive
%learning rate backpropagation

% If you chose training functions that use momentum and learning rate, you
% need to set these parameters too.
net.trainParam.mc = 0.8; % momentum parameter
net.trainParam.lr = 0.01; % learning rate parameter