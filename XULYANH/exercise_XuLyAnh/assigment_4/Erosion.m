image = imread('fingerprint.tif');
SE = strel('line',3,0);
a = imerode(image,SE);
b = imdilate(a,SE);
figure, subplot(1,3,1), imshow(image), title('Original');
subplot(1,3,2), imshow(a), title('Erode');
subplot(1,3,3),imshow(b), title('Dilate');