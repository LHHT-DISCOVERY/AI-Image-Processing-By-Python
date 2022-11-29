function m = Central_moments(img,p,q)
m = 0;
img2 = im2bw(img);
S = sum(img2(:));
sizea= size(img2) ;
for i = 1:sizea(1)
    sumy(i) = sum(i*sum(img2(i,:)));
end
sumY = sum(sumy)/S;
for i = 1:sizea(2)
    sumx(i) = sum(i*sum(img2(:,i)));
end
sumX = sum(sumx)/S;
    for i = 1:sizea(1)  
        for j = 1:sizea(2)
            m = ((j-sumX)^p * (i-sumY)^q * img2(i,j)) + m;
        end
    end
end