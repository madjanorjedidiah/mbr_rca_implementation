from plotter import Plotter
from main_from_file import Polygon



def main():
    plotter = Plotter()

    """ read polygon.csv """
    poly = Polygon('polygon.csv')
    read_data = poly.read_polygon_data()

    """ Insert point information """
    x = float(input('x coordinate: '))
    y = float(input('y coordinate: '))

    """ categorize point """
    categorize_mbr = poly.create_point_mbr([x, y])
    categorize_rca = poly.create_rca_category([x, y])

    """ plot polygon and point """
    plotter.add_point(categorize_mbr[0], categorize_mbr[1], categorize_mbr[2])
    xs = [point[1] for point in read_data]
    ys = [point[2] for point in read_data]
    plotter.add_polygon(xs, ys)
    plotter.show()


if __name__ == '__main__':
    main()
