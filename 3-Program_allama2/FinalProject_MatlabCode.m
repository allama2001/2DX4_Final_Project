f2 = load('C:\Users\abdul\Downloads\2dx4_dsA0-1 Python Code1\2dx4_dsA0-1 Python Code\projectfile2dx4.xyz');
    CX = f2(:,1);
    CY = f2(:,2);
    CZ = f2(:,3);
     
    plot3(CY,CX,CZ);
    
    xlabel('This is y axis');
    ylabel('Displacement');
    zlabel('This is z-axis');
    grid on;
    axis normal;
   