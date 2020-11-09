% Simulate a uniform Poisson line process on a disk.
% Author: H. Paul Keeler, 2019.
% Website: hpaulkeeler.com
% Repository: github.com/hpaulkeeler/posts
% For more details, see the post:
% hpaulkeeler.com/simulating-a-poisson-line-process/

close all; clearvars; clc;

%%%START Parameters START%%%
%Poisson line process parameters
lambda=4; %intensity (ie mean density) of the Poisson line process

%Simulation disk dimensions
xx0=0; yy0=0; %center of disk
r=1; %disk radius
massLine=2*pi*r*lambda; %total measure/mass of the line process
%%%END Parameters END%%%

%%%START Simulate a Poisson line process on a disk START%%%
%Simulate Poisson point process
numbLines=poissrnd(massLine);%Poisson number of lines
theta=2*pi*rand(numbLines,1); %choose angular component uniformly
p=r*rand(numbLines,1); %choose radial component uniformly
q=sqrt(r.^2-p.^2); %distance to circle edge (alonge line)

%calculate trig values
sin_theta=sin(theta);
cos_theta=cos(theta);

%calculate segment endpoints of Poisson line process
xx1=xx0+p.*cos_theta+q.*sin_theta;
yy1=yy0+p.*sin_theta-q.*cos_theta;
xx2=xx0+p.*cos_theta-q.*sin_theta;
yy2=yy0+p.*sin_theta+q.*cos_theta;
%%%END Simulate a Poisson line process on a disk END%%%


%%% START Plotting %%%START
%draw circle
t=linspace(0,2*pi,200);
xp=xx0+r*cos(t); yp=yy0+r*sin(t);
plot(xp,yp,'k');
axis square; hold on;
axis tight;
xticks([]);yticks([]);
set(gca,'Visible','off');

%plot segments of Poisson line process
plot([xx1';xx2'],[yy1';yy2'],'b','LineWidth',2);
%%%END Plotting END%%%

