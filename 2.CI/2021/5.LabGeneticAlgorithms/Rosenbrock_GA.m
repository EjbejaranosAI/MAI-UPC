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

popSize = 49;               % This result was the best for 1000 iterations

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

% n0 = 1.1;
% ni = 0.1;
% nf = 3;
% iter = 1000;
% fval_vec = zeros(1,iter);
% for n=n0:ni:nf
%     for i=1:iter
%         options = optimoptions('ga','InitialPopulationRange',[1;n],...
%             "SelectionFcn",selFun,'PopulationSize',popSize,'MaxGenerations',gen,'CrossoverFraction',crossFraction);
%         [solution,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
%         [],[],[],[],options);
%         fval_vec(i) = fval;
%     end
%     Z_ga = [Z_ga; mean(fval_vec)];
%     XY_ga = [XY_ga; solution];
% end
% 
% plot(n0:ni:nf,Z_ga)
% xlabel('Initial range (upper limit)')
% ylabel('Fval')


initRange = [1;1.1];


%% Solve with the better parameters
% If you want to run this part of the code, comment the previus parts
% ,then uncomment the next lines
options = optimoptions('ga','InitialPopulationRange',initRange,...
        "SelectionFcn",selFun,'PopulationSize',popSize,'MaxGenerations',gen,'CrossoverFraction',crossFraction,'PlotFcn',{'gaplotstopping','gaplotbestf','gaplotbestindiv'});
    [solution,fval,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],...
    [],[],[],[],options);

Z_ga = [Z_ga; fval];
XY_ga = [XY_ga; solution];
%% 2. Plot the surface
% Top plot

 f = @(x,y) (1-x).^2 + 100*(y-x.^2).^2;

 x = linspace(-2,2); y = linspace(-1,3);
 [xx,yy] = meshgrid(x,y); ff = f(xx,yy);
 levels = 10:10:300;
 LW = 'linewidth'; FS = 'fontsize'; MS = 'markersize';

 figure, contour(x,y,ff,levels,LW,1.2), colorbar
 axis([-2 2 -1 2]), axis square, hold on


 fminx0 = @(x0) min(chebfun(@(y) f(x0,y),[-1 3]));
    
%Global minimun for the 2d surface

 gm = plot3(XY_ga(:,1),XY_ga(:,2),Z_ga,'p','Color','r','MarkerSize',10)
 legend(gm,'Global minimum','Location','best');
 ylabel('fval')
 xlabel('Crossover Fraction');

 %% 3. Plot 3d function with the global minimum


x = -2.:0.05:2.;
y = -1.:0.05:3.;
n = length(x);
m = length(y);
[X,Y] = meshgrid(x,y);
Z = zeros(n,m);

for i = 1:n
    for j = 1:m
        Z(i,j) =  (1-X(i,j))^2 + 100*(Y(i,j)-X(i,j)^2)^2;
    end
end

figure
colormap (flipud(jet))
C = log10(Z);
s = surf(X,Y,Z,C);
s.EdgeColor = 'none';

hold on     

h1= plot3(XY_ga(:,1),XY_ga(:,2),Z_ga,'*','Color','r','MarkerSize',15);
legend(h1,'Global minimum','Location','best');
strm = RandStream.getGlobalStream;
%strm.State = Output.rngstate.State;
[x,Fval,exitFlag,Output] = ga(FitnessFunction,numberOfVariables);




%% Results

fprintf('\n')
% The parameters found was:
fprintf('The parameters found were:')
fprintf('\n')
% -Crossover fraction
fprintf('Crossover fraction : %d\n', crossFraction)
% -MaxGenerations
fprintf('MaxGenerations : %d\n', gen)
% -Population size
fprintf('Population size : %g\n', popSize)
% -Selection function
fprintf('Selection function : selectionremainder')
% -Initial range
fprintf('Initial range : %g\n', initRange)

fprintf('\n')
fprintf('\n')
fprintf('The number of generations was : %d\n', Output.generations)
fprintf('The number of function evaluations was : %d\n', Output.funccount)
fprintf('The best function value found was : %g\n', fval)
% Clear variables
clearvars options

toc