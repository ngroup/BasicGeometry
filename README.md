# tiny2d
This tiny library is for dealing with application of 2D geometry in Python.


## Usage
A minimal tiny2d application looks like this:
```python
import tiny2d as t2d

# create a Polygon
polygon = t2d.Polygon([(1, 1), (1, 2), (2, 3), (3, 2.6), (2.5, 0)])

# tell whether a point is inside the polygon
polygon.contains(1.5, 1.5) # True
polygon.contains(0, 1.5) # False
```

### Vector2D
```python
vec1 = Vector2D(1, 2)
vec2 = Vector2D(3, 5)
vec1 += vec2 # vec1 = (4, 7)
```
