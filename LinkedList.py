from manim import *

class LinkedListVisual:
    def __init__(self, scene):
        self.scene = scene
        self.visual_nodes = [] # create list of nodes

    def create_linked_list(self, values):
        for value in values:
            self.add_node_visual(value) # create a new node for each value

    def add_node_visual(self, value):
        new_circle = Circle(radius=0.5, color=BLUE)
        new_text = Text(str(value)).move_to(new_circle.get_center())
        new_node = VGroup(new_circle, new_text)

        print(self.visual_nodes)
        if not self.visual_nodes: # if visual nodes is empty, set new node as first node
            new_node.to_edge(LEFT)
        else:
            last_node = self.visual_nodes[-1][0]
            new_node.next_to(last_node, RIGHT, buff=1) # move node to right of previous node
            arrow = Arrow(start=last_node.get_right(), end=new_node.get_left(), color=WHITE) # create arrow from previous node to new node
            
            #self.scene.play(Create(arrow))
        arrow = Arrow(
            start=new_node.get_right(),
            end=new_node.get_right() + RIGHT * 1,
            stroke_width=10
        )
        self.visual_nodes.append([new_node, arrow]) # add node to visual nodes

        self.scene.play(Write(new_node))
        self.scene.play(Write(arrow)) # may not work

        
        print(self.visual_nodes)

    def remove_node_visual(self, value):
        print(self.visual_nodes)
        i = 0
        for node, arrow in self.visual_nodes:
            i += 1
            print(f"i: {i}")
            if node[1].text == str(value): # if node is value to be removed
                print(self.visual_nodes)
                self.scene.play(node.animate.shift(DOWN * 2), arrow.animate.shift(DOWN * 2))
                self.scene.play(FadeOut(node, arrow)) # remove node from scene
                self.visual_nodes.remove([node, arrow]) # remove node from visual nodes
                print(f"i: {i}")
                i -= 1
                print(f"i: {i}")
                print(self.visual_nodes)
                break

        for f in range(i, len(self.visual_nodes)):
            print(f"f: {f}")
            self.scene.play(self.visual_nodes[f][0].animate.shift(LEFT * 2))
            self.scene.play(self.visual_nodes[f][1].animate.shift(LEFT * 2))





class Visual(Scene):
    def construct(self):
        LL = LinkedListVisual(self)
        LL.create_linked_list([1, 2, 3, 4, 5, 6])
        LL.remove_node_visual(4)
        LL.add_node_visual(7)
        LL.remove_node_visual(2)
        LL.add_node_visual(8)
        LL.remove_node_visual(6)


        print(LL.visual_nodes)