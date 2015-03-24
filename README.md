# WhichSide
This simple library is for dealing with the questions like "point is inside or outside of a polygon" or "point lies left side or right side of a line".


## Usage
```python
import whichside as ws

# polygon
polygon = ws.Polygon()
polygon.add_vertex(1, 1)
polygon.add_vertex(1, 2)
polygon.add_vertex(2, 3)
polygon.add_vertex(3, 2.6)
polygon.add_vertex(2.5, 0)

polygon.contains(1.5, 1.5) # True
polygon.contains(0, 1.5) # False
```
