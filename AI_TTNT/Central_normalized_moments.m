function M = Central_normalized_moments(img,p,q)
    m = Central_moments(img,p,q);
    S = Central_moments(img,0,0);
    M = m/(S^(((p+q)/2)+1));
end