import numpy as np

if __name__ == "__main__":
    Docs=([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    Query=([1,1,0,0,1,0])

    dot_product = np.dot(Docs, Query)

    Docs_norm = np.linalg.norm(Docs, axis=1)
    Query_norm = np.linalg.norm(Query)

    similarity = dot_product / (Docs_norm * Query_norm)

    print("doc1={:.2f}".format(similarity[0]))
    print("doc2={:.2f}".format(similarity[1]))
    print("doc3={:.2f}".format(similarity[2]))
   
