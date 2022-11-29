clear;clc;
im=imread('Text.bmp');
[row, col]=size(im);
subplot(3,2,1);
imshow(im);
title('Original Image');
%% Histogram
h=histogram(im);
subplot(3,2,2);
% plot(h);
title('Image Histogram');
%% Threshold
for i=1:row
    for j=1:col
        if im(i,j)<100
            output(i,j)=0;
        else
            output(i,j)=255;
        end
    end
end
output=uint8(output);
h2=histogram(output);
subplot(3,2,3);
imshow(output);
title('Image after Thresholding');
%% Erosion
eout=[255*ones(1,col);output;255*ones(1,col)];
eout=[255*ones(row+2,1) eout 255*ones(row+2,1)];

kernel=[0 1 0
        1 1 1
        0 1 0];
[krow,kcol]=size(kernel);

for m=1:5
    for i=1:row
        for j=1:col
            sum=0;
            for k=1:krow
                for l=1:kcol
                    if eout(i-1+k,j-1+l)==0
                        sum=sum+1*kernel(4-k,4-l);
                    end
                end
            end
            if sum>=5
                eout(i,j)=0;
            else eout(i,j)=255;
            end
        end
    end
end
eout=eout(1:row,1:col);
eout=uint8(eout);
subplot(3,2,4);
 imshow(eout);
 title('Image after Erosion');
%% Dilation
dout=[255*ones(1,col);eout;255*ones(1,col)];
dout=[255*ones(row+2,1) dout 255*ones(row+2,1)];
dkernel=[0 1 0
        1 1 1
        0 1 0];
[drow,dcol]=size(dkernel);
for m=1:5
    for i=1:row
        for j=1:col
            sum=0;
            for k=1:drow
                for l=1:dcol
                    if dout(i-1+k,j-1+l)==0
                        sum=sum+1*dkernel(4-k,4-l);
                    end
                end
            end
            if sum>=1
                dout(i,j)=0;
            else dout(i,j)=255;
            end
        end
    end
end
dout=dout(1:row,1:col);
dout=uint8(dout);
subplot(3,2,5);
imshow(dout);
title('Image after Dilation');

%% Absolute difference
diff=zeros(row,col);
diff=abs(double(output-dout));

diff=uint8(diff);
subplot(3,2,6);
imshow(diff);
title('Absolute difference');