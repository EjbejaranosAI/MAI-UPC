%% Generate 51 input-output pairs 
% between x ϵ[-10, 10], and choose 
% training and checking data sets:


numPts=51;
x=linspace(-10,10,numPts)';
y=-2*x-x.^2;
data=[x y];
trndata=data(1:2:numPts,:);
chkdata=data(2:2:numPts,:);

% Take a look to the training output:
plot(trndata(:,1),trndata(:,2),'*r')

% and the cheking output:
hold on
plot(chkdata(:,1),chkdata(:,2),'*b')

% Set the number and type of 
% membership functions:

numMFs=5;
mfType='gbellmf';

