function [target] =inputfunction(latest_fprintf)
    upperbound=4;
    lowerbound=1;
    fre=1;
    target=(lowerbound+upperbound)/2+(upperbound-lowerbound)/2*sin(2*pi*fre*latest_fprintf);
end