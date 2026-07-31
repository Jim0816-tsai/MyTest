from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# 這裡使用 Kivy Garden 的 Graph 組件來繪製簡單走勢線
from kivy_garden.graph import Graph, MeshLinePlot

class StockApp(App):
    def build(self):
        # 建立主畫面版面
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='台股/美股 模擬走勢圖', size_hint_y=0.1))
        
        # 建立圖表元件
        graph = Graph(xlabel='時間', ylabel='價格', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=10,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=100, ymax=150)
                      
        # 模擬一段股市上升走勢數據
        plot = MeshLinePlot(color=[0, 1, 0, 1]) # 綠色走勢線
        plot.points = [(x, 100 + (x ** 0.8) + (x % 5)) for x in range(0, 101)]
        graph.add_widget(plot)
        
        layout.add_widget(graph)
        return layout

if __name__ == '__main__':
    StockApp().run()

