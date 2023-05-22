import numpy as np

if __name__ == "__main__":
    arr=np.array([[1,2],[3,4]])
    e_value,e_vector=np.linalg.eig(arr)
    deter=np.linalg.det(arr)

    vec1=[1,2,3]
    vec2=[4,5,6]
    cp=np.cross(vec1,vec2)

    A=([[1,2,-2],[2,1,-5],[1,-4,1]])
    b=([-15,-21,18])
    x=np.linalg.solve(A,b)
    x_row=np.reshape(x,(-1,1))

    print("Eigenvalues:",e_value)
    print("Eigenvectors:\n",e_vector)
    print("Determinant:",deter)
    print("Cross product:",cp)
    print("Solution:\n",x_row)