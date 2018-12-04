%Simulate a Thomas cluster point process on a rectangle
%Author: H. Paul Keeler, 2018.

%Simulation window parameters
xMin=-.5;xMax=.5;
yMin=-.5;yMax=.5;
xDelta=xMax-xMin;yDelta=yMax-yMin; %rectangle dimensions
areaTotal=xDelta*yDelta; %area of rectangle

%Parameters for the parent and daughter point processes 
lambdaParent=10;%density of parent Poisson point process
lambdaDautgher=100;%mean number of points in each cluster
sigma=0.1;%sigma for normal variables (ie random locations) of daughters

%Simulate Poisson point process for the parents
numbPointsParent=poissrnd(areaTotal*lambdaParent,1,1);%Poisson number of points
%x and y coordinates of Poisson points for the parent
xxParent=xMin+xDelta*rand(numbPointsParent,1);
yyParent=yMin+yDelta*rand(numbPointsParent,1);

%Simulate Poisson point process for the daughters (ie final poiint process)
numbPointsDaughter=poissrnd(lambdaDautgher,numbPointsParent,1); 
numbPoints=sum(numbPointsDaughter); %total number of points

%Generate the (relative) locations in Cartesian coordinates by 
%simulating independent normal variables
xx0=normrnd(0,sigma,numbPoints,1);
yy0=normrnd(0,sigma,numbPoints,1);

%replicate parent points (ie centres of disks/clusters) 
xx=repelem(xxParent,numbPointsDaughter);
yy=repelem(yyParent,numbPointsDaughter);
%translate points (ie parents points are the centres of cluster disks)
xx=xx(:)+xx0;
yy=yy(:)+yy0;

%Plotting
scatter(xx,yy);
shg;