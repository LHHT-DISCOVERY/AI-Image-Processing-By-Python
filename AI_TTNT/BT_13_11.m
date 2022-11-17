clear;
clc;
%doc nhieu file anh :
imagefiles = dir('bitmap\*.jpg');      
nfiles = length(imagefiles);
for j=1: nfiles
    currentfilename = ['bitmap\' num2str(j) '.jpg'];
    img = imread(currentfilename);
    % moment trung tam:
    m02 = Central_moments(img,0,2);
    m20 = Central_moments(img,2,0);
    m11 = Central_moments(img,1,1);
    m30 = Central_moments(img,3,0);
    m03 = Central_moments(img,0,3);
    m12 = Central_moments(img,1,2);
    m21 = Central_moments(img,2,1);
    %Central_moments(0,0)
    
    % moment trung tam chuan hoa :
    M02 = Central_normalized_moments(img,0,2);
    M20 = Central_normalized_moments(img,2,0);
    M11 = Central_normalized_moments(img,1,1);
    M30 = Central_normalized_moments(img,3,0);
    M03 = Central_normalized_moments(img,0,3);
    M12 = Central_normalized_moments(img,1,2);
    M21 = Central_normalized_moments(img,2,1);
    % Hu moment  :
    S1 = M20 + M02;
    S2 = (M20 - M02)*(M20 + M02)+(4*M11*M11);
    S3 = ((M30 - 3*M12)^2) + ((M30 - 3*M21)^2);
    S4 = ((M30 + M12)^2) + ((M03 + M21)^2);
    S5 = (M30 - 3*M12)*(M30 + M12)*(((M30 + M12)^2) - 3*((M03 + M21)^2)) + (3*M21 - M03)*(M03 + M21)*(3*((M30+M12)^2) - ((M03+M21)^2));
    S6 = (M20-M02)*(((M30 + M12)^2) - ((M03+M21)^2)) + 4*M11*(M30+M12)*(M03+M21);
    S7 = (3*M21-M03)*(M30+M12)*(((M30+M12)^2) - 3*(M03+M21)^2)+(M30-3*M12)*(M21+M02)*(3*((M30+M12)^2) - (M03+M21)^2);
    
    Hu_moment(j,:) = [S1 S2 S3 S4 S5 S6 S7];

end
y = ['dau';'dau';'dau';'dau';'dau';'dau';'dau';'dau';'dau';'dau';'cam';'cam';'cam';'cam';'cam';'cam';'cam';'cam';'cam';'cam'];

ds = mat2dataset(Hu_moment);
ds(1:20,:);
ds.loai = nominal(y);
ds(1:20,:);
DS = dataset2table(ds)
% 5-fold cross validation :
A = [1,2, 11,12;
    3,4, 13,14;
    5,6, 17,18;
    7,8, 15,16;
    9,10, 19,20];
B = ones(5,4);
C = [1,1, 2,2;
     1,1, 2,2;
     1,1, 2,2;
     1,1, 2,2;
     1,1, 2,2];
K = 3;
dau = 0;
cam = 0;
for i = 1:5
    DS2 = DS;
    DS2([A(i,1),A(i,2),A(i,3),A(i,4)] , :)=[]; 
    %training data :
    Hu_moment_train = DS2(:,1:7);
    y_train = DS2(:,8);
    %--------------------------------------------------------------------
    % Model KNN:
        %Mdl = fitcknn(Hu_moment_train,y_train,'NumNeighbors',3,'Standardize',1);
    %test :
        %         if (string(predict(Mdl,Hu_moment(A(i,j),:))) == "cam")
        %             B(i,j) = 2;
        %         elseif (string(predict(Mdl,Hu_moment(A(i,j),:))) == "dau")
        %             B(i,j) = 1;
        %         end
      for j = 1 : 4
            for k = 1 : 16
                d(j,k) = norm(Hu_moment(A(i,j),:)-table2array(Hu_moment_train(k,:)));
                if (table2array(y_train(k,:)) == 'dau' )
                    e(j,k) = 1;
                elseif (table2array(y_train(k,:)) == 'cam' )
                    e(j,k) = 2;
                end
            
            end
        
      end
            d1 = sort(d,2);
            for I= 1 : size(d1,1)
                for J =1 : size(d1,2)
                        d2(I,J) = e(d1(I,J)==d);
                end
            end
            d2 = d2(:,1:K);
            for i1 = 1 : size(d2,1)
                for j1 = 1 : K
                    if (d2(i1,j1) == 1)
                        dau = dau + 1;
                    elseif (d2(i1,j1) == 2)
                        cam = cam + 1;
                    end
                end
                if (dau >= cam) 
                    KQ(i,i1) = 1;
                elseif (cam > dau)
                    KQ(i,i1) = 2;
                end
                dau = 0;
                cam = 0;
            end
end
% Confusion Matrix :
kq = KQ';
kq = kq(:)';
c = C';
c = c(:)';

D = confusionmat(c,kq);
F = confusionchart(D)
%--------------------------------------------------------------------
% ACC :
acc = sum(kq == c, 'all') / 20
%--------------------------------------------------------------------
