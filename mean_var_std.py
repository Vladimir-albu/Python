import numpy as np


def calculate(list):
  if (len(list) == 9 and (all(isinstance(i, int) for i in list))):
    tab = np.array(list).reshape((3, 3))
    return ({
      'mean': [(np.sum(tab, axis=0) / 3).tolist(),
               (np.sum(tab, axis=1) / 3).tolist(),
               np.sum(tab) / 9],
      'variance': [
        np.var(tab, axis=0).tolist(),
        np.var(tab, axis=1).tolist(),
        np.var(tab)
      ],
      'standard deviation': [
        np.std(tab, axis=0).tolist(),
        np.std(tab, axis=1).tolist(),
        np.std(tab)
      ],
      'max': [
        np.max(tab, axis=0).tolist(),
        np.max(tab, axis=1).tolist(),
        np.max(tab)
      ],
      'min': [
        np.min(tab, axis=0).tolist(),
        np.min(tab, axis=1).tolist(),
        np.min(tab)
      ],
      'sum': [
        np.sum(tab, axis=0).tolist(),
        np.sum(tab, axis=1).tolist(),
        np.sum(tab)
      ]
    })
  else:
    raise ValueError("List must contain nine numbers.")

    return calculations
