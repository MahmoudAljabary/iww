import sys
import os
import itertools
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 100)

sys.path.append(os.path.realpath(os.path.abspath('../utilities')))


from dom_mapper import DOM_Mapper



class CLG(DOM_Mapper):
    
    FEATURES_LABELS = ['POS_LEFT', 'POS_RIGHT', 'POS_TOP', 'POS_BOTTOM', 'POS_X', 'POS_Y', 'POS_DIST', 
                        'AREA_SIZE', 'AREA_DIST', 'FONT_COLOR_POPULARITY', 'FONT_SIZE', 'FONT_SIZE_POPULARITY', 
                        'VISIBLE_CHAR', 'TEXT_RATIO', 'TAG_SCORE','TAG_DENSITY', 'LINK_DENSITY']
    
    
    def __init__(self):
        #...
        pass


# =============================================================================
#     def absolute(self):
#               
#         self.map(self.DOM, fun1 = self.__absolute)
#         
#         pass
# =============================================================================
    
    
# =============================================================================
#     def __absolute(self, node):
#         
#         node['CLG'] = {}
#         node['CLG']['absolute'] = {}
#         node['CLG']['absolute']['centerX'] = node['bounds']['x']
#         node['CLG']['absolute']['centerY'] = node['bounds']['y']
#         
# # =============================================================================
# #         top = self.reduce(node, fun = lambda x,y: x if x['bounds']['top'] < y['bounds']['top'] else y)
# #         bottom = self.reduce(node, fun = lambda x,y: x if x['bounds']['bottom'] < y['bounds']['bottom'] else y)
# #         left = self.reduce(node, fun = lambda x,y: x if x['bounds']['left'] < y['bounds']['left'] else y)
# #         right = self.reduce(node, fun = lambda x,y: x if x['bounds']['right'] < y['bounds']['right'] else y)
# # =============================================================================
#         
#         top, bottom, left, right = itertools.repeat(node, 4)
#         
#         for child in node['children']:
#             
#             top = child if child['bounds']['top'] < top['bounds']['top'] else top
#             bottom = child if child['bounds']['bottom'] < bottom['bounds']['bottom'] else bottom
#             left = child if child['bounds']['left'] < left['bounds']['left'] else left
#             right = child if child['bounds']['right'] < right['bounds']['right'] else right
#             
#             node['CLG']['absolute']['centerX'] += child['bounds']['x']
#             node['CLG']['absolute']['centerY'] += child['bounds']['y']
#             
#             
# =============================================================================
# #          node['CLG']['absolute']['centerX'] = 0
# #          node['CLG']['absolute']['centerY'] = 0  
# #          center = self.reduce(node, fun = self.__center)    
# =============================================================================
#         
#         
#         node['CLG']['absolute']['absolute_top'] = top['bounds']['top']
#         node['CLG']['absolute']['absolute_bottom'] = bottom['bounds']['bottom'] 
#         node['CLG']['absolute']['absolute_left'] = left['bounds']['left']
#         node['CLG']['absolute']['absolute_right'] = right['bounds']['right'] 
#         node['CLG']['absolute']['centerX'] = node['CLG']['absolute']['centerX'] / (len(node['children']) + 1)
#         node['CLG']['absolute']['centerY'] = node['CLG']['absolute']['centerY'] / (len(node['children']) + 1)
#         
#         return node        
#         
#         pass
# =============================================================================
    
    
# =============================================================================
#      def __center(self, x, y):
#          
#          if x.get('CLG') == None:
#              x['CLG'] = {}
#              x['CLG']['absolute'] = {}
#              x['CLG']['absolute']['centerX'] = 0
#              x['CLG']['absolute']['centerY'] = 0
#          
#          x['CLG']['absolute']['centerX'] += y['bounds']['x']
#          x['CLG']['absolute']['centerY'] += y['bounds']['y']
#          
#          return x
#          
#          pass
# =============================================================================
     
        
    def absolute(self):
        
        self.map(
                self.DOM, 
                fun1 = self.__init_absolute, 
                fun3 = self.__absolute,
                fun4 = self.__end_absolute)
        
        pass
    
    
    def __init_absolute(self, node):
        
        node['CLG'] = {}
        node['CLG']['absolute'] = {}
        node['CLG']['absolute']['absolute_top'] = node['bounds']['top']
        node['CLG']['absolute']['absolute_bottom'] = node['bounds']['bottom'] 
        node['CLG']['absolute']['absolute_left'] = node['bounds']['left']
        node['CLG']['absolute']['absolute_right'] = node['bounds']['right']
        node['CLG']['absolute']['centerX'] = node['bounds']['x']
        node['CLG']['absolute']['centerY'] = node['bounds']['y']
        
        return node
    
        pass
    

    
    
    def __absolute(self, parent, child):
        
# =============================================================================
#         top = self.reduce(node, fun = lambda x,y: x if x['CLG']['absolute']['absolute_top'] < y['CLG']['absolute']['absolute_top'] else y)
#         bottom = self.reduce(node, fun = lambda x,y: x if x['CLG']['absolute']['absolute_top'] < y['CLG']['absolute']['absolute_top'] else y)
#         left = self.reduce(node, fun = lambda x,y: x if x['CLG']['absolute']['absolute_top'] < y['CLG']['absolute']['absolute_top'] else y)
#         right = self.reduce(node, fun = lambda x,y: x if x['CLG']['absolute']['absolute_top'] < y['CLG']['absolute']['absolute_top'] else y)
# =============================================================================
        
        top = parent if parent['CLG']['absolute']['absolute_top'] < child['CLG']['absolute']['absolute_top'] else child
        bottom = parent if parent['CLG']['absolute']['absolute_bottom'] < child['CLG']['absolute']['absolute_bottom'] else child
        left = parent if parent['CLG']['absolute']['absolute_left'] < child['CLG']['absolute']['absolute_left'] else child
        right = parent if parent['CLG']['absolute']['absolute_right'] < child['CLG']['absolute']['absolute_right'] else child
     
        parent['CLG']['absolute']['centerX'] += child['CLG']['absolute']['centerX']
        parent['CLG']['absolute']['centerY'] += child['CLG']['absolute']['centerY']
        
        parent['CLG']['absolute']['absolute_top'] = top['CLG']['absolute']['absolute_top']
        parent['CLG']['absolute']['absolute_bottom'] = bottom['CLG']['absolute']['absolute_bottom']
        parent['CLG']['absolute']['absolute_left'] = left['CLG']['absolute']['absolute_left']
        parent['CLG']['absolute']['absolute_right'] = right['CLG']['absolute']['absolute_right'] 
        
        return parent, child
        
        pass
    
    
    
    def __end_absolute(self, node):
        
        node['CLG']['absolute']['centerX'] = node['CLG']['absolute']['centerX'] / (len(node['children']) + 1)
        node['CLG']['absolute']['centerY'] = node['CLG']['absolute']['centerY'] / (len(node['children']) + 1)
        
        return node
        pass
        
    
    def relative(self):
        
        self.map(self.DOM, fun1 = self.__relative)
        
        pass
    
    
    
    def __relative(self, node):
        
        node['CLG']['relative'] = {
                'relative_top': node['CLG']['absolute']['absolute_top'] / self.DOM['bounds']['height'],
                'relative_bottom': node['CLG']['absolute']['absolute_bottom'] / self.DOM['bounds']['height'],
                'relative_left': node['CLG']['absolute']['absolute_left'] / self.DOM['bounds']['width'],
                'relative_right': node['CLG']['absolute']['absolute_right'] / self.DOM['bounds']['width'],
                'centerX': node['CLG']['absolute']['centerX'] / self.DOM['CLG']['absolute']['centerX'],
                'centerY': node['CLG']['absolute']['centerY'] / self.DOM['CLG']['absolute']['centerY']                
        }
        
        return node
    
        pass
    
    
    
    
    def perfect(self):
                
        pass

    
    
    def adjust(self):
        
        pass
    
    pass





if __name__ == '__main__':
    
    clg = CLG()
    clg.retrieve_DOM_tree(os.path.realpath('../datasets/extracted_data/0000.json'))
    #arr = clg.toArray(features = ['tagName','xpath'])
    #print(arr)
    clg.absolute()
    clg.relative()
    print(clg.DOM['children'][2]['CLG'])
    
    pass