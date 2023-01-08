import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import hvplot.pandas
from pathlib import Path

class Plotter:
    
    """
    
    """
    
    def __init__(self):
        self.rot = 45
        self.grid = True
        self.height = 750
        self.width = 1500
        self.alpha = .7
        self.hover_alpha = 1
        self.fontsize = {'title': 24,'labels': 15,'xticks': 10,'yticks': 10,'legend': 11,'legend_title': 14}
        self.bgcolor = '#F5F5F5'
        
    def get_image_path(self, title): 
        return Path(f'./Resources/images/plots/{title.lower().replace(" ","_")}.png')
        
    def line(self, df, title, bgcolor='#F5F5F5'):
        acp = 'Adjusted Close Price'
        title = title + ' ETF Adjusted Closing Prices'
        
        line_plot = df.hvplot(
                            title=title,
                            ylabel=f'{acp} - USD',
                            rot=self.rot,
                            grid=self.grid, 
                            height=self.height, 
                            width=self.width,
                            line_width=3,
                            hover_line_width=5,
                            group_label=acp,
                            alpha=self.alpha,
                            hover_alpha=self.hover_alpha,
                            ).opts(
                                fontsize=self.fontsize,
                                bgcolor=bgcolor
                            )
        
        hvplot.save(line_plot,self.get_image_path(title))
        
        return line_plot
        
    def bar(self, df, title):
        bar_plot = df.hvplot.bar(
                            title=title,
                            ylabel=title,
                            xlabel='ETF',
                            rot=self.rot,
                            grid=self.grid, 
                            height=self.height, 
                            width=self.width,
                            alpha=self.alpha,
                            hover_alpha=self.hover_alpha,
                            ).opts(
                                fontsize=self.fontsize,
                                bgcolor=self.bgcolor
                            )

        hvplot.save(bar_plot,self.get_image_path(title))

        return bar_plot
    
    def heatmap(self, df, title):
        etf_price = 'ETF Price'
        title = title + f' {etf_price} Correlation'
        
        # Create correlation matrix DataFrame
        correlation_df = df.corr()

        # Save figure
        fig = plt.figure(figsize=(15,8))
        # Set title
        plt.title(title, fontsize=15, fontweight='bold')
        # Generate heatmap plot          
        sns.heatmap(correlation_df,
                        cbar_kws={'shrink': .5},
                        mask=np.triu(np.ones_like(correlation_df, dtype=bool)),
                        vmin=-1,
                        vmax=1,
                        center=0,
                        cmap='vlag', 
                        linewidth=1,
                        square=True).set(xlabel=etf_price,
                                         ylabel=etf_price);
        fig.savefig(self.get_image_path(title))