from manim import *
class BubbleSortVisual:
    def __init__(self, scene):
        self.scene = scene
        self.elements = []
        self.visual_elements = [] 

    def create_bubble_sort(self, values):
        for value in values:
            self.elements.append(value)
            self.add_element(value) # create a new node for each value
            print(self.elements)
            print(self.visual_elements)
        self.animate_elements()
            
    def add_element(self, value):
        new_circle = Circle(radius=0.5, color=BLUE)
        new_text = Text(str(value)).move_to(new_circle.get_center())
        new_element = VGroup(new_circle, new_text)
        if not self.visual_elements:
            new_element.to_edge(LEFT)
        else:
            last_element = self.visual_elements[-1]
            new_element.next_to(last_element, RIGHT, buff=0.2)
        self.visual_elements.append(new_element)

    def animate_elements(self):
        animations = [Write(element) for element in self.visual_elements]
        self.scene.play(AnimationGroup(*animations, lag_ratio=0))

    
    def sort_elements(self):
    
        n = len(self.elements)
        for i in range(n):

            swapped = False

            for j in range(0, n-i-1):

                if self.elements[j] > self.elements[j+1]:

                    self.elements[j], self.elements[j+1] = self.elements[j+1], self.elements[j]
                    pos1 = self.visual_elements[j].get_center()
                    pos2 = self.visual_elements[j+1].get_center()
                    self.scene.play(
                        self.visual_elements[j].animate.move_to(pos2),
                        self.visual_elements[j+1].animate.move_to(pos1)
                    )
                    self.visual_elements[j], self.visual_elements[j+1] = self.visual_elements[j+1], self.visual_elements[j]

                    swapped = True

            if swapped == False:
                break


    

class BubbleSortScene(Scene):
    def construct(self):
        bubble_sort = BubbleSortVisual(self)
        bubble_sort.create_bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        bubble_sort.sort_elements()

