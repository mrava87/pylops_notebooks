det _rmatvec(x):
    x = x.squeeze()
    y = np.zeros(self.N, self.dtype)
    y[0:-2] -= (0.5 * x[1:-1]) / self.sampling
    y[2:] += (0.5 * x[1:-1]) / self.sampling
    if self.edge:
        y[0] -= x[0] / self.sampling
        y[1] += x[0] / self.sampling
        y[-2] -= x[-1] / self.sampling
        y[-1] += x[-1] / self.sampling