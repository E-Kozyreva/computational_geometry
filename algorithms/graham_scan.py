import matplotlib.pyplot as plt


class GrahamScan(object):

    def __init__(self, points: list):
        self.points = points
        self.convex_hull = self.graham_scan(points)
    

    def rotate(self, a, b, c) -> int:
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
    

    def graham_scan(self, points: list) -> list:
        n = len(points) 
        p = list(range(n))

        for i in range(1, n):
            if points[p[i]][0] < points[p[0]][0]: 
                p[i], p[0] = p[0], p[i]
        
        for i in range(2, n):
            j = i
            while j > 1 and self.rotate(points[p[0]], points[p[j - 1]], points[p[j]]) < 0:
                p[j], p[j - 1] = p[j - 1], p[j]
                j -= 1
        
        s = [p[0], p[1]]

        for i in range(2, n):
            while self.rotate(points[s[-2]], points[s[-1]], points[p[i]]) < 0:
                del s[-1]
            s.append(p[i])
        return s
    
    
    def draw(self):
        fig, ax = plt.subplots()
        plt.xlabel('Width')
        plt.ylabel('Height')
        plt.title('Graham Scan')
        plt.grid(True)
        plt.xlim(0, 200)
        plt.ylim(0, 200)
        x = [self.points[i][0] for i in range(len(self.points))]
        y = [self.points[i][1] for i in range(len(self.points))]
        ax.scatter(x, y, color='#ffcc00')
        for i in range(len(self.convex_hull)):
            if i == len(self.convex_hull) - 1:
                ax.plot([self.points[self.convex_hull[i]][0], self.points[self.convex_hull[0]][0]], [self.points[self.convex_hull[i]][1], self.points[self.convex_hull[0]][1]], color='#ff9900')
            else:
                ax.plot([self.points[self.convex_hull[i]][0], self.points[self.convex_hull[i + 1]][0]], [self.points[self.convex_hull[i]][1], self.points[self.convex_hull[i + 1]][1]], color='#ff9900')
        ax.fill([self.points[self.convex_hull[i]][0] for i in range(len(self.convex_hull))], [self.points[self.convex_hull[i]][1] for i in range(len(self.convex_hull))], color='#ff9900', alpha=0.3)
        plt.show()
        fig.savefig('F:/university/constructing_minimal_convex_hull/output/graham_scan/graham_scan.png')