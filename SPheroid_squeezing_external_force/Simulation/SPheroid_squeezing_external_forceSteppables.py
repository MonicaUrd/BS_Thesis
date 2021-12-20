
from cc3d.core.PySteppables import *

class SPheroid_squeezing_external_forceSteppable(SteppableBasePy):

    def __init__(self,frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        
#Size of the spheroid = 30
        for x in range(290, 320, 5):
            for y in (61, 86):
                cell = self.new_cell(self.PERIPHERY)
                self.cell_field[x:x+5, y:y+5, 0] = cell
                
        for y in range(61, 89, 5):
            for x in (290, 315):
                cell = self.new_cell(self.PERIPHERY)
                self.cell_field[x:x+5, y:y+5, 0] = cell


# # CORE for mature spheroid;                
#         for x in range(295, 300, 10):
#             for y in range(66, 70, 10):
#                 cell = self.new_cell(self.CORE)
#                 self.cell_field[x:x+19, y:y+19, 0] = cell

# # CORE for solid sphere:                
        for x in range(295, 311, 5):
            for y in range(66, 82, 5):
                cell = self.new_cell(self.CORE)
                self.cell_field[x:x+5, y:y+5, 0] = cell

#Size of the spheroid = 60
#         for x in range(325, 380, 5):
#             for y in (51, 101):
#                 cell = self.new_cell(self.PERIPHERY)
#                 self.cell_field[x:x+5, y:y+5, 0] = cell
                
#         for y in range(56, 98, 5):
#             for x in (325, 375):
#                 cell = self.new_cell(self.PERIPHERY)
#                 self.cell_field[x:x+5, y:y+5, 0] = cell


# # # CORE for mature spheroid;                
# #         for x in range(325, 330, 50):
# #             for y in range(51, 60, 10):
# #                 cell = self.new_cell(self.CORE)
# #                 self.cell_field[x:x+49, y:y+49, 0] = cell

# # CORE for solid sphere:                
#         for x in range(330, 371, 5):
#             for y in range(56, 101, 5):
#                 cell = self.new_cell(self.CORE)
#                 self.cell_field[x:x+5, y:y+5, 0] = cell
                
#CHAMBER with diameter = 16:               
        for x in range(160, 245, 5):
            for y in (63, 84):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell
                
        for x in (245, 160):
            for y in (63, 58, 53, 48, 43, 38, 33, 28, 23, 18, 13, 8, 84, 89, 94, 99, 104, 109, 114, 119, 124, 129, 134, 139):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell
                
        for x in (250, 155):
            for y in (58, 53, 48, 43, 38, 33, 28, 23, 18, 13, 8, 89, 94, 99, 104, 109, 114, 119, 124, 129, 134, 139):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell

        for x in (255, 150):
            for y in (53, 48, 43, 38, 33, 28, 23, 18, 13, 8, 94, 99, 104, 109, 114, 119, 124, 129, 134, 139):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell
                
        for x in (260, 145):
            for y in (53, 48, 43, 38, 33, 28, 23, 18, 13, 8, 99, 104, 109, 114, 119, 124, 129, 134, 139):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell
        
        for x in (265, 140):
            for y in (48, 43, 38, 33, 28, 23, 18, 13, 8, 104, 109, 114, 119, 124, 129, 134, 139):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell
        
        for x in (270, 135):
            for y in (43, 38, 33, 28, 23, 18, 13, 8, 109, 114, 119, 124, 129, 134, 139):
                cell = self.new_cell(self.CHAMBER)
                self.cell_field[x:x+5, y:y+5, 0] = cell
        
        
#CHAMBER with diameter = 12:                
#         for x in range(110, 195, 5):
#             for y in (65, 82):
#                 cell = self.new_cell(self.CHAMBER)
#                 self.cell_field[x:x+5, y:y+5, 0] = cell
                
#         for x in range(195, 200, 5):
#             for y in (10, 15, 30, 35, 20, 25, 50, 45, 40, 102, 107, 55, 65, 60, 82, 87, 92, 97, 112, 117, 122, 127, 132):
#                 cell = self.new_cell(self.CHAMBER)
#                 self.cell_field[x:x+5, y:y+5, 0] = cell

        self.plot_win_x = self.add_new_plot_window(title='Cell COM Track',
                                                 x_axis_title='MCS', x_scale_type='linear',
                                                 y_axis_title='COM', y_scale_type='linear',
                                                 grid=False)
        self.plot_win_x.add_plot("Trackxa", style='dot', color='green', size=4)
        self.plot_win_x.add_plot("Trackya", style='dot', color='blue', size=4) 
        self.plot_win_x.add_plot("Trackxb", style='dot', color='green', size=4)
        self.plot_win_x.add_plot("Trackyb", style='dot', color='blue', size=4) 
#Creating a plot for tracking volume and surface area of the core:

#         self.plot_win_x = self.add_new_plot_window(title='Volume of Core',
#                                                  x_axis_title='Number of MCS', x_scale_type='linear',
#               
#         #Creating a plot for surface area of core:
#         self.plot_win_y = self.add_new_plot_window(title='Surface area of the core',
#                                              x_axis_title='Number of MCS', x_scale_type='linear',
#                                              y_axis_title='Surface area of the core', y_scale_type='linear',
#                                                    y_axis_title='Volume of the core', y_scale_type='linear',
#                                                  grid=False)
#         self.plot_win_x.add_plot("Trackv", style='dot', color='white', size=2)
#                                     grid=False)
#         self.plot_win_y.add_plot("Tracksa", style='dot', color='white', size=2)
        
        
#     def step(self,mcs):
#         # Tracking the volume and surface area of the core every 100th MCS
#         if mcs % 10 == 0:
#             for cell in self.cell_list_by_type(self.CORE):

#                 # Approach 2: using the plot:
#                 self.plot_win_x.add_data_point("Trackv",mcs,cell.volume)  
#                 self.plot_win_y.add_data_point("Tracksa",mcs,cell.surface)


    def step(self,mcs):
        # just tracking the center of "acell" type every 100th MCS
        if mcs % 10 == 0:
            for cell in self.cell_list_by_type(self.PERIPHERY):

                # Approach 2: using the plot:
                self.plot_win_x.add_data_point("Trackxa",mcs,cell.xCOM)  
                self.plot_win_x.add_data_point("Trackya",mcs,cell.yCOM)
                
            for cell in self.cell_list_by_type(self.CORE):

                # Approach 2: using the plot:
                self.plot_win_x.add_data_point("Trackxb",mcs,cell.xCOM)  
                self.plot_win_x.add_data_point("Trackyb",mcs,cell.yCOM)
                
        if mcs % 10000 == 0:
            if self.output_dir is not None:
                output_path = Path(self.output_dir).joinpath("comPlots_Hollow_size=30_pc=0_pp=10.txt")
                self.plot_win_x.save_plot_as_data(output_path, CSV_FORMAT)
                print(output_path)       


    