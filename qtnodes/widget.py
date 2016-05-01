"""Editor widget."""

from PySide import QtGui
from PySide import QtCore

from .node import Node
from .view import GridView


class NodeGraphWidget(QtGui.QWidget):
    """Display the node graph and offer editing functionality."""

    def __init__(self, parent=None):
        super(NodeGraphWidget, self).__init__(parent=parent)

        self.scene = QtGui.QGraphicsScene()
        self.view = GridView()
        self.view.setScene(self.scene)

        self.view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.view.setViewportUpdateMode(
            QtGui.QGraphicsView.FullViewportUpdate)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.nodeClasses = []

    def keyPressEvent(self, event):
        """React on various keys regarding Nodes."""

        # Delete selected nodes.
        if event.key() == QtCore.Qt.Key.Key_Delete:
            selectedNodes = [i for i in self.scene.selectedItems()
                             if isinstance(i, Node)]
            for node in selectedNodes:
                node.destroy()

        super(NodeGraphWidget, self).keyPressEvent(event)

    def contextMenuEvent(self, event):
        """Show a menu to create registered Nodes."""
        menu = QtGui.QMenu(self)
        action = menu.addAction("Create Nodes")
        menu.addSeparator()
        for cls in self.nodeClasses:
            className = cls.__name__
            action = menu.addAction(className)
            # http://stackoverflow.com/questions/20390323/pyqt-dynamic-generate-qmenu-action-and-connect  # noqa
            action.triggered[()].connect(
                lambda cls=cls: self._createNode(cls))
        menu.exec_(event.globalPos())

        super(NodeGraphWidget, self).contextMenuEvent(event)

    def _createNode(self, cls, atMousePos=True, center=True):
        """The class must provide defaults in its constructor.

        We ensure the scene immediately gets the Node added, otherwise
        the GC could snack it up right away.
        """
        node = cls()
        self.addNode(node)

        if atMousePos:
            mousePos = self.view.mapToScene(
                self.mapFromGlobal(QtGui.QCursor.pos()))
            node.setPos(mousePos)
        if center:
            self.view.centerOn(node.pos())

    def registerNodeClass(self, cls):
        if cls not in self.nodeClasses:
            self.nodeClasses.append(cls)

    def unregisterNodeClass(self, cls):
        if cls in self.nodeClasses:
            self.nodeClasses.remove(cls)

    def addNode(self, node):
        """Add a Node to the current scene.

        This is only necessary when the scene has not been passed on
        creation, e.g. when you create a Node programmatically.
        """
        if node not in self.scene.items():
            self.scene.addItem(node)
