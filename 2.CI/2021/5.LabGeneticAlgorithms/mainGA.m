% *************************************************************************
% Find the minimum of the Rosenbrock function by comparing different values 
% of the following operators: population size, number of generations, 
% initial range, selection and reproduction (crossover and mutation).

%**************** FIRST CONFIGURATION OF THE GENETIC ALGORITHM*************
% *************************************************************************
%% 1. Genetic algorithm
close all; clear; clc;


FitnessFunction = @(x)(1-x(1))^2+100*(x(2)-x(1)^2)^2;

numberOfVariables = 10;

opts = gaoptimset('PlotFcns',{@gaplotbestf,@gaplotstopping});
%opts = gaoptimset('PlotFcns',{@gaplotbestf,@gaplot1drange});

%opts = gaoptimset(opts,'HybridFcn',{@fminunc, opts});
opts = gaoptimset(opts,'PopulationSize',500);
opts = gaoptimset(opts,'Generations',50,'StallGenLimit', 600);
opts = gaoptimset(opts, 'SelectionFcn',@selectiontournament, 'FitnessScalingFcn',@fitscalingprop);
opts = gaoptimset(opts,'PopulationType', 'bitstring', 'OutputFcns',@my_view);
% opts = gaoptimset(opts,'InitialPopulation',50);
opts = gaoptimset(opts,'PopInitRange',[-2 -2; 2 2]);
opts = gaoptimset(opts, 'SelectionFcn',@selectiontournament, 'FitnessScalingFcn',@fitscalingprop);
%opts.InitialPopulationRange = [-10 0; 1 200];
%opts = gaoptimset(opts,'MaxGenerations',300,'MaxStallGenerations', 100);



%% 2. Evaluation and plot the GA algorithm

Z_ga=[];
XY_ga=[];

rng default
for n=0:.3:1
% for n=0:.05:1    
    opts = gaoptimset(opts,'CrossoverFraction',n);
    [x,fval,exitFlag,Output,population,scores] = ga(FitnessFunction,numberOfVariables,[],[],[],[],[],[],[],opts)
    
    hold on
    Z_ga = [Z_ga; fval];
    XY_ga = [XY_ga; x];
end

fprintf('The number of generations was : %d\n', Output.generations)
fprintf('The number of function evaluations was : %d\n', Output.funccount)
fprintf('The best function value found was : %g\n', fval)


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
strm.State = Output.rngstate.State;
[x,Fval,exitFlag,Output] = ga(FitnessFunction,numberOfVariables);