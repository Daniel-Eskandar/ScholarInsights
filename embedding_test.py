import pandas as pd
from gensim.models import KeyedVectors
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D


# TODO: you need to download a word2vec model and put its path here
word_vectors = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)


def get_title_embedding(title, model):
    words = title.lower().split()
    word_embeddings = [model[word] for word in words if word in model]
    
    if word_embeddings:
        title_embedding = np.mean(word_embeddings, axis=0)
        return title_embedding
    else:
        return np.zeros(model.vector_size)
    

def get_professor_embedding(titles, model):
    title_embeddings = [get_title_embedding(title, model) for title in titles]
    professor_embedding = np.mean(title_embeddings, axis=0)
    return professor_embedding





directory = 'Data'
high_dim_vecs = []
vec_names = []
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        print(f"Processing {file_path}")

        df = pd.read_csv(file_path)
        paper_titles = list(df[df['year']>=2019]['title'])

        vec = np.array(get_professor_embedding(paper_titles, word_vectors))
        
        high_dim_vecs.append(vec)
        vec_names.append(filename)


"""# 2D vector space
print(high_dim_vecs)

high_dim_vecs = np.array(high_dim_vecs)

pca = PCA(n_components=2)
reduced_vectors_pca = pca.fit_transform(high_dim_vecs)  # Replace with your vectors

# Using PCA
plt.scatter(reduced_vectors_pca[:, 0], reduced_vectors_pca[:, 1])

# Adding names to points
for i, name in enumerate(vec_names):
    plt.text(reduced_vectors_pca[i, 0], reduced_vectors_pca[i, 1], name)

plt.title('PCA Reduction')
plt.show()
"""

# Assuming high_dim_vecs is your list of vectors
high_dim_vecs = np.array(high_dim_vecs)

# Use PCA with 3 components
pca = PCA(n_components=3)
reduced_vectors_pca = pca.fit_transform(high_dim_vecs)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for 3D data
ax.scatter(reduced_vectors_pca[:, 0], reduced_vectors_pca[:, 1], reduced_vectors_pca[:, 2])

# Adding names to points
for i, name in enumerate(vec_names):
    ax.text(reduced_vectors_pca[i, 0], reduced_vectors_pca[i, 1], reduced_vectors_pca[i, 2], name)

plt.title('PCA 3D Reduction')
plt.show()

