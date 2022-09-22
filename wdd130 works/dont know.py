//how to fine the volume of a car tire?
volumes = list()
for index in range(0, 50):
    r = z[np.logical_and(zcosmo>index * 0.01, zcosmo<index * 0.01 + 0.01)] / 2
    h = x[np.logical_and(zcosmo>index * 0.01, zcosmo<index * 0.01 + 0.01)]

    volumes.append(math.pi*(r**2)*(h))



