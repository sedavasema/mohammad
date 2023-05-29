def my_plot2(X,cluster_lab,db):
  # Number of clusters in labels, ignoring noise if present.
  n_clusters_ = len(set(cluster_lab)) - (1 if -1 in cluster_lab  else 0)
  n_noise_ = list(cluster_lab).count(-1)

  print("Estimated number of clusters: %d" % n_clusters_)
  print("Estimated number of noise points: %d" % n_noise_)
  unique_labels = set(cluster_lab)
  core_samples_mask = np.zeros_like(cluster_lab, dtype=bool)
  core_samples_mask[db.core_sample_indices_] = True

  min_x=min(X[:,0])
  max_x=max(X[:,0])
  min_y=min(X[:,1])
  max_y=max(X[:,1])
  plt.xlim(min_x-1,max_x+1)
  plt.ylim(min_y-1,max_y+1)
  
  plt.xticks(np.arange(min_x-1,max_x+1 , 1))
  plt.yticks(np.arange(min_y-1,max_y+1 , 1))

  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
  colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
  for k, col in zip(unique_labels, colors):
      if k == -1:
          # Black used for noise.
          col = [0, 0, 0, 1]

      class_member_mask = cluster_lab == k

      xy = X[class_member_mask & core_samples_mask]
      plt.plot(
          xy[:, 0],
          xy[:, 1],
          "o",
          markerfacecolor=tuple(col),
          markeredgecolor="k",
          markersize=14,
      )

      xy = X[class_member_mask & ~core_samples_mask]
      plt.plot(
          xy[:, 0],
          xy[:, 1],
          "o",
          markerfacecolor=tuple(col),
          markeredgecolor="k",
          markersize=6,
      )
  plt.legend(['Clusters','Border Cluster'])
  plt.title(f"Estimated number of clusters: {n_clusters_}")
  plt.show()
