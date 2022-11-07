from plotter import Plotter
import csv  
from rca import *


class Polygon():

    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.data = []
        self.testing_data = []


    """ read polygon.csv """
    def read_polygon_data(self):
        try:
            with open(self.path_to_data) as f:
                rd = f.readlines()
            for a in rd[1:]:
                a = a.replace('\n', '').split(',')[:]
                a = tuple(map(float, (a)))
                self.data.append(a)
        except Exception as e:
            print(e)
        return self.data


    """ read input.csv """
    def testing_points(self, path_to_testing_data):
        with open(path_to_testing_data) as f:
            rd = f.readlines()
        for a in rd[1:]:
            a = a.replace('\n', '').split(',')[:]
            a = tuple(map(float, (a)))
            self.testing_data.append(a)
        return self.testing_data


    """ categorize points using minimum bounding rectangle """
    def create_mbr_multiple_points(self, category_data):
        categorize = []
        try:
            xs = [point[1] for point in self.data]
            ys = [point[2] for point in self.data]
            maxX = max(xs)
            minX = min(xs)
            maxY = max(ys)
            minY = min(ys)
            mbr = [[maxX, maxY], [minX, minY]]
            for ac in category_data:
                if (minX <= ac[0] <= maxX ) and (minY <= ac[1] <= maxY):
                    acs = list(ac)+ ['inside']
                    categorize.append(acs)
                else:
                    ac = list(ac) + ['outside']
                    categorize.append(ac)
        except Exception as e:
            print(e)
        return categorize


    """ categorize points using minimum bounding rectangle """
    def create_point_mbr(self, point):
        try:
            xs = [point[1] for point in self.data]
            ys = [point[2] for point in self.data]
            maxX = max(xs)
            minX = min(xs)
            maxY = max(ys)
            minY = min(ys)
            mbr = [[maxX, maxY], [minX, minY]]
            if (minX <= point[0] <= maxX ) and (minY <= point[1] <= maxY):
                point = point + ['inside']
            else:
                point = point + ['outside']
        except Exception as e:
            print(e)
        return point        


    """ categorize points using ray casting """
    def create_rca_category(self, point):
        try:
            polys = self.data[:]
            # Function call
            if checkInside(polys, len(polys), point):
                point = list(point) + ['inside']
            else:
                point =  list(point) + ['outside']
        except Exception as e:
            print(e)
        return point


    """ write output.csv """
    def write_category_to_csv(self, category_data):
        with open('n_output2.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['x', 'y', 'category'])
            writer.writerows(category_data)



def main():
    plotter = Plotter()

    #read polygon.csv 
    poly = Polygon('polygon.csv')
    read_data = poly.read_polygon_data()
    
    #read input.csv
    testing_points = poly.testing_points('input.csv')

    #categorize points
    create_mbr = poly.create_mbr_multiple_points([a[1:] for a in testing_points])
    create_rca_category = [poly.create_rca_category(a[1:]) for a in testing_points]

    #write output.csv
    poly.write_category_to_csv(create_rca_category)

    #plot polygon and points
    for a in create_mbr:
        plotter.add_point(a[0], a[1], a[2])
    xs = [point[1] for point in read_data]
    ys = [point[2] for point in read_data]
    plotter.add_polygon(xs, ys)
    plotter.show()


if __name__ == '__main__':
    main()
