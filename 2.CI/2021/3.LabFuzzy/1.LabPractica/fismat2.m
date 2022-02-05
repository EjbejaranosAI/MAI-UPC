%Task5
%%Copy and page code in AnfisModel.m
numPts = 51;
x = linspace(-10,10,numPts)';
y = -2*x-x.^2;
data = [x y];
trndata = data(1:2:numPts,:);
chkdata=data(2:2:numPts,:);

%Take a look to the training output

plot(trndata(:,1),trndata(:,2),'*r')

% and the cheking output:
hold on
plot(chkdata(:,1),chkdata(:,2),'*b')

% Set the number and type of membership funciotns:
numMFs = 10;
mfType='trimf';

fismat=(genfis1(trndata,numMFs,mfType))
numEpochs=40;
[fismat1,trnErr,ss,fismat2,chkErr]=anfis(trndata,fismat,numEpochs,NaN,chkdata);


anfis_y=evalfis(x(:,1),fismat1);
plot(trndata(:,1),trndata(:,2),'o',chkdata(:,1),chkdata(:,2),'x',x,anfis_y,'-')


hold on;
plot(x,y)

writefis(fismat1,'fismat1')