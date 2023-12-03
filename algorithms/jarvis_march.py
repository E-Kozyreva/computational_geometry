import matplotlib.pyplot as plt


class JarvisMarch(object):
    
    def __init__(self, points: list):
        self.points = points
        self.convex_hull = self.jarvis_march(points)
    

    def rotate(self, a, b, c) -> int:
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
    

    def jarvis_march(self, points: list) -> list:
        n = len(points)
        p = list(range(n))
        for i in range(1, n):
            if points[p[i]][0] < points[p[0]][0]: 
                p[i], p[0] = p[0], p[i]
        h = [p[0]]
        del p[0]
        p.append(h[0])
        while True:
            right = 0
            for i in range(1, len(p)):
                if self.rotate(points[h[-1]], points[p[right]], points[p[i]]) < 0:
                    right = i
            if p[right] == h[0]: 
                break
            else:
                h.append(p[right])
                del p[right]
        return h
    
    
    def draw(self):
        fig, ax = plt.subplots()
        plt.xlabel('Width')
        plt.ylabel('Height')
        plt.title('Jarvis March')
        plt.grid(True)
        plt.xlim(0, 200)
        plt.ylim(0, 200)
        x = [self.points[i][0] for i in range(len(self.points))]
        y = [self.points[i][1] for i in range(len(self.points))]
        ax.scatter(x, y, color='#00bfff')
        for i in range(len(self.convex_hull)):
            if i == len(self.convex_hull) - 1:
                ax.plot([self.points[self.convex_hull[i]][0], self.points[self.convex_hull[0]][0]], [self.points[self.convex_hull[i]][1], self.points[self.convex_hull[0]][1]], color='#1cd3a2')
            else:
                ax.plot([self.points[self.convex_hull[i]][0], self.points[self.convex_hull[i + 1]][0]], [self.points[self.convex_hull[i]][1], self.points[self.convex_hull[i + 1]][1]], color='#1cd3a2')
        ax.fill([self.points[self.convex_hull[i]][0] for i in range(len(self.convex_hull))], [self.points[self.convex_hull[i]][1] for i in range(len(self.convex_hull))], color='#1cd3a2', alpha=0.3)
        plt.show()
        fig.savefig('F:/university/constructing_minimal_convex_hull/output/jarvis_march/jarvis_march.png')