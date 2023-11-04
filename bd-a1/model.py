from sklearn.cluster import KMeans


df = globals()["df"]

X = df
y = df['Customer Status']
kmeans = KMeans(n_clusters=3, random_state=0) 

kmeans.fit(X)

labels = kmeans.labels_
cluster_count = 1
text = ""
for label in set(labels):
  count = len([x for x in labels if x == label])
  text += f"Cluster {cluster_count}: {count} data points\n"
  cluster_count+=1

f = open("k.txt", "a")
f.write(text)
f.close()


print("Pipeline Finished! Run final.sh to transfer data and close the container.")
