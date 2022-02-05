% *************************************************************************
% Find the minimum of the Rosenbrock function by comparing different values 
% of the following operators: population size, number of generations, 
% initial range, selection and reproduction (crossover and mutation).

%% 1. Genetic algorithm
close all; clear; clc;
tic

%rng default

FitnessFunction = @(x)(1-x(1))^2+100*(x(2)-x(1)^2)^2;
numberOfVariables = 2;


Z_ga=[];
XY_ga=[];

% Then the parameters were iterated 1000 for each of the following parameters:
% -Crossover fraction
% -MaxGenerations
% -Population size
% -Selection function
% -Initial range

%% Solve for crossover fraction
% If you want to run this part of the code, comment the lines 152 until
% 158, then uncomment the next lines

% iter = 1000;
% fval_vec = zeros(1,iter);
% for n=0:.05:1
%     for i=1:iter
%         options = optimoptions('ga','MaxGenerations',200);
%         options = optimoptions(options,'CrossoverFraction',n);
%         [solution,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
%         [],[],[],[],options);
%         fval_vec(i) = fval;
%     end
%     Z_ga = [Z_ga; mean(fval_vec)];
%     XY_ga = [XY_ga; solution];
% end
% 
% plot(0:0.05:1,Z_ga)
% xlabel('Crossover fraction')
% ylabel('Fval')

crossFraction = 0.55;       % This result was the best for 1000 iterations

%% Solve for MaxGenerations
% If you want to run this part of the code, comment the lines 152 until
% 158, then uncomment the next lines

% n0 = 20;
% ni = 10;
% nf = 200;
% iter = 1000;
% fval_vec = zeros(1,iter);
% for n=n0:ni:nf
%     for i=1:iter
%         
%         options = optimoptions('ga','MaxGenerations',n);
%         options = optimoptions(options,'CrossoverFraction',crossFraction);
%         [solution,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
%         [],[],[],[],options);
%         fval_vec(i) = fval;
%     end
%     Z_ga = [Z_ga; mean(fval_vec)];
%     XY_ga = [XY_ga; solution];
% end
% 
% plot(n0:ni:nf,Z_ga)
% xlabel('Crossover fraction')
% ylabel('Fval')


gen = 100;       % This result was the best for 1000 iterations

%% Solve for population size
% If you want to run this part of the code, comment the lines 152 until
% 158, then uncomment the next lines

% n0 = 1;
% ni = 2;
% nf = 50;
% iter = 1000;
% fval_vec = zeros(1,iter);
% for n=n0:ni:nf
%     for i=1:iter
%         options = optimoptions('ga','PopulationSize',n,...
%             'MaxGenerations',gen,'CrossoverFraction',crossFraction);
%         [solution,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
%         [],[],[],[],options);
%         fval_vec(i) = fval;
%     end
%     Z_ga = [Z_ga; mean(fval_vec)];
%     XY_ga = [XY_ga; solution];
% end
% 
% plot(n0:ni:nf,Z_ga)
% xlabel('Population size')
% ylabel('Fval')

popSize = 50;               % This result was the best for 1000 iterations

%% Solve for selection function
% If you want to run this part of the code, comment the lines 152 until
% 158, then uncomment the next lines

% selFun = {[],'selectionstochunif','selectionremainder','selectionuniform','selectionroulette'};
% iter = 1000;
% fval_vec = zeros(1,iter);
% for n=1:length(selFun)
%     display(selFun{n})
%     for i=1:iter
%         options = optimoptions('ga',"SelectionFcn",selFun{n},...
%             'PopulationSize',popSize,'MaxGenerations',gen,'CrossoverFraction',crossFraction);
%         [solution,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
%         [],[],[],[],options);
%         fval_vec(i) = fval;
%     end
%     Z_ga = [Z_ga; mean(fval_vec)];
%     XY_ga = [XY_ga; solution];
% end
% 
% stem(1:length(selFun),Z_ga')
% ylabel('Fval')
% set(gca,'xticklabel',selFun)
% xtickangle(45)
selFun =  'selectionremainder' ;             % This result was the best for 1000 iterations

%% Solve for initial range
% If you want to run this part of the code, comment the lines 152 until
% 158, then uncomment the next lines

n0 = 1.1;
ni = 0.1;
nf = 3;
iter = 1000;
fval_vec = zeros(1,iter);
for n=n0:ni:nf
    for i=1:iter
        options = optimoptions('ga','InitialPopulationRange',[1;n],...
            "SelectionFcn",selFun,'PopulationSize',popSize,'MaxGenerations',gen,'CrossoverFraction',crossFraction);
        [solution,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
        [],[],[],[],options);
        fval_vec(i) = fval;
    end
    Z_ga = [Z_ga; mean(fval_vec)];
    XY_ga = [XY_ga; solution];
end

plot(n0:ni:nf,Z_ga)
xlabel('Initial range (upper limit)')
ylabel('Fval')


initRange = [1;1.1];

