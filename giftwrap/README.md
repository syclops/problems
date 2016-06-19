# Gift Wrapping Algorithm

Use the [gift wrapping
algorithm](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm) to solve the
convex hull problem.

## Input

A set of points defined by their x and y coordinates, one per line. No two
points will be the same.

Example:

```
1 1
0 1
1 0
1 2
3 0
0 0
2 2
2 1
3 1
4 0
2 0
```

## Output

The set of points in the convex hull in clockwise order, starting with the lower
leftmost point.

Example for the above example input:

```
0 0
0 1
1 2
2 2
3 1
4 0
3 0
2 0
1 0
```
