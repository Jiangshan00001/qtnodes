# qtnodes

Node graph visualization and editing with PySide.

Very **WIP** right now, the goal is to have a bunch of premade components that make it easy to implement a node graph to store and modify arbitrary data.

The UI part is coming along nicely, but no actual data handling is attached to it yet.

## UI Example

Although this graph makes no sense, it shows the current look and feel:

![](http://i.imgur.com/oBj0FBJ.png)

## Code Example

```python
from PySide import QtGui

from qtnodes import (Header, Node, InputKnob,
                     OutputKnob, NodeGraphWidget)


class Multiply(Node):

    def __init__(self, *args, **kwargs):
        super(Multiply, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text=self.__class__.__name__))
        self.addKnob(InputKnob(labelText="x"))
        self.addKnob(InputKnob(labelText="y"))
        self.addKnob(OutputKnob(labelText="value"))

app = QtGui.QApplication([])
graph = NodeGraphWidget()
graph.registerNodeClass(Multiply)
graph.addNode(Multiply())
graph.show()
app.exec_()
```

## Usage

To start a small demo:

    $ python -m qtnodes

### Scene

- **Pan the viewport**: Hold the middle mousebutton and drag.
- **Zoom the viewport**: Use the mouse wheel.
- **Save scene to file:** Rightclick > Scene > Save As...
- **Load scene from file:** Rightclick > Scene > Open File...
- **Merge scene from file:** Rightclick > Scene > Merge File...
- **Clear complete scene:** Rightclick > Scene > Clear Scene
- **Hold scene state:** Rightclick > Scene > Hold
- **Fetch scene state:** Rightclick > Scene > Fetch
- **Autolayout scene:** Rightclick > Scene > Auto Layout

### Nodes

- **Select a node**: Leftclick its header.
- **Select multiple nodes**: Leftclick and drag a rectangle over the nodes, release to select.
- **Create a node**: Rightclick > Nodes, choose a node type.
- **Move a node**: Leftclick and drag its header.
- **Delete a node**: Select it then press `DELETE`.
- **Create a connection**: Hover over a knob, then leftclick and drag to another knob. You can only connect inputs to outputs and vice versa.
- **Remove a connection**: Hold `ALT`, the connections turn red, click one to remove it.

## Credits

This started as a port of the original Qt/C++ tool `qnodeseditor` by Stanislaw Adaszewski, see:

http://algoholic.eu/qnodeseditor-qt-nodesports-based-data-processing-flow-editor/

Additional sources and inspirations:

- http://austinjbaker.com/node-editor-prototype
- http://nukengine.com/blog/category/all/qt-node-editor/
- http://blog.interfacevision.com/design/design-visual-progarmming-languages-snapshots/
- https://github.com/Tillsten/qt-dataflow