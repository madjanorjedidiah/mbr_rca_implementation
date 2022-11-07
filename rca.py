

def onLine(line ,point):

	 # Check whether p is on the line or not
	if (point[0] <= max(line[0][0], line[1][0]) and point[0] <= min(line[0][0], line[1][0]) and 
		point[1] <= max(line[0][1], line[1][1]) and point[1] <= min(line[0][1], line[1][1])):
		return True;

	return False;


def direction(Point_a, Point_b, Point_c):
	val = (Point_b[1] - Point_a[1]) * (Point_c[0] - Point_b[0]) - (Point_b[0] - 
		Point_a[0]) * (Point_c[1] - Point_b[1])
	if val == 0:
		 # Colinear
		return 0;
	elif val < 0:
		# Anti-clockwise direction
		return 2;
	 # Clockwise direction
	return 1;



def isIntersect(line_l1, line_l2):
	#Four direction for two lines and points of other line
	dir1 = direction(line_l1[0], line_l1[1], line_l2[0])
	dir2 = direction(line_l1[0], line_l1[1], line_l2[1])
	dir3 = direction(line_l2[0], line_l2[1], line_l1[0]);
	dir4 = direction(line_l2[0], line_l2[1], line_l1[1]);

	 # When intersecting
	if dir1 != dir2 and dir3 != dir4:
		return True;

	 # When p2 of line2 are on the line1
	if dir1 == 0 and onLine(line_l1, line_l2[0]):
		return True;

	# When p1 of line2 are on the line1
	if dir2 == 0 and onLine(line_l1, line_l2[1]):
		return True;

	# When p2 of line1 are on the line2
	if dir3 == 0 and onLine(line_l2, line_l1[0]):
		return True;

	 # When p1 of line1 are on the line2
	if dir4 == 0 and onLine(line_l2, line_l2[1]):
		return True;

	return False;


def checkInside(poly, n, p):
	# When polygon has less than 3 edge, it is not polygon
	if n < 3:
		return False;

	# Create a point at infinity, y is same as point p
	exline = [p, (9999, p[1])]
	count = 0;
	i, start = 0, 0;
	while start < len(poly) :
		# Forming a line from two consecutive points of polygon
		side = [poly[i], poly[(i + 1) % n]];
		if isIntersect(side, exline):
			 # If side is intersects exline
			if direction(side[0], p, side[1]) == 0:
				return onLine(side, p)
			count+=1
		i = (i + 1) % n
		start += 1
	 # When count is odd
	return count & 1;

