function board_cutter
%BOARD_CUTTER Optimizes board cuts
%   requires the matlab allcomb function and the optimization toolbox

cuts = [44 49 44.5];
quantity = [4 2 3];
max_length = 96;

% how do we find patterns, let's label our cuts 1,2,3

% say stock size is 8 feet (96) we want to minimize waste

% first let's find patterns

% what is the max number of any cut that will work?
max_num = 2;

% here 3 cuts are hard-coded
M = allcomb([0:max_num], [0:max_num], [0:max_num]);

% now reduce to the feasible solutions
F = M(M*cuts' < max_length, :);

% remove the trivial
F = F(2:end,:);

l = size(F,1);

% now compute the waste
c = max_length - F*cuts';

% now find the solution
x = intlinprog(c',1:l,[], [], F',quantity', zeros(l,1), ones(l,1)*4);

% now pull out solutions
solns = F(x>0,:);
count = x(x>0);
num_solns = size(solns,1);

h = figure('Color',[1 1 1]);
axis off;

% now provide some type of meaningful display
colors = autumn(length(cuts));

for i = 1:num_solns
   cut_string = '';
   soln = solns(i,:);
   waste = max_length - soln*cuts';
   % draw the base
   y=8*(i-1); x=5;
   rectangle('Position', [x,y,96,6]);
   text(x+98,y+3, [num2str(count(i)) ' boards']);
   for j = 1:length(cuts)     
     if soln(j) > 0
      for iCut = 1:soln(j)
        rectangle('Position',[x,y,cuts(j),6],'FaceColor',colors(j,:));
        text(x+cuts(j)/2,y+3,num2str(cuts(j)));
        x = x + cuts(j);
      end      
      s = [num2str(soln(j)) ' cuts of ' num2str(cuts(j)) ' '];
     else
      s = '';
     end
     cut_string = [cut_string s];
   end
   disp(['board: ' num2str(i) ' | quantity: ' num2str(count(i)) ...
       ' | ' cut_string ' waste: ' num2str(waste)]);  
end



disp('----------------------');
disp(['Total waste: ' num2str(c'*x) ' inches']);

end