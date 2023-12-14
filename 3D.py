
from manim import *

class ThreeDAxesScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        # Mark x-axis
        x_labels = VGroup()
        x_values = [-5,-4,-3, -2, -1, 0, 1, 2, 3,4,5]
        for value in x_values:
            label = Integer(value,color=RED).scale(0.6)
            label.next_to(axes.x_axis.number_to_point(value),DOWN)
            x_labels.add(label)

        # Mark y-axis
        y_labels = VGroup()
        y_values = [-4,-3, -2, -1, 1, 2, 3,4]
        for value in y_values:
            label = Integer(value,color=RED).scale(0.6)
            label.next_to(axes.y_axis.number_to_point(value), LEFT)
            y_labels.add(label)

        # Mark z-axis
        z_labels = VGroup()
        z_values = [-4,-3, -2, -1, 1, 2, 3,4]
        for value in z_values:
            label = Integer(value,color=RED).scale(0.6)
            label.next_to(axes.z_axis.number_to_point(value), OUT)
            z_labels.add(label)

        surface = Surface(
            lambda u, v: [u, v, 0],
            u_range=(1,3),
            v_range=(1,3),
            checkerboard_colors=[BLUE_B,BLUE_D],
            resolution=(20, 20)
        )

        cuboid = Prism(dimensions=[3, 3, 2], fill_color=YELLOW, fill_opacity=0.1,stroke_width=1).shift(RIGHT*1.5).shift(UP*1.5).shift(OUT*0.99) #centre of mass
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        self.wait(0.5)
        self.play(Create(x_labels))
        self.wait(0.5)
        self.play(Create(y_labels))
        self.wait(0.5)
        self.play(Create(z_labels))
        self.wait(0.5)

        
        self.play(Create(surface))
        self.wait()

        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait()

        # Move the camera back to the initial angle
        # self.move_camera(phi=75* DEGREES, theta=45 * DEGREES)
        # self.wait()

        surface.generate_target()
        surface.target.shift(OUT*2)
        self.play(MoveToTarget(surface))

        # self.move_camera(phi=0 * DEGREES, theta=90 * DEGREES)
        # self.wait()

        # # Move the camera back to the initial angle
        # self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES)
        # self.wait()
        self.move_camera(phi=45 * DEGREES, theta=30 * DEGREES)
        self.wait()

        # self.move_camera(phi=-45 * DEGREES, theta=-30 * DEGREES)
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES)
        self.wait()
         
        self.play(Create(cuboid))
        self.wait()

        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait()

        group  = VGroup(cuboid, surface)

        self.move_camera(phi=60 * DEGREES, theta=60 * DEGREES)

        self.begin_ambient_camera_rotation(rate = 0.2)
        self.set_camera_orientation(phi=60 * DEGREES, theta=60 * DEGREES)
        self.wait(3.5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi= 60 * DEGREES, theta=120 * DEGREES)

        self.play(ApplyMatrix([[1,0,.5],[0,1,.5],[0, 0, 1]], group ))

        self.wait(0.5)

        self.move_camera(phi= 60 * DEGREES, theta=120 * DEGREES)
        self.begin_ambient_camera_rotation(rate = -0.2)

        self.set_camera_orientation(phi= 60 * DEGREES, theta=120 * DEGREES)
        self.wait(4)

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=60 * DEGREES, theta=60 * DEGREES)
        self.play(FadeOut(cuboid))
        self.wait(2)

        # self.wait(2)
        surface.generate_target()
        surface.target.shift(-1*OUT*2)
        self.play(MoveToTarget(surface))
        

